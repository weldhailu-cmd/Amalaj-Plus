from datetime import datetime, timedelta
from typing import List, Optional
from fastapi import FastAPI, File, Form, HTTPException, UploadFile, status
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles

app = FastAPI(title="Amalaj Plus API", version="12.0")

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

        <!-- Marketplace Section -->
        <section id="marketplace" class="max-w-7xl mx-auto px-6 py-6 space-y-6">
            <div class="flex justify-between items-center bg-[#16203a] border border-slate-700/60 rounded-2xl p-6 shadow-xl">
                <div>
                    <span class="text-xs text-amber-400 font-bold uppercase tracking-wider">P2P Asset Trading</span>
                    <h2 class="text-xl font-black text-white mt-1">Browse Verified Marketplace Listings</h2>
                </div>
                <span class="px-3 py-1 bg-emerald-500/20 text-emerald-400 rounded-full text-xs font-bold">Protected by 2% Escrow</span>
            </div>

            <!-- Platform Category Selection Cards (All + 5 Platforms with dedicated Brand Colors) -->
            <div class="grid grid-cols-2 sm:grid-cols-3 lg:grid-cols-6 gap-4">
                <div class="bg-[#16203a] border-2 border-amber-500 rounded-2xl p-4 text-center space-y-2 cursor-pointer shadow-xl">
                    <div class="font-black text-white text-xs">All Platforms</div>
                    <span class="inline-block px-2 py-0.5 bg-amber-500 text-slate-950 text-[10px] font-bold rounded-full">Browse Listings</span>
                </div>
                <div class="bg-[#16203a] border border-blue-500 rounded-2xl p-4 text-center space-y-2 cursor-pointer shadow-xl">
                    <div class="font-black text-white text-xs">Telegram</div>
                    <span class="inline-block px-2 py-0.5 bg-blue-600 text-white text-[10px] font-bold rounded-full">Browse Listings</span>
                </div>
                <div class="bg-[#16203a] border border-red-500 rounded-2xl p-4 text-center space-y-2 cursor-pointer shadow-xl">
                    <div class="font-black text-white text-xs">YouTube</div>
                    <span class="inline-block px-2 py-0.5 bg-red-600 text-white text-[10px] font-bold rounded-full">Browse Listings</span>
                </div>
                <div class="bg-[#16203a] border border-pink-500 rounded-2xl p-4 text-center space-y-2 cursor-pointer shadow-xl">
                    <div class="font-black text-white text-xs">TikTok</div>
                    <span class="inline-block px-2 py-0.5 bg-pink-600 text-white text-[10px] font-bold rounded-full">Browse Listings</span>
                </div>
                <div class="bg-[#16203a] border border-purple-500 rounded-2xl p-4 text-center space-y-2 cursor-pointer shadow-xl">
                    <div class="font-black text-white text-xs">Instagram</div>
                    <span class="inline-block px-2 py-0.5 bg-purple-600 text-white text-[10px] font-bold rounded-full">Browse Listings</span>
                </div>
                <div class="bg-[#16203a] border border-blue-600 rounded-2xl p-4 text-center space-y-2 cursor-pointer shadow-xl">
                    <div class="font-black text-white text-xs">Facebook</div>
                    <span class="inline-block px-2 py-0.5 bg-blue-700 text-white text-[10px] font-bold rounded-full">Browse Listings</span>
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