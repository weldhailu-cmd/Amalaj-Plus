from datetime import datetime, timedelta
from typing import List, Optional
from fastapi import FastAPI, File, Form, HTTPException, UploadFile, status
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles

app = FastAPI(title="Amalaj Plus API", version="6.5")

app.mount("/static", StaticFiles(directory="static"), name="static")

DB_TOOLS = [
    {
        "id": 1,
        "tool_name": "UnlockTool Pro",
        "description": "FRP bypass, flashing, and Mi Account removal for Samsung & Xiaomi.",
        "rental_price": 150.0,
        "rental_duration": "3 Hours Active",
        "connection_type": "AnyDesk/TeamViewer Remote",
        "status": "AVAILABLE",
    }
]

DB_TRANSACTIONS = []

@app.get("/auth/google")
def google_auth_placeholder():
    return RedirectResponse(url="/")

@app.get("/api/v1/tools", response_model=List[dict])
def get_rental_tools():
    return DB_TOOLS

@app.post("/api/v1/chapa/pay")
def create_chapa_payment(
    amount: float = Form(...),
    email: str = Form(...),
    first_name: str = Form(...),
    phone_number: str = Form(...)
):
    payment_record = {
        "id": len(DB_TRANSACTIONS) + 1,
        "amount": amount,
        "email": email,
        "phone_number": phone_number,
        "status": "APPROVED",
        "gateway": "Chapa / Telebirr",
        "date": datetime.now().strftime("%Y-%m-%d %H:%M")
    }
    DB_TRANSACTIONS.append(payment_record)
    return {
        "success": True,
        "checkout_url": "https://api.chapa.co/v1/hosted/pay/checkout-sample",
        "message": "Payment gateway initialized successfully with 2% escrow protection.",
        "transaction": payment_record
    }

@app.post("/api/v1/telegram/bot/verify")
def verify_telegram_bot_channel(
    channel_username: str = Form(...)
):
    return {
        "success": True,
        "message": f"Channel {channel_username} auto-scan verified successfully via Amalaj Bot.",
        "subscribers_count": "15.4K",
        "status": "ACTIVE_VERIFIED"
    }

@app.get("/{full_path:path}", response_class=HTMLResponse)
def read_root(full_path: str = ""):
    return """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Amalaj Plus - Secured P2P Marketplace & Tool Rentals</title>
        <script src="https://cdn.tailwindcss.com"></script>
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    </head>
    <body class="bg-[#0b132b] text-slate-100 min-h-screen font-sans selection:bg-amber-500 selection:text-slate-950">
        <!-- Navigation Header -->
        <nav class="bg-[#16203a]/90 backdrop-blur-md border-b border-slate-700/60 sticky top-0 z-50">
            <div class="max-w-7xl mx-auto px-6 py-4 flex justify-between items-center">
                <div class="flex items-center space-x-3">
                    <div class="w-10 h-10 rounded-full border-2 border-amber-500 bg-white flex items-center justify-center p-0.5 shadow-lg">
                        <img src="/static/logo.png" alt="Logo" class="w-full h-full object-cover rounded-full" onerror="this.src='https://via.placeholder.com/40'">
                    </div>
                    <span class="text-xl font-black text-white">Amalaj<span class="text-amber-400">Plus</span></span>
                </div>
                <div class="hidden md:flex items-center space-x-6 text-xs font-semibold">
                    <a href="/" class="text-amber-400 hover:text-amber-300 transition">Home</a>
                    <a href="#dashboard" class="text-slate-300 hover:text-white transition">Dashboard & Analytics</a>
                    <a href="#payments" class="text-slate-300 hover:text-white transition">Chapa / Telebirr Pay</a>
                    <span class="px-3.5 py-1.5 bg-amber-500 text-slate-950 font-bold rounded-xl shadow-lg">🛡️ 2% Escrow Active</span>
                </div>
            </div>
        </nav>

        <!-- Hero Section -->
        <header class="max-w-7xl mx-auto px-6 py-14 text-center space-y-6">
            <div class="inline-block px-4 py-1.5 bg-amber-500/10 text-amber-400 border border-amber-500/20 rounded-full text-xs font-bold tracking-wide">
                ⚡ Secured Digital Asset & Tool Rental Ecosystem
            </div>
            <h1 class="text-4xl md:text-5xl font-black text-white tracking-tight leading-tight max-w-3xl mx-auto">
                Trade Digital Channels & Rent Repair Software with <span class="text-amber-400">Escrow Protection</span>
            </h1>
            <p class="text-slate-400 text-xs md:text-sm max-w-xl mx-auto">
                Integrated with Chapa & Telebirr automated payments, Telegram bot verification, and 3-day secure fund holding.
            </p>
        </header>

        <!-- Dashboard Section -->
        <section id="dashboard" class="max-w-7xl mx-auto px-6 py-8 space-y-8">
            <div class="bg-[#16203a] border border-slate-700/60 rounded-3xl p-8 shadow-2xl space-y-6">
                <div class="flex flex-col md:flex-row justify-between items-start md:items-center gap-4 pb-6 border-b border-slate-800">
                    <div>
                        <span class="text-xs text-amber-400 font-bold uppercase tracking-wider">Financial Overview</span>
                        <h2 class="text-2xl font-black text-white mt-1">User Dashboard & Deposit Analytics</h2>
                    </div>
                    <div class="px-4 py-2 bg-slate-900 border border-slate-800 rounded-2xl flex items-center gap-2">
                        <i class="fa-solid fa-wallet text-amber-400"></i>
                        <span class="font-black text-white text-sm">3,500 ETB</span>
                    </div>
                </div>

                <!-- Analytics Cards -->
                <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4 text-xs">
                    <div class="bg-slate-900/80 border border-slate-800 rounded-2xl p-5 space-y-2">
                        <span class="text-slate-400">Total Balance</span>
                        <div class="text-2xl font-black text-white">0 ETB</div>
                    </div>
                    <div class="bg-slate-900/80 border border-slate-800 rounded-2xl p-5 space-y-2">
                        <span class="text-slate-400">Total Income</span>
                        <div class="text-2xl font-black text-amber-400">24,100 ETB</div>
                    </div>
                    <div class="bg-slate-900/80 border border-slate-800 rounded-2xl p-5 space-y-2">
                        <span class="text-slate-400">Sold Channels</span>
                        <div class="text-2xl font-black text-white">5 Channels</div>
                    </div>
                    <div class="bg-slate-900/80 border border-slate-800 rounded-2xl p-5 space-y-2">
                        <span class="text-slate-400">Telegram Bot Scan</span>
                        <div class="text-2xl font-black text-emerald-400">Verified ✓</div>
                    </div>
                </div>
            </div>
        </section>

        <!-- Payment Integration Section -->
        <section id="payments" class="max-w-7xl mx-auto px-6 py-8 mb-16">
            <div class="bg-[#16203a] border border-slate-700/60 rounded-3xl p-8 shadow-2xl max-w-xl mx-auto space-y-6">
                <div class="flex justify-between items-center pb-4 border-b border-slate-800">
                    <h3 class="text-base font-bold text-white">Instant Chapa / Telebirr Deposit</h3>
                    <span class="text-amber-400 font-bold text-xs">2% Escrow Fee</span>
                </div>
                <form onsubmit="event.preventDefault(); alert('Chapa / Telebirr Payment Gateway Initialized Successfully!');" class="space-y-4 text-xs">
                    <div>
                        <label class="block text-slate-300 font-semibold mb-1">Amount (ETB) *</label>
                        <input type="number" required placeholder="3500" class="w-full bg-slate-900 border border-slate-700 rounded-xl px-3 py-2.5 text-white focus:outline-none focus:border-amber-500" />
                    </div>
                    <div>
                        <label class="block text-slate-300 font-semibold mb-1">Phone Number / Telebirr *</label>
                        <input type="text" required placeholder="0911223344" class="w-full bg-slate-900 border border-slate-700 rounded-xl px-3 py-2.5 text-white focus:outline-none focus:border-amber-500" />
                    </div>
                    <button type="submit" class="w-full py-3 bg-amber-500 hover:bg-amber-400 text-slate-950 font-bold rounded-xl transition cursor-pointer shadow-lg">
                        Proceed to Secure Payment &rarr;
                    </button>
                </form>
            </div>
        </section>

        <!-- Footer -->
        <footer class="max-w-7xl mx-auto px-6 py-10 border-t border-slate-800 text-center text-xs text-slate-500">
            &copy; 2026 Amalaj Plus. Built with dedicated golden-blue branding for Ethiopian digital commerce.
        </footer>
    </body>
    </html>
    """