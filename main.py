from typing import List
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles

app = FastAPI(title="Amalaj Plus API", version="17.0")

app.mount("/static", StaticFiles(directory="static"), name="static")

DB_MARKETPLACE_LISTINGS = [
    {"id": 1, "title": "Crypto Hub", "platform": "Telegram", "subscribers": "12K", "views": "45K", "price": "15,000 ETB"},
    {"id": 2, "title": "Sportsphere", "platform": "YouTube", "subscribers": "303K", "views": "14M", "price": "78,000 ETB"}
]

@app.get("/api/v1/marketplace", response_model=List[dict])
def get_marketplace_listings():
    return DB_MARKETPLACE_LISTINGS

# ማንኛውንም ሌላ ራውት ሲጠይቅ በቀጥታ ዋናውን ገጽ እንዲመልስ (Render 404 ስህተትን ይከላከላል)
@app.get("/{full_path:path}", response_class=HTMLResponse)
def catch_all(full_path: str):
    return """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Amalaj Plus - Secured Digital Ecosystem</title>
        <script src="https://cdn.tailwindcss.com"></script>
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    </head>
    <body class="bg-[#0b132b] text-slate-100 min-h-screen font-sans">
        <nav class="bg-[#16203a]/90 border-b border-slate-700/60 sticky top-0 z-50 px-6 py-4 flex justify-between items-center max-w-7xl mx-auto">
            <span class="text-xl font-black text-white">Amalaj<span class="text-amber-400">Plus</span></span>
            <div class="flex space-x-6 text-xs font-semibold">
                <a href="/" class="text-amber-400">Home</a>
                <span class="text-emerald-400">🛡️ Escrow & National ID Active</span>
            </div>
        </nav>
        <main class="max-w-7xl mx-auto px-6 py-16 text-center space-y-6">
            <div class="inline-block px-4 py-1.5 bg-amber-500/10 text-amber-400 border border-amber-500/20 rounded-full text-xs font-bold">
                ⚡ Secured Digital Asset & Tool Rental Ecosystem
            </div>
            <h1 class="text-3xl md:text-4xl font-black text-white tracking-tight">
                Trade Digital Channels with <span class="text-amber-400">National ID Protection</span>
            </h1>
            <p class="text-slate-400 text-xs max-w-xl mx-auto">
                First-time sellers must provide high-quality National ID (Fayida) verification to prevent fraud and ensure 100% secure transactions.
            </p>
        </main>
    </body>
    </html>
    """