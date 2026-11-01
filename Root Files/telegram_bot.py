"""
telegram_bot.py - አማላጅ ፕላስ seller bot (aiogram 3.x).

What it verifies
  1. Ownership: the seller must be the channel *creator*, and the bot must be an admin of that channel.
  2. Size: real member count straight from Telegram.
  3. Engagement / fake-follower screening: average views of recent posts vs. member count, plus how uniform
     the views are (bought views look suspiciously flat).

Important limitation: the Telegram *Bot* API cannot read post views. For the engagement check, set
TG_API_ID / TG_API_HASH / TG_SESSION (a Telethon user session that can read the channel) and `pip install telethon`.
Without it the bot still verifies ownership + size, but the listing goes to manual review with no quality score.
The score is a heuristic, not proof - admins still review screenshots.

Env: BOT_TOKEN, API_BASE (default http://localhost:8000), BOT_API_KEY (same value as the backend)
"""
import asyncio
import logging
import os
import re
from decimal import Decimal, InvalidOperation
from statistics import mean, pstdev

import httpx
from aiogram import Bot, Dispatcher, F, Router
from aiogram.exceptions import TelegramAPIError
from aiogram.filters import Command, CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.types import CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup, Message

BOT_TOKEN = os.environ["BOT_TOKEN"]
API_BASE = os.getenv("API_BASE", "http://localhost:8000")
BOT_API_KEY = os.environ["BOT_API_KEY"]
SITE_URL = os.getenv("SITE_URL", "https://amalajplus.example")

router = Router()
log = logging.getLogger("amalaj-bot")


class Sell(StatesGroup):
    handle = State()
    price = State()
    revenue = State()
    category = State()
    description = State()
    confirm = State()


# ----------------------------------------------------------------------------- verification logic
def parse_handle(text: str) -> str | None:
    m = re.fullmatch(r"(?:https?://)?(?:t\.me/|telegram\.me/)?@?([A-Za-z][A-Za-z0-9_]{4,31})/?", text.strip())
    return f"@{m.group(1)}" if m else None


async def fetch_recent_views(handle: str, limit: int = 20) -> list[int] | None:
    """Post view counts via Telethon (optional). Returns None when not configured or unreadable."""
    api_id, api_hash, session = os.getenv("TG_API_ID"), os.getenv("TG_API_HASH"), os.getenv("TG_SESSION")
    if not (api_id and api_hash and session):
        return None
    try:
        from telethon import TelegramClient
        async with TelegramClient(session, int(api_id), api_hash) as client:
            msgs = await client.get_messages(handle, limit=limit)
            return [m.views for m in msgs if getattr(m, "views", None)]
    except Exception as exc:  # network, flood-wait, private channel...
        log.warning("view fetch failed for %s: %s", handle, exc)
        return None


def score_followers(members: int, views: list[int] | None) -> tuple[float | None, float | None]:
    """Returns (engagement_rate_percent, fake_followers_score 0..100). Heuristic only."""
    if not views or len(views) < 5 or members <= 0:
        return None, None
    avg = mean(views)
    er = avg / members * 100
    fake = 0.0
    if er < 3:
        fake += 55
    elif er < 8:
        fake += 30
    elif er < 15:
        fake += 10
    if len(views) >= 10 and avg > 0 and pstdev(views) / avg < 0.08:
        fake += 25  # near-identical views on every post: typical of purchased views
    if er > 150:
        fake += 20  # more views than members, usually via forwards/boosts - worth a human look
    return round(er, 1), float(min(fake, 100))


async def verify_channel(bot: Bot, user_id: int, handle: str) -> dict:
    chat = await bot.get_chat(handle)
    if chat.type != "channel":
        raise ValueError("not_channel")
    me = await bot.get_me()
    try:
        bot_member = await bot.get_chat_member(chat.id, me.id)
    except TelegramAPIError:
        raise ValueError("bot_not_admin")
    if bot_member.status != "administrator":
        raise ValueError("bot_not_admin")
    seller = await bot.get_chat_member(chat.id, user_id)
    if seller.status != "creator":
        raise ValueError("not_owner")
    members = await bot.get_chat_member_count(chat.id)
    views = await fetch_recent_views(handle)
    er, fake = score_followers(members, views)
    return {"title": chat.title, "members": members, "engagement_rate": er, "fake_score": fake,
            "description": chat.description or ""}


async def api(method: str, path: str, **kw) -> httpx.Response:
    async with httpx.AsyncClient(base_url=API_BASE, timeout=20, headers={"X-Bot-Key": BOT_API_KEY}) as c:
        return await c.request(method, path, **kw)


# ----------------------------------------------------------------------------- handlers
@router.message(CommandStart())
async def start(m: Message):
    await m.answer(
        "👋 እንኳን ወደ አማላጅ ፕላስ በደህና መጡ!\nWelcome to Amalaj Plus - secure escrow for digital accounts.\n\n"
        "/sell - ቻናልዎን ያረጋግጡና ይዘርዝሩ / verify and list your channel\n"
        "/cancel - ሂደቱን አቋርጥ / cancel\n\n"
        f"መጀመሪያ በ {SITE_URL} ላይ ይመዝገቡ እና የቴሌግራም መታወቂያዎን (ID: {m.from_user.id}) ያስገቡ።\n"
        f"First register at {SITE_URL} and add your Telegram ID: {m.from_user.id}"
    )


@router.message(Command("cancel"))
async def cancel(m: Message, state: FSMContext):
    await state.clear()
    await m.answer("ተሰርዟል። / Cancelled.")


@router.message(Command("sell"))
async def sell(m: Message, state: FSMContext):
    r = await api("GET", f"/bot/users/{m.from_user.id}")
    if r.status_code != 200:
        return await m.answer(f"❌ ይህ የቴሌግራም መታወቂያ ({m.from_user.id}) ከአካውንት ጋር አልተገናኘም።\n"
                              f"No account linked to this Telegram ID. Register at {SITE_URL} first.")
    await state.set_state(Sell.handle)
    await m.answer(
        "1️⃣ ቦቱን የቻናልዎ አድሚን ያድርጉት፤ ከዚያ የቻናል ስም ይላኩ።\n"
        "Make this bot an admin of your channel, then send the channel handle, e.g. @mychannel"
    )


ERRORS = {
    "not_channel": "❌ ይህ ቻናል አይደለም። / That is not a public channel.",
    "bot_not_admin": "❌ ቦቱ የቻናሉ አድሚን አይደለም። / Add this bot as a channel admin, then try again.",
    "not_owner": "❌ ቻናሉን የሚሸጠው ባለቤቱ (creator) ብቻ ነው። / Only the channel owner (creator) can list it.",
}


@router.message(Sell.handle, F.text)
async def got_handle(m: Message, state: FSMContext, bot: Bot):
    handle = parse_handle(m.text)
    if not handle:
        return await m.answer("የቻናል ስም ትክክል አይደለም። Example: @mychannel")
    await m.answer("⏳ በማረጋገጥ ላይ... / Verifying...")
    try:
        info = await verify_channel(bot, m.from_user.id, handle)
    except ValueError as e:
        return await m.answer(ERRORS.get(str(e), "Verification failed."))
    except TelegramAPIError as e:
        return await m.answer(f"❌ ቻናሉን ማግኘት አልተቻለም / Could not read that channel: {e.message}")
    await state.update_data(handle=handle, **info)
    if info["fake_score"] is None:
        quality = "ያልተለካ - በአስተዳዳሪ ይገመገማል / not measured - goes to manual review"
    else:
        quality = f"{round(100 - info['fake_score'])}/100 (engagement {info['engagement_rate']}%)"
    await state.set_state(Sell.price)
    await m.answer(f"✅ ባለቤትነት ተረጋግጧል / Ownership verified\n📢 {info['title']}\n👥 {info['members']:,}\n"
                   f"⭐ Quality score: {quality}\n\n2️⃣ የሚፈልጉት ዋጋ በብር? / Asking price in ETB?")


def parse_money(text: str) -> Decimal | None:
    try:
        v = Decimal(text.replace(",", "").strip())
        return v if v >= 0 else None
    except InvalidOperation:
        return None


@router.message(Sell.price, F.text)
async def got_price(m: Message, state: FSMContext):
    v = parse_money(m.text)
    if not v or v <= 0:
        return await m.answer("ቁጥር ብቻ ያስገቡ። Numbers only, e.g. 150000")
    await state.update_data(price=str(v))
    await state.set_state(Sell.revenue)
    await m.answer("3️⃣ ወርሃዊ ገቢ በብር (ከሌለ 0)? / Monthly revenue in ETB (0 if none)?")


@router.message(Sell.revenue, F.text)
async def got_revenue(m: Message, state: FSMContext):
    v = parse_money(m.text)
    if v is None:
        return await m.answer("ቁጥር ብቻ ያስገቡ። Numbers only.")
    await state.update_data(revenue=str(v))
    await state.set_state(Sell.category)
    await m.answer("4️⃣ ምድብ? / Category? (e.g. News, Entertainment, Business)")


@router.message(Sell.category, F.text)
async def got_category(m: Message, state: FSMContext):
    await state.update_data(category=m.text.strip()[:80])
    await state.set_state(Sell.description)
    await m.answer("5️⃣ አጭር መግለጫ ይጻፉ። / Short description (what the channel is about, audience, income sources).")


@router.message(Sell.description, F.text)
async def got_description(m: Message, state: FSMContext):
    await state.update_data(description=m.text.strip()[:4000])
    d = await state.get_data()
    kb = InlineKeyboardMarkup(inline_keyboard=[[
        InlineKeyboardButton(text="✅ አትም / Publish", callback_data="confirm"),
        InlineKeyboardButton(text="✖️ ሰርዝ / Cancel", callback_data="abort"),
    ]])
    await state.set_state(Sell.confirm)
    await m.answer(f"{d['title']} ({d['handle']})\n👥 {d['members']:,}  💰 {Decimal(d['price']):,.0f} ETB\n"
                   f"ወርሃዊ ገቢ / Monthly: {Decimal(d['revenue']):,.0f} ETB\n📂 {d['category']}\n\n"
                   "ከ2% ኮሚሽን ጋር በእስክሮው ብቻ መሸጥ ይችላሉ። Sales happen only through escrow (2% fee).", reply_markup=kb)


@router.callback_query(Sell.confirm, F.data == "abort")
async def abort(c: CallbackQuery, state: FSMContext):
    await state.clear()
    await c.message.edit_text("ተሰርዟል። / Cancelled.")
    await c.answer()


@router.callback_query(Sell.confirm, F.data == "confirm")
async def confirm(c: CallbackQuery, state: FSMContext):
    d = await state.get_data()
    payload = {
        "telegram_id": c.from_user.id, "handle": d["handle"], "account_title": d["title"], "category": d["category"],
        "followers_subscribers_count": d["members"], "monthly_revenue_etb": d["revenue"], "asking_price_etb": d["price"],
        "description": d["description"], "engagement_rate": d["engagement_rate"],
        "fake_followers_score": d["fake_score"], "bot_verified": True,  # ownership was verified above
    }
    r = await api("POST", "/bot/listings", json=payload)
    await state.clear()
    if r.status_code != 201:
        log.error("listing failed %s %s", r.status_code, r.text)
        await c.message.edit_text("❌ ማተም አልተቻለም። እባክዎ በኋላ ይሞክሩ። / Could not publish. Try again later.")
        return await c.answer()
    res = r.json()
    if res["status"] == "Active":
        text = f"🎉 ዝርዝርዎ ታትሟል! / Listing #{res['listing_id']} is live. Quality score: {res['quality_score']}/100"
    else:
        text = (f"📝 ዝርዝር #{res['listing_id']} ለግምገማ ተልኳል። / Listing #{res['listing_id']} is pending admin review "
                "(the quality score was too low or could not be measured).")
    await c.message.edit_text(text)
    await c.answer()


@router.message(F.text)
async def fallback(m: Message):
    await m.answer("/sell - ለመሸጥ / to sell  |  /start - እገዛ / help")


async def main():
    logging.basicConfig(level=logging.INFO)
    bot = Bot(BOT_TOKEN)
    dp = Dispatcher(storage=MemoryStorage())
    dp.include_router(router)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
