from datetime import datetime, timedelta
from typing import List, Optional
from fastapi import FastAPI, File, Form, HTTPException, UploadFile, status
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles

app = FastAPI(title="Amalaj Plus API", version="8.0")

app.mount("/static", StaticFiles(directory="static"), name="static")

DB_MARKETPLACE_LISTINGS = [
    {"id": 1, "title": "Sportsphere", "platform": "YouTube", "subscribers": "303K", "views": "14M", "price": "78,000 ETB", "status": "ACTIVE"},
    {"id": 2, "title": "NextGoal", "platform": "YouTube", "subscribers": "33K", "views": "3.3M", "price": "14,950 ETB", "status": "ACTIVE"},
    {"id": 3, "title": "thela.stone291", "platform": "Instagram", "subscribers": "1.1K", "views": "1 Avg Likes", "price": "910 ETB", "status": "ACTIVE"},
    {"id": 4, "title": "Osama Jami", "platform": "Facebook", "subscribers": "5.1K", "views": "12 Page Likes", "price": "1,950 ETB", "status": "ACTIVE"}
]

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

@app.get("/api/v1/marketplace", response_model=List[dict])
def get_marketplace_listings():
    return DB_MARKETPLACE_LISTINGS

@app.get("/api/v1/tools", response_model=List[dict])
def get_rental_tools():
    return DB_TOOLS

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
                    <a href="#marketplace" class="text-slate-300 hover:text-white transition">Marketplace</a>
                    <a href="#toolRentals" class="text-slate-300 hover:text-white transition">Tool Rentals</a>
                    <a href="#dashboard" class="text-slate-300 hover:text-white transition">Dashboard</a>
                    <span class="px-3.5 py-1.5 bg-amber-500 text-slate-950 font-bold rounded-xl shadow-lg">🛡️ 2% Escrow Active</span>
                </div>
            </div>
        </nav>

        <!-- Hero Section -->
        <header class="max-w-7xl mx-auto px-6 py-12 text-center space-y-4">
            <div class="inline-block px-4 py-1.5 bg-amber-500/10 text-amber-400 border border-amber-500/20 rounded-full text-xs font-bold">
                ⚡ Secured Digital Asset & Tool Rental Ecosystem
            </div>
            <h1 class="text-3xl md:text-4xl font-black text-white tracking-tight">
                Trade Digital Channels & Rent Repair Software with <span class="text-amber-400">Escrow Protection</span>
            </h1>
        </header>

        <!-- Marketplace Listings Section -->
        <section id="marketplace" class="max-w-7xl mx-auto px-6 py-6 space-y-6">
            <div class="flex justify-between items-center bg-[#16203a] border border-slate-700/60 rounded-2xl p-6 shadow-xl">
                <div>
                    <span class="text-xs text-amber-400 font-bold uppercase tracking-wider">P2P Asset Trading</span>
                    <h2 class="text-xl font-black text-white mt-1">Browse Verified Marketplace Listings</h2>
                </div>
                <span class="px-3 py-1 bg-emerald-500/20 text-emerald-400 rounded-full text-xs font-bold">Protected by 2% Escrow</span>
            </div>

            <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
                <!-- Listing 1 -->
                <div class="bg-[#16203a] border border-slate-700/60 rounded-3xl overflow-hidden shadow-2xl flex relative">
                    <div class="bg-red-600 w-10 flex items-center justify-center py-6 shrink-0">
                        <span class="text-white font-bold text-xs tracking-widest uppercase transform -rotate-90 whitespace-nowrap">YouTube</span>
                    </div>
                    <div class="p-5 flex-grow space-y-3 text-xs">
                        <div class="flex justify-between items-start">
                            <div>
                                <span class="px-2 py-0.5 bg-blue-600 text-white rounded text-[9px] font-bold">NEW</span>
                                <h3 class="font-bold text-white text-sm mt-1">Sportsphere</h3>
                            </div>
                        </div>
                        <div class="bg-slate-900/80 border border-slate-800 rounded-2xl p-2.5 flex justify-between text-[11px]">
                            <div><strong class="text-white">303K</strong><div class="text-slate-400 text-[9px]">Subscribers</div></div>
                            <div><strong class="text-white">14M</strong><div class="text-slate-400 text-[9px]">Views</div></div>
                        </div>
                        <div class="flex justify-between items-center pt-2 border-t border-slate-800">
                            <div><div class="text-[9px] text-slate-400 uppercase">Price</div><div class="text-base font-black text-white">78,000 ETB</div></div>
                            <button onclick="alert('Initiating Escrow Purchase for Sportsphere (78,000 ETB)')" class="px-3.5 py-2 bg-red-600 hover:bg-red-500 text-white font-bold rounded-xl cursor-pointer shadow">Buy</button>
                        </div>
                    </div>
                </div>

                <!-- Listing 2 -->
                <div class="bg-[#16203a] border border-slate-700/60 rounded-3xl overflow-hidden shadow-2xl flex relative">
                    <div class="bg-red-600 w-10 flex items-center justify-center py-6 shrink-0">
                        <span class="text-white font-bold text-xs tracking-widest uppercase transform -rotate-90 whitespace-nowrap">YouTube</span>
                    </div>
                    <div class="p-5 flex-grow space-y-3 text-xs">
                        <div class="flex justify-between items-start">
                            <div>
                                <span class="px-2 py-0.5 bg-blue-600 text-white rounded text-[9px] font-bold">NEW</span>
                                <h3 class="font-bold text-white text-sm mt-1">NextGoal</h3>
                            </div>
                        </div>
                        <div class="bg-slate-900/80 border border-slate-800 rounded-2xl p-2.5 flex justify-between text-[11px]">
                            <div><strong class="text-white">33K</strong><div class="text-slate-400 text-[9px]">Subscribers</div></div>
                            <div><strong class="text-white">3.3M</strong><div class="text-slate-400 text-[9px]">Views</div></div>
                        </div>
                        <div class="flex justify-between items-center pt-2 border-t border-slate-800">
                            <div><div class="text-[9px] text-slate-400 uppercase">Price</div><div class="text-base font-black text-white">14,950 ETB</div></div>
                            <button onclick="alert('Initiating Escrow Purchase for NextGoal (14,950 ETB)')" class="px-3.5 py-2 bg-red-600 hover:bg-red-500 text-white font-bold rounded-xl cursor-pointer shadow">Buy</button>
                        </div>
                    </div>
                </div>

                <!-- Listing 3 -->
                <div class="bg-[#16203a] border border-slate-700/60 rounded-3xl overflow-hidden shadow-2xl flex relative">
                    <div class="bg-gradient-to-b from-purple-600 via-pink-600 to-amber-500 w-10 flex items-center justify-center py-6 shrink-0">
                        <span class="text-white font-bold text-xs tracking-widest uppercase transform -rotate-90 whitespace-nowrap">Instagram</span>
                    </div>
                    <div class="p-5 flex-grow space-y-3 text-xs">
                        <div class="flex justify-between items-start">
                            <div>
                                <span class="px-2 py-0.5 bg-blue-600 text-white rounded text-[9px] font-bold">NEW</span>
                                <h3 class="font-bold text-white text-sm mt-1">thela.stone291</h3>
                            </div>
                        </div>
                        <div class="bg-slate-900/80 border border-slate-800 rounded-2xl p-2.5 flex justify-between text-[11px]">
                            <div><strong class="text-white">1.1K</strong><div class="text-slate-400 text-[9px]">Subscribers</div></div>
                            <div><strong class="text-white">1 Avg</strong><div class="text-slate-400 text-[9px]">Likes</div></div>
                        </div>
                        <div class="flex justify-between items-center pt-2 border-t border-slate-800">
                            <div><div class="text-[9px] text-slate-400 uppercase">Price</div><div class="text-base font-black text-white">910 ETB</div></div>
                            <button onclick="alert('Initiating Escrow Purchase for thela.stone291 (910 ETB)')" class="px-3.5 py-2 bg-red-600 hover:bg-red-500 text-white font-bold rounded-xl cursor-pointer shadow">Buy</button>
                        </div>
                    </div>
                </div>

                <!-- Listing 4 -->
                <div class="bg-[#16203a] border border-slate-700/60 rounded-3xl overflow-hidden shadow-2xl flex relative">
                    <div class="bg-blue-600 w-10 flex items-center justify-center py-6 shrink-0">
                        <span class="text-white font-bold text-xs tracking-widest uppercase transform -rotate-90 whitespace-nowrap">Facebook</span>
                    </div>
                    <div class="p-5 flex-grow space-y-3 text-xs">
                        <div class="flex justify-between items-start">
                            <div>
                                <span class="px-2 py-0.5 bg-blue-600 text-white rounded text-[9px] font-bold">NEW</span>
                                <h3 class="font-bold text-white text-sm mt-1">Osama Jami</h3>
                            </div>
                        </div>
                        <div class="bg-slate-900/80 border border-slate-800 rounded-2xl p-2.5 flex justify-between text-[11px]">
                            <div><strong class="text-white">5.1K</strong><div class="text-slate-400 text-[9px]">Subscribers</div></div>
                            <div><strong class="text-white">12 Likes</strong><div class="text-slate-400 text-[9px]">Pages</div></div>
                        </div>
                        <div class="flex justify-between items-center pt-2 border-t border-slate-800">
                            <div><div class="text-[9px] text-slate-400 uppercase">Price</div><div class="text-base font-black text-white">1,950 ETB</div></div>
                            <button onclick="alert('Initiating Escrow Purchase for Osama Jami (1,950 ETB)')" class="px-3.5 py-2 bg-red-600 hover:bg-red-500 text-white font-bold rounded-xl cursor-pointer shadow">Buy</button>
                        </div>
                    </div>
                </div>
            </div>
        </section>

        <!-- Tool Rentals Section -->
        <section id="toolRentals" class="max-w-7xl mx-auto px-6 py-6 space-y-6">
            <div class="flex justify-between items-center bg-[#16203a] border border-slate-700/60 rounded-2xl p-6 shadow-xl">
                <div>
                    <span class="text-xs text-amber-400 font-bold uppercase tracking-wider">For Technicians</span>
                    <h2 class="text-xl font-black text-white mt-1">Mobile Repair Software Tool Rentals ⚡</h2>
                </div>
                <span class="px-3 py-1 bg-blue-500/20 text-blue-400 rounded-full text-xs font-bold">AnyDesk Remote</span>
            </div>

            <div class="bg-[#16203a] border border-slate-700/60 rounded-2xl p-6 shadow-xl flex justify-between items-center text-xs">
                <div>
                    <h3 class="font-bold text-white text-base">UnlockTool Pro</h3>
                    <p class="text-slate-300 mt-1">FRP bypass, flashing, and Mi Account removal for Samsung & Xiaomi.</p>
                    <span class="text-amber-300 font-semibold mt-2 block"><i class="fa-solid fa-link"></i> AnyDesk/TeamViewer Remote</span>
                </div>
                <div class="text-right space-y-2">
                    <div class="text-base font-black text-emerald-400">150.0 ETB / 3 Hours</div>
                    <button onclick="alert('Opening UnlockTool Rental Modal...')" class="px-4 py-2 bg-amber-500 hover:bg-amber-400 text-slate-950 font-bold rounded-xl cursor-pointer shadow">
                        Rent Tool Now ⚡
                    </button>
                </div>
            </div>
        </section>

        <!-- Dashboard Analytics Section -->
        <section id="dashboard" class="max-w-7xl mx-auto px-6 py-6 mb-16 space-y-6">
            <div class="bg-[#16203a] border border-slate-700/60 rounded-3xl p-8 shadow-2xl space-y-6">
                <div class="flex justify-between items-center border-b border-slate-800 pb-4">
                    <div>
                        <span class="text-xs text-amber-400 font-bold uppercase tracking-wider">Overview</span>
                        <h2 class="text-xl font-black text-white mt-1">User Dashboard & Deposit Analytics</h2>
                    </div>
                    <div class="px-4 py-2 bg-slate-900 border border-slate-800 rounded-2xl flex items-center gap-2">
                        <i class="fa-solid fa-wallet text-amber-400"></i>
                        <span class="font-black text-white text-sm">3,500 ETB</span>
                    </div>
                </div>

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

        <!-- Footer -->
        <footer class="max-w-7xl mx-auto px-6 py-10 border-t border-slate-800 text-center text-xs text-slate-500">
            &copy; 2026 Amalaj Plus. Built with dedicated golden-blue branding for Ethiopian digital commerce.
        </footer>
    </body>
    </html>
    """