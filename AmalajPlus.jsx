import { useState, useEffect, useCallback } from "react";

/* አማላጅ ፕላስ - Dark Mode Escrow & Digital Asset Marketplace Hub */
const API = "http://localhost:8000";
const PLATFORMS = ["TikTok", "YouTube", "Telegram", "Instagram", "Facebook", "X_Twitter", "Website_SaaS"];
const PLABEL = { TikTok: "TikTok", YouTube: "YouTube", Telegram: "Telegram", Instagram: "Instagram", Facebook: "Facebook", X_Twitter: "X (Twitter)", Website_SaaS: "Websites / SaaS" };

const T = {
  en: {
    market: "Marketplace", sell: "Sell an Account", deals: "My Deals", archive: "Sold Archive", admin: "Admin",
    login: "Sign In", register: "Create Account", logout: "Sign Out", all: "All Platforms",
    fullName: "Full Name", phone: "Phone Number", email: "Email (optional)", password: "Password", tgId: "Telegram ID (optional)",
    followers: "Followers", revenue: "Monthly Revenue", price: "Asking Price", engagement: "Engagement", category: "Category",
    description: "Description", title: "Account Title", proof: "Analytics Screenshot", handle: "Handle / Link (Private)",
    quality: "Quality Score", submit: "Submit for Review", startEscrow: "Buy with Escrow", agreed: "Agreed Amount (ETB)",
    fee: "Amalaj Fee (2%)", payout: "Seller Receives", cooldown: "Safety Hold (Days)", cancel: "Cancel", back: "Back",
    empty: "No listings match these filters yet.", noDeals: "You have no deals yet.", noArchive: "No completed deals yet.",
    "Very Good Price": "Very Good Price", "Fair Price": "Fair Price", "High Price": "High Price",
    transferred: "Credentials Transferred", confirmAccess: "Confirm Access", dispute: "Open Dispute",
    confirmDeposit: "Confirm Deposit", holdLeft: "Left in Safety Hold", payRef: "Pay into Escrow Reference",
    chat: "Deal Chat", send: "Send", offPlatform: "Direct negotiations or outside payments are prohibited.",
    pending: "Pending Review", approve: "Approve", suspend: "Suspend", release: "Release Funds", refund: "Refund Buyer",
    disputes: "Disputes", review: "Pending Listings", reason: "Describe problem (min 10 chars)", note: "Resolution Note",
    sellerNote: "Listings are verified before publishing to ensure transaction safety.",
    signInFirst: "Sign in to continue.", saved: "Submitted! Pending admin review.", sold: "Sold",
  },
  am: {
    market: "ገበያ", sell: "አካውንት ይሽጡ", deals: "የእኔ ስምምነቶች", archive: "የተሸጡ ቻናሎች", admin: "አስተዳዳሪ",
    login: "ግባ", register: "ተመዝገብ", logout: "ወጣ", all: "ሁሉም ፕላትፎርሞች",
    fullName: "ሙሉ ስም", phone: "ስልክ ቁጥር", email: "ኢሜይል (አማራጭ)", password: "የይለፍ ቃል", tgId: "የቴሌግራም መታወቂያ",
    followers: "ተከታዮች", revenue: "ወርሃዊ ገቢ", price: "የሚጠየቀው ዋጋ", engagement: "ተሳትፎ", category: "ምድብ",
    description: "መግለጫ", title: "የአካውንት ርዕስ", proof: "የማረጋገጫ ፎቶ", handle: "ስም / ሊንክ (ለግምገማ ብቻ)",
    quality: "የጥራት ነጥብ", submit: "ለግምገማ ላክ", startEscrow: "በእስክሮው ግዛ", agreed: "የተስማማው ዋጋ (ብር)",
    fee: "የአማላጅ ክፍያ (2%)", payout: "ሻጭ የሚቀበለው", cooldown: "የደህንነት እገዳ (ቀናት)", cancel: "ተው", back: "ተመለስ",
    empty: "ከዚህ ማጣሪያ ጋር የሚሄድ ዝርዝር የለም።", noDeals: "እስካሁን ምንም ስምምነት የለዎትም።", noArchive: "እስካሁን የተጠናቀቀ ስምምነት የለም።",
    "Very Good Price": "በጣም ጥሩ ዋጋ", "Fair Price": "ተገቢ ዋጋ", "High Price": "ከፍተኛ ዋጋ",
    transferred: "መግቢያውን አስተላልፌያለሁ", confirmAccess: "መግባት ችያለሁ - እገዳውን ጀምር", dispute: "አለመግባባት አንሳ",
    confirmDeposit: "ክፍያ አረጋግጥ", holdLeft: "የደህንነት እገዳ ቀርቷል", payRef: "በዚህ ማመሳከሪያ ወደ እስክሮው ይክፈሉ",
    chat: "የስምምነት ውይይት", send: "ላክ", offPlatform: "ከአማላጅ ፕላስ ውጭ መደራደር ወይም መክፈል በጥብቅ ክልክል ነው፤ ይመዘገባል።",
    pending: "ግምገማ በመጠባበቅ ላይ", approve: "አጽድቅ", suspend: "አግድ", release: "ለሻጭ ልቀቅ", refund: "ለገዢ መልስ",
    disputes: "አለመግባባቶች", review: "ግምገማ የሚጠብቁ ዝርዝሮች", reason: "ችግሩን ይግለጹ (ቢያንስ 10 ፊደል)", note: "የውሳኔ ማስታወሻ",
    sellerNote: "ዝርዝሮች ለደህንነት ሲባል ከመታተማቸው በፊት በአስተዳዳሪ ይገመገማሉ።",
    signInFirst: "ለመቀጠል ይግቡ።", saved: "ተልኳል። አስተዳዳሪ ዝርዝርዎን ይገመግማል።", sold: "ተሽጧል",
  },
};

const STATUS = {
  en: { Pending_Deposit: "Waiting for Deposit", Secured_in_Escrow: "Secured in Escrow", Credentials_Transferred: "Login Transferred", Buyer_Verification_Period: "Safety Hold", Completed: "Completed", Disputed: "Disputed", Refunded: "Refunded" },
  am: { Pending_Deposit: "ክፍያ በመጠባበቅ ላይ", Secured_in_Escrow: "በእስክሮው ተቀምጧል", Credentials_Transferred: "መግቢያ ተላልፏል", Buyer_Verification_Period: "የደህንነት እገዳ", Completed: "ተጠናቋል", Disputed: "አለመግባባት", Refunded: "ተመላሽ ተደርጓል" },
};

const TAG_STYLE = { "Very Good Price": "bg-emerald-900/60 text-emerald-300 border border-emerald-500/30", "Fair Price": "bg-amber-900/60 text-amber-300 border border-amber-500/30", "High Price": "bg-rose-900/60 text-rose-300 border border-rose-500/30" };
const etb = (n) => Number(n).toLocaleString("en-US", { maximumFractionDigits: 2 }) + " ETB";
const fmtK = (n) => (n >= 1e6 ? (n / 1e6).toFixed(1) + "M" : n >= 1e3 ? (n / 1e3).toFixed(1) + "K" : String(n));

const inputCls = "w-full border border-slate-700 rounded-lg px-3 py-2 text-white bg-slate-900/80 focus:outline-none focus:border-amber-400 focus:ring-1 focus:ring-amber-400 placeholder-slate-500 transition-all";
const btn = "px-4 py-2 rounded-lg font-bold transition-all focus:outline-none focus:ring-2 focus:ring-amber-400 active:scale-95";
const btnPrimary = btn + " bg-amber-400 text-slate-950 hover:bg-amber-300 shadow-lg shadow-amber-400/10";
const btnGhost = btn + " bg-slate-800 text-slate-200 border border-slate-700 hover:bg-slate-700 hover:text-white";

export default function AmalajPlus() {
  const [lang, setLang] = useState("am");
  const [view, setView] = useState("market");
  const [token, setToken] = useState(null);
  const [me, setMe] = useState(null);
  const [showAuth, setShowAuth] = useState(false);
  const [toast, setToast] = useState(null);
  const [selected, setSelected] = useState(null);
  const t = T[lang];

  const notify = (msg, bad = false) => { setToast({ msg, bad }); setTimeout(() => setToast(null), 5000); };

  const api = useCallback(async (path, { method = "GET", json, form } = {}) => {
    const headers = {};
    if (token) headers.Authorization = `Bearer ${token}`;
    if (json) headers["Content-Type"] = "application/json";
    const res = await fetch(API + path, { method, headers, body: form || (json ? JSON.stringify(json) : undefined) });
    const data = await res.json().catch(() => ({}));
    if (!res.ok) {
      const d = data.detail;
      throw new Error(Array.isArray(d) ? d.map((e) => e.msg).join("; ") : d || `Error ${res.status}`);
    }
    return data;
  }, [token]);

  const needLogin = () => { notify(t.signInFirst, true); setShowAuth(true); };
  const go = (v) => { setView(v); setSelected(null); };

  const nav = [["market", t.market], ["sell", t.sell], ["deals", t.deals], ["archive", t.archive], ...(me?.is_admin ? [["admin", t.admin]] : [])];

  return (
    <div className="min-h-screen bg-slate-950 text-slate-100 selection:bg-amber-400 selection:text-slate-950" style={{ fontFamily: "'Noto Sans Ethiopic','Inter',system-ui,sans-serif" }}>
      <style>{"@import url('https://fonts.googleapis.com/css2?family=Noto+Sans+Ethiopic:wght@400;600;800&family=Inter:wght@400;600;800&display=swap');"}</style>

      {/* Header / Navigation */}
      <header className="bg-slate-900/90 backdrop-blur border-b border-slate-800 sticky top-0 z-30">
        <div className="max-w-6xl mx-auto px-4 py-3.5 flex flex-wrap items-center gap-4">
          <button onClick={() => go("market")} className="text-2xl font-black tracking-tight text-amber-400 flex items-center gap-2 hover:opacity-90">
            <span className="bg-amber-400 text-slate-950 text-sm px-2 py-0.5 rounded font-extrabold">A+</span>
            {lang === "am" ? "አማላጅ ፕላስ" : "Amalaj Plus"}
          </button>
          
          <nav className="flex flex-wrap gap-1 flex-1 ml-2">
            {nav.map(([k, label]) => (
              <button key={k} onClick={() => ((k === "sell" || k === "deals" || k === "admin") && !me ? needLogin() : go(k))}
                className={"px-3.5 py-1.5 rounded-lg text-sm font-bold transition-all " + (view === k ? "bg-amber-400 text-slate-950 shadow-md shadow-amber-400/20" : "text-slate-300 hover:bg-slate-800 hover:text-white")}>
                {label}
              </button>
            ))}
          </nav>

          <button onClick={() => setLang(lang === "am" ? "en" : "am")} className="border border-slate-700 bg-slate-800/80 rounded-lg px-3 py-1.5 text-xs font-bold text-slate-300 hover:bg-slate-700 hover:text-white transition-all" aria-label="Switch language">
            {lang === "am" ? "EN 🇺🇸" : "አማ 🇪🇹"}
          </button>

          {me ? (
            <button onClick={() => { setToken(null); setMe(null); go("market"); }} className="text-xs font-bold text-slate-400 hover:text-rose-400 underline decoration-rose-500/50">{me.full_name} · {t.logout}</button>
          ) : (
            <button onClick={() => setShowAuth(true)} className={btnPrimary + " text-sm py-1.5 px-4"}>{t.login}</button>
          )}
        </div>
      </header>

      {/* Main Content Area */}
      <main className="max-w-6xl mx-auto px-4 py-8">
        {view === "market" && (selected
          ? <Detail id={selected} t={t} lang={lang} api={api} me={me} onBack={() => setSelected(null)} needLogin={needLogin} notify={notify} onDeal={() => go("deals")} />
          : <Market t={t} lang={lang} api={api} onOpen={setSelected} notify={notify} />)}
        {view === "sell" && <Sell t={t} api={api} notify={notify} onDone={() => go("market")} />}
        {view === "deals" && <Deals t={t} lang={lang} api={api} me={me} notify={notify} />}
        {view === "archive" && <Archive t={t} api={api} notify={notify} />}
        {view === "admin" && <Admin t={t} lang={lang} api={api} notify={notify} />}
      </main>

      {/* Auth Modal */}
      {showAuth && <Auth t={t} api={api} notify={notify} onClose={() => setShowAuth(false)}
        onAuth={(r) => { setToken(r.token); setMe(r.user); setShowAuth(false); }} />}

      {/* Toast Notification */}
      {toast && (
        <div role="status" className={"fixed bottom-6 left-1/2 -translate-x-1/2 px-5 py-3 rounded-xl font-bold shadow-2xl backdrop-blur z-50 transition-all border " + (toast.bad ? "bg-rose-950/90 text-rose-200 border-rose-800" : "bg-emerald-950/90 text-emerald-200 border-emerald-800")}>
          {toast.msg}
        </div>
      )}
    </div>
  );
}

/* ----------------------------------------------------------------------- Components */
function Field({ label, children }) {
  return <label className="block"><span className="block text-xs font-bold uppercase tracking-wider text-slate-400 mb-1.5">{label}</span>{children}</label>;
}
function Tag({ tag, t }) {
  return <span className={"text-xs font-bold px-2.5 py-1 rounded-md " + TAG_STYLE[tag]}>{t[tag]}</span>;
}
function Quality({ score, t }) {
  if (score == null) return null;
  return <span className="text-xs font-bold px-2.5 py-1 rounded-md bg-amber-400/10 text-amber-300 border border-amber-400/20">✓ {t.quality}: {score}/100</span>;
}

/* ----------------------------------------------------------------------- Auth Form */
function Auth({ t, api, notify, onAuth, onClose }) {
  const [mode, setMode] = useState("login");
  const [f, setF] = useState({ full_name: "", phone_number: "", email: "", password: "", telegram_id: "" });
  const [busy, setBusy] = useState(false);
  const set = (k) => (e) => setF({ ...f, [k]: e.target.value });
  const submit = async (e) => {
    e.preventDefault(); setBusy(true);
    try {
      const r = mode === "login"
        ? await api("/auth/login", { method: "POST", json: { identifier: f.phone_number || f.email, password: f.password } })
        : await api("/auth/register", { method: "POST", json: { full_name: f.full_name, phone_number: f.phone_number, password: f.password, email: f.email || null, telegram_id: f.telegram_id ? Number(f.telegram_id) : null } });
      onAuth(r);
    } catch (err) { notify(err.message, true); } finally { setBusy(false); }
  };
  return (
    <div className="fixed inset-0 bg-slate-950/80 backdrop-blur-sm flex items-center justify-center p-4 z-50" role="dialog" aria-modal="true">
      <form onSubmit={submit} className="bg-slate-900 rounded-2xl border border-slate-800 p-6 w-full max-w-sm space-y-4 shadow-2xl shadow-black">
        <div className="flex gap-2 p-1 bg-slate-950 rounded-xl border border-slate-800">
          {["login", "register"].map((m) => (
            <button type="button" key={m} onClick={() => setMode(m)} className={"flex-1 py-2 rounded-lg font-bold text-xs transition-all " + (mode === m ? "bg-amber-400 text-slate-950" : "text-slate-400 hover:text-white")}>
              {m === "login" ? t.login : t.register}
            </button>
          ))}
        </div>
        {mode === "register" && <Field label={t.fullName}><input className={inputCls} value={f.full_name} onChange={set("full_name")} required minLength={2} /></Field>}
        <Field label={t.phone}><input className={inputCls} value={f.phone_number} onChange={set("phone_number")} placeholder="09XXXXXXXX" required /></Field>
        {mode === "register" && <>
          <Field label={t.email}><input type="email" className={inputCls} value={f.email} onChange={set("email")} /></Field>
          <Field label={t.tgId}><input inputMode="numeric" className={inputCls} value={f.telegram_id} onChange={set("telegram_id")} /></Field>
        </>}
        <Field label={t.password}><input type="password" className={inputCls} value={f.password} onChange={set("password")} required minLength={8} /></Field>
        <div className="flex gap-2 pt-2">
          <button disabled={busy} className={btnPrimary + " flex-1 text-sm"}>{mode === "login" ? t.login : t.register}</button>
          <button type="button" onClick={onClose} className={btnGhost + " text-sm"}>{t.cancel}</button>
        </div>
      </form>
    </div>
  );
}

/* ----------------------------------------------------------------------- Marketplace */
function Market({ t, lang, api, onOpen, notify }) {
  const [platform, setPlatform] = useState("");
  const [q, setQ] = useState("");
  const [sort, setSort] = useState("new");
  const [rows, setRows] = useState(null);

  useEffect(() => {
    const p = new URLSearchParams({ sort });
    if (platform) p.set("platform", platform);
    if (q) p.set("q", q);
    const h = setTimeout(() => api("/listings?" + p).then(setRows).catch((e) => { setRows([]); notify(e.message, true); }), 250);
    return () => clearTimeout(h);
  }, [platform, q, sort, api]);

  return (
    <div className="space-y-6">
      {/* Hero Banner Section */}
      <section className="text-center py-10 px-4 bg-gradient-to-b from-slate-900 to-slate-950 rounded-2xl border border-slate-800/80 shadow-2xl relative overflow-hidden">
        <div className="absolute inset-0 bg-[radial-gradient(circle_at_top,_var(--tw-gradient-stops))] from-amber-400/5 via-transparent to-transparent"></div>
        <h1 className="text-3xl md:text-5xl font-black text-white mb-4 tracking-tight">
          ሶሻል ሚዲያ አካውንቶችን በአስተማማኝ ሁኔታ <span className="text-amber-400">ይግዙ እና ይሽጡ</span>
        </h1>
        <p className="text-slate-400 text-sm md:text-base max-w-2xl mx-auto mb-6">
          ገዢን እና ሻጭን በአደራ (Escrow) በማገናኘት ከማጭበርበር ነፃ የሆነ አስተማማኝ የንግድ ልውውጥ ያድርጉ።
        </p>
      </section>

      {/* Filter Tabs */}
      <div className="grid grid-cols-2 sm:grid-cols-4 lg:grid-cols-8 gap-2" role="tablist">
        {[["", t.all], ...PLATFORMS.map((p) => [p, PLABEL[p]])].map(([k, label]) => (
          <button key={k} role="tab" aria-selected={platform === k} onClick={() => setPlatform(k)}
            className={"py-2.5 px-3 rounded-xl text-xs font-bold transition-all border " + (platform === k ? "bg-amber-400 text-slate-950 border-amber-400 shadow-md shadow-amber-400/10" : "bg-slate-900 text-slate-300 border-slate-800 hover:bg-slate-800 hover:border-slate-700")}>
            {label}
          </button>
        ))}
      </div>

      {/* Search & Sort Controls */}
      <div className="flex gap-3">
        <input className={inputCls} placeholder="🔍 ይፈልጉ..." value={q} onChange={(e) => setQ(e.target.value)} aria-label="Search" />
        <select className={inputCls + " max-w-xs cursor-pointer"} value={sort} onChange={(e) => setSort(e.target.value)} aria-label="Sort">
          <option value="new">{lang === "am" ? "አዲስ" : "Newest"}</option>
          <option value="price_asc">{lang === "am" ? "ዋጋ ↑" : "Price low-high"}</option>
          <option value="price_desc">{lang === "am" ? "ዋጋ ↓" : "Price high-low"}</option>
          <option value="followers">{t.followers}</option>
        </select>
      </div>

      {/* Listing Cards Grid */}
      {rows === null ? <p className="text-center py-10 text-slate-500">በመጫን ላይ...</p> : rows.length === 0 ? <p className="py-16 text-center text-slate-500 font-semibold">{t.empty}</p> : (
        <div className="grid sm:grid-cols-2 lg:grid-cols-3 gap-5">
          {rows.map((l) => (
            <button key={l.id} onClick={() => onOpen(l.id)} className="text-left bg-slate-900/90 rounded-2xl border border-slate-800 p-5 hover:border-amber-400/50 hover:bg-slate-800/50 transition-all group focus:outline-none focus:ring-2 focus:ring-amber-400 shadow-lg">
              <div className="flex justify-between items-start gap-2 mb-3">
                <span className="text-xs font-extrabold bg-slate-800 text-amber-400 px-2.5 py-1 rounded-md border border-slate-700">{PLABEL[l.platform_type]}</span>
                <Tag tag={l.valuation_tag} t={t} />
              </div>
              <h3 className="font-black text-lg text-white mb-1 group-hover:text-amber-400 transition-colors leading-snug">{l.account_title}</h3>
              <p className="text-xs font-semibold text-slate-400 mb-4">{l.category}</p>
              
              <div className="grid grid-cols-2 gap-2 bg-slate-950/60 p-3 rounded-xl border border-slate-800/80 mb-4 text-xs">
                <div><span className="text-slate-500 block">{t.followers}</span><b className="text-slate-200 text-sm font-bold">{fmtK(l.followers_subscribers_count)}</b></div>
                <div><span className="text-slate-500 block">{t.revenue}</span><b className="text-slate-200 text-sm font-bold">{etb(l.monthly_revenue_etb)}</b></div>
              </div>

              <div className="flex justify-between items-end pt-1">
                <div>
                  <span className="text-[10px] uppercase tracking-wider text-slate-500 block">{t.price}</span>
                  <p className="text-xl font-black text-amber-400">{etb(l.asking_price_etb)}</p>
                </div>
                <Quality score={l.quality_score} t={t} />
              </div>
            </button>
          ))}
        </div>
      )}
    </div>
  );
}

/* ----------------------------------------------------------------------- Detail View */
function Detail({ id, t, lang, api, me, onBack, needLogin, notify, onDeal }) {
  const [l, setL] = useState(null);
  const [open, setOpen] = useState(false);
  const [amount, setAmount] = useState("");
  const [days, setDays] = useState("");

  useEffect(() => { api("/listings/" + id).then((d) => { setL(d); setAmount(String(d.asking_price_etb)); }).catch((e) => notify(e.message, true)); }, [id]);
  if (!l) return <p className="text-center py-10 text-slate-500">በመጫን ላይ...</p>;

  const amt = Number(amount) || 0;
  const fee = Math.round(amt * 2) / 100;
  const start = async (e) => {
    e.preventDefault();
    try {
      await api("/escrow", { method: "POST", json: { listing_id: l.id, agreed_amount_etb: amt, cooldown_days: days ? Number(days) : null } });
      notify("✓ የስምምነት ጥያቄ ተልኳል"); onDeal();
    } catch (err) { notify(err.message, true); }
  };

  return (
    <div className="space-y-6">
      <button onClick={onBack} className="text-sm font-bold text-amber-400 hover:underline">← {t.back}</button>
      
      <div className="grid md:grid-cols-5 gap-6">
        <div className="md:col-span-3 space-y-5 bg-slate-900 border border-slate-800 rounded-2xl p-6">
          <div className="flex flex-wrap gap-2 items-center">
            <span className="text-xs font-bold bg-slate-800 text-amber-400 px-2.5 py-1 rounded-md">{PLABEL[l.platform_type]}</span>
            <Tag tag={l.valuation_tag} t={t} />
            <Quality score={l.quality_score} t={t} />
            {l.status === "Sold" && <span className="text-xs font-bold px-2.5 py-1 rounded-md bg-rose-950 text-rose-300 border border-rose-800">{t.sold}</span>}
          </div>

          <h1 className="text-2xl md:text-3xl font-black text-white">{l.account_title}</h1>

          <div className="grid grid-cols-2 sm:grid-cols-4 gap-3">
            {[[t.followers, fmtK(l.followers_subscribers_count)], [t.engagement, l.engagement_rate != null ? l.engagement_rate + "%" : "-"], [t.category, l.category], [t.revenue, etb(l.monthly_revenue_etb)]].map(([k, v]) => (
              <div key={k} className="bg-slate-950 border border-slate-800 rounded-xl p-3">
                <dt className="text-[10px] uppercase font-bold text-slate-500">{k}</dt>
                <dd className="font-black text-slate-200 mt-1">{v}</dd>
              </div>
            ))}
          </div>

          <p className="whitespace-pre-wrap text-slate-300 text-sm leading-relaxed">{l.description}</p>

          {l.proof_image_url && (
            <figure className="pt-2">
              <figcaption className="text-xs font-bold uppercase tracking-wider text-slate-400 mb-2">{t.proof}</figcaption>
              <img src={API + l.proof_image_url} alt={t.proof} className="w-full rounded-xl border border-slate-800 shadow-xl" />
            </figure>
          )}
        </div>

        <aside className="md:col-span-2">
          <div className="bg-slate-900 border border-slate-800 rounded-2xl p-6 sticky top-20 shadow-2xl space-y-4">
            <div>
              <p className="text-xs font-bold uppercase tracking-wider text-slate-500">{t.price}</p>
              <p className="text-3xl font-black text-amber-400 mt-1">{etb(l.asking_price_etb)}</p>
            </div>

            {l.status === "Active" && !open && (
              <button className={btnPrimary + " w-full py-3 text-base"} onClick={() => (me ? setOpen(true) : needLogin())}>
                {t.startEscrow}
              </button>
            )}

            {open && (
              <form onSubmit={start} className="space-y-4 pt-2 border-t border-slate-800">
                <Field label={t.agreed}><input type="number" min="1" step="0.01" className={inputCls} value={amount} onChange={(e) => setAmount(e.target.value)} required /></Field>
                <Field label={t.cooldown}>
                  <select className={inputCls} value={days} onChange={(e) => setDays(e.target.value)}>
                    <option value="">{lang === "am" ? "ነባሪ" : "Default"}</option>
                    {[3, 4, 5, 6, 7].map((d) => <option key={d} value={d}>{d}</option>)}
                  </select>
                </Field>
                <div className="text-xs bg-slate-950 border border-slate-800 rounded-xl p-3 space-y-2">
                  <div className="flex justify-between text-slate-400"><span>{t.fee}</span><b className="text-slate-200">{etb(fee)}</b></div>
                  <div className="flex justify-between text-slate-400"><span>{t.payout}</span><b className="text-amber-400 font-bold">{etb(amt - fee)}</b></div>
                </div>
                <p className="text-[11px] text-rose-400/80 leading-tight">{t.offPlatform}</p>
                <div className="flex gap-2">
                  <button className={btnPrimary + " flex-1 text-sm py-2"}>{t.startEscrow}</button>
                  <button type="button" onClick={() => setOpen(false)} className={btnGhost + " text-sm py-2"}>{t.cancel}</button>
                </div>
              </form>
            )}
          </div>
        </aside>
      </div>
    </div>
  );
}

/* ----------------------------------------------------------------------- Sell Form */
function Sell({ t, api, notify, onDone }) {
  const blank = { platform_type: "Telegram", account_title: "", category: "", followers_subscribers_count: "", monthly_revenue_etb: "0", asking_price_etb: "", description: "", handle: "" };
  const [f, setF] = useState(blank);
  const [file, setFile] = useState(null);
  const [busy, setBusy] = useState(false);

  const set = (k) => (e) => setF({ ...f, [k]: e.target.value });
  const submit = async (e) => {
    e.preventDefault();
    if (!file) return notify(t.proof, true);
    setBusy(true);
    const fd = new FormData();
    Object.entries(f).forEach(([k, v]) => v !== "" && fd.append(k, v));
    fd.append("proof_image", file);
    try { await api("/listings", { method: "POST", form: fd }); notify(t.saved); onDone(); }
    catch (err) { notify(err.message, true); } finally { setBusy(false); }
  };

  return (
    <form onSubmit={submit} className="max-w-2xl mx-auto bg-slate-900 border border-slate-800 rounded-2xl p-6 md:p-8 space-y-5 shadow-2xl">
      <h1 className="text-2xl font-black text-white">{t.sell}</h1>
      <p className="text-xs text-slate-400 leading-relaxed">{t.sellerNote}</p>
      
      <Field label="Platform"><select className={inputCls} value={f.platform_type} onChange={set("platform_type")}>{PLATFORMS.map((p) => <option key={p} value={p}>{PLABEL[p]}</option>)}</select></Field>
      <Field label={t.title}><input className={inputCls} value={f.account_title} onChange={set("account_title")} required minLength={3} /></Field>
      
      <div className="grid sm:grid-cols-2 gap-4">
        <Field label={t.category}><input className={inputCls} value={f.category} onChange={set("category")} required /></Field>
        <Field label={t.followers}><input type="number" min="0" className={inputCls} value={f.followers_subscribers_count} onChange={set("followers_subscribers_count")} required /></Field>
        <Field label={t.revenue + " (ETB)"}><input type="number" min="0" className={inputCls} value={f.monthly_revenue_etb} onChange={set("monthly_revenue_etb")} /></Field>
        <Field label={t.price + " (ETB)"}><input type="number" min="1" className={inputCls} value={f.asking_price_etb} onChange={set("asking_price_etb")} required /></Field>
      </div>

      <Field label={t.handle}><input className={inputCls} value={f.handle} onChange={set("handle")} /></Field>
      <Field label={t.description}><textarea rows={4} className={inputCls} value={f.description} onChange={set("description")} /></Field>
      <Field label={t.proof}><input type="file" accept="image/png,image/jpeg,image/webp" onChange={(e) => setFile(e.target.files[0] || null)} className="block w-full text-xs text-slate-400 file:mr-4 file:py-2 file:px-4 file:rounded-lg file:border-0 file:text-xs file:font-bold file:bg-slate-800 file:text-amber-400 hover:file:bg-slate-700 cursor-pointer" required /></Field>

      <button disabled={busy} className={btnPrimary + " w-full py-3 text-base"}>{t.submit}</button>
    </form>
  );
}

/* ----------------------------------------------------------------------- Deals & Chat */
function timeLeft(iso) {
  const ms = new Date(iso + "Z") - Date.now();
  if (ms <= 0) return "0h";
  const d = Math.floor(ms / 864e5), h = Math.floor((ms % 864e5) / 36e5);
  return d ? `${d}d ${h}h` : `${h}h`;
}

function Deals({ t, lang, api, me, notify }) {
  const [rows, setRows] = useState(null);
  const [chat, setChat] = useState(null);

  const load = useCallback(() => api("/escrow").then(setRows).catch((e) => { setRows([]); notify(e.message, true); }), [api]);
  useEffect(() => { load(); }, [load]);

  const act = async (id, action, json) => {
    try { await api(`/escrow/${id}/${action}`, { method: "POST", json }); load(); }
    catch (e) { notify(e.message, true); }
  };
  const dispute = (id) => { const reason = window.prompt(t.reason); if (reason) act(id, "dispute", { reason }); };

  if (rows === null) return <p className="text-center py-10 text-slate-500">በመጫን ላይ...</p>;
  if (!rows.length) return <p className="py-16 text-center text-slate-500 font-semibold">{t.noDeals}</p>;

  return (
    <div className="space-y-4">
      {rows.map((d) => {
        const buyer = d.buyer_id === me.id, seller = d.seller_id === me.id;
        const live = ["Secured_in_Escrow", "Credentials_Transferred", "Buyer_Verification_Period"].includes(d.status);
        return (
          <div key={d.id} className="bg-slate-900 border border-slate-800 rounded-2xl p-5 space-y-3 shadow-xl">
            <div className="flex flex-wrap justify-between gap-2 items-center">
              <h3 className="font-black text-lg text-white">#{d.id} · {d.listing_title}</h3>
              <span className="text-xs font-bold bg-amber-400/10 text-amber-300 border border-amber-400/20 px-3 py-1 rounded-full">{STATUS[lang][d.status]}</span>
            </div>
            
            <p className="text-xs text-slate-400">
              {buyer ? (lang === "am" ? "ገዢ" : "Buyer") : (lang === "am" ? "ሻጭ" : "Seller")} · <b className="text-white">{etb(d.agreed_amount_etb)}</b> · {t.fee}: {etb(d.commission_fee_etb)} · {t.payout}: {etb(d.seller_payout_etb)}
            </p>

            {d.status === "Pending_Deposit" && buyer && <p className="text-xs bg-slate-950 border border-slate-800 rounded-xl p-3 text-amber-300">{t.payRef}: <b>{d.payment_reference}</b></p>}
            {d.status === "Buyer_Verification_Period" && <p className="text-xs font-bold text-amber-400">⏳ {timeLeft(d.cooldown_ends_at)} {t.holdLeft}</p>}
            {d.dispute_reason && <p className="text-xs text-rose-400 bg-rose-950/50 border border-rose-800 p-2.5 rounded-xl">⚠ {d.dispute_reason}</p>}
            {d.resolution_note && <p className="text-xs text-emerald-400 bg-emerald-950/50 border border-emerald-800 p-2.5 rounded-xl">✔ {d.resolution_note}</p>}

            <div className="flex flex-wrap gap-2 pt-2">
              {me.is_admin && d.status === "Pending_Deposit" && <button className={btnPrimary + " text-xs"} onClick={() => act(d.id, "confirm-deposit")}>{t.confirmDeposit}</button>}
              {seller && d.status === "Secured_in_Escrow" && <button className={btnPrimary + " text-xs"} onClick={() => act(d.id, "credentials-transferred")}>{t.transferred}</button>}
              {buyer && d.status === "Credentials_Transferred" && <button className={btnPrimary + " text-xs"} onClick={() => act(d.id, "confirm-access")}>{t.confirmAccess}</button>}
              {live && <button className={btnGhost + " text-xs border-rose-900/50 hover:bg-rose-950/50 text-rose-300"} onClick={() => dispute(d.id)}>{t.dispute}</button>}
              <button className={btnGhost + " text-xs"} onClick={() => setChat(chat === d.id ? null : d.id)}>{t.chat}</button>
            </div>

            {chat === d.id && <Chat id={d.id} me={me} t={t} api={api} notify={notify} />}
          </div>
        );
      })}
    </div>
  );
}

function Chat({ id, me, t, api, notify }) {
  const [msgs, setMsgs] = useState([]);
  const [body, setBody] = useState("");

  const load = useCallback(() => api(`/escrow/${id}/messages`).then(setMsgs).catch(() => {}), [api, id]);
  useEffect(() => { load(); const h = setInterval(load, 8000); return () => clearInterval(h); }, [load]);

  const send = async (e) => {
    e.preventDefault();
    try {
      const r = await api(`/escrow/${id}/messages`, { method: "POST", json: { body } });
      if (r.warning) notify(r.warning, true);
      setBody(""); load();
    } catch (err) { notify(err.message, true); }
  };

  return (
    <div className="mt-4 border-t border-slate-800 pt-4 space-y-3">
      <div className="max-h-56 overflow-y-auto space-y-2 pr-1">
        {msgs.map((m) => (
          <div key={m.id} className={"text-xs px-3.5 py-2 rounded-xl max-w-md " + (m.sender_id === me.id ? "ml-auto bg-amber-400 text-slate-950 font-semibold" : "bg-slate-950 text-slate-200 border border-slate-800") + (m.flagged ? " ring-2 ring-rose-500" : "")}>{m.body}</div>
        ))}
      </div>
      <form onSubmit={send} className="flex gap-2">
        <input className={inputCls + " text-xs py-2"} value={body} onChange={(e) => setBody(e.target.value)} required maxLength={2000} />
        <button className={btnPrimary + " text-xs py-2 px-4"}>{t.send}</button>
      </form>
    </div>
  );
}

/* ----------------------------------------------------------------------- Archive & Admin */
function Archive({ t, api, notify }) {
  const [rows, setRows] = useState(null);
  useEffect(() => { api("/archive").then(setRows).catch((e) => { setRows([]); notify(e.message, true); }); }, [api]);
  if (rows === null) return <p className="text-center py-10 text-slate-500">በመጫን ላይ...</p>;
  if (!rows.length) return <p className="py-16 text-center text-slate-500 font-semibold">{t.noArchive}</p>;

  return (
    <div className="grid sm:grid-cols-2 lg:grid-cols-3 gap-5">
      {rows.map((r, i) => (
        <div key={i} className="bg-slate-900 border border-slate-800 rounded-2xl p-5 shadow-xl">
          <div className="flex justify-between mb-2"><span className="text-xs font-bold bg-slate-800 text-amber-400 px-2 py-0.5 rounded">{PLABEL[r.platform_type]}</span><span className="text-xs text-slate-500">{r.completed_on}</span></div>
          <p className="font-black text-white tracking-wide">{r.masked_title}</p>
          <p className="text-xs text-slate-400 mt-1">{r.category} · {r.followers_bucket}</p>
          <p className="mt-3 text-lg font-black text-amber-400">{etb(r.sold_price_etb)}</p>
        </div>
      ))}
    </div>
  );
}

function Admin({ t, lang, api, notify }) {
  const [pending, setPending] = useState([]);
  const [disputes, setDisputes] = useState([]);
  const [deposits, setDeposits] = useState([]);

  const load = useCallback(() => {
    api("/admin/deposits").then(setDeposits).catch((e) => notify(e.message, true));
    api("/admin/listings").then(setPending).catch((e) => notify(e.message, true));
    api("/admin/disputes").then(setDisputes).catch((e) => notify(e.message, true));
  }, [api]);
  useEffect(() => { load(); }, [load]);

  const listingAct = async (id, a) => { try { await api(`/admin/listings/${id}/${a}`, { method: "POST" }); load(); } catch (e) { notify(e.message, true); } };
  const confirmDeposit = async (id) => { try { await api(`/escrow/${id}/confirm-deposit`, { method: "POST" }); load(); } catch (e) { notify(e.message, true); } };

  return (
    <div className="grid lg:grid-cols-2 gap-6">
      <section className="lg:col-span-2 bg-slate-900 border border-slate-800 rounded-2xl p-6 shadow-xl">
        <h2 className="text-xl font-black text-white mb-4">{t.confirmDeposit} ({deposits.length})</h2>
        <div className="grid sm:grid-cols-2 gap-3">
          {deposits.map((d) => (
            <div key={d.id} className="bg-slate-950 border border-slate-800 rounded-xl p-4">
              <p className="font-bold text-white text-sm">#{d.id} · {d.listing_title} · <span className="text-amber-400">{etb(d.agreed_amount_etb)}</span></p>
              <p className="text-xs text-slate-400 mt-1">{d.payment_reference}</p>
              <button className={btnPrimary + " mt-3 text-xs py-1.5"} onClick={() => confirmDeposit(d.id)}>{t.confirmDeposit}</button>
            </div>
          ))}
        </div>
      </section>

      <section className="bg-slate-900 border border-slate-800 rounded-2xl p-6 shadow-xl">
        <h2 className="text-xl font-black text-white mb-4">{t.review} ({pending.length})</h2>
        <div className="space-y-3">
          {pending.map((l) => (
            <div key={l.id} className="bg-slate-950 border border-slate-800 rounded-xl p-4 space-y-2">
              <p className="font-bold text-white text-sm">{l.account_title} <span className="text-xs font-normal text-slate-400">· {PLABEL[l.platform_type]} · {fmtK(l.followers_subscribers_count)} · {etb(l.asking_price_etb)}</span></p>
              {l.handle && <p className="text-xs text-slate-400">{l.handle}</p>}
              {l.proof_image_url && <a className="text-xs text-amber-400 underline block" href={API + l.proof_image_url} target="_blank" rel="noreferrer">{t.proof}</a>}
              <div className="flex gap-2 pt-1">
                <button className={btnPrimary + " text-xs py-1.5 px-3"} onClick={() => listingAct(l.id, "approve")}>{t.approve}</button>
                <button className={btnGhost + " text-xs py-1.5 px-3"} onClick={() => listingAct(l.id, "suspend")}>{t.suspend}</button>
              </div>
            </div>
          ))}
        </div>
      </section>
    </div>
  );
}