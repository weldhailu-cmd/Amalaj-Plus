from typing import List
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles

app = FastAPI(title="Amalaj Plus API", version="15.0")

app.mount("/static", StaticFiles(directory="static"), name="static")

DB_MARKETPLACE_LISTINGS = [
    {"id": 1, "title": "Crypto Hub", "platform": "Telegram", "subscribers": "12K", "views": "45K", "price": "15,000 ETB"},
    {"id": 2, "title": "Sportsphere", "platform": "YouTube", "subscribers": "303K", "views": "14M", "price": "78,000 ETB"},
    {"id": 3, "title": "Habesha Trends", "platform": "TikTok", "subscribers": "45K", "views": "1.2M", "price": "6,500 ETB"},
    {"id": 4, "title": "thela.stone291", "platform": "Instagram", "subscribers": "1.1K", "views": "1 Avg", "price": "910 ETB"},
    {"id": 5, "title": "Osama Jami", "platform": "Facebook", "subscribers": "5.1K", "views": "12 Likes", "price": "1,950 ETB"}
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
        <title>Amalaj Plus</title>
        <script src="https://cdn.tailwindcss.com"></script>
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    </head>
    <body class="bg-[#0b132b] text-slate-100 min-h-screen font-sans">
        <nav class="bg-[#16203a]/90 border-b border-slate-700/60 sticky top-0 z-50 px-6 py-4 flex justify-between items-center max-w-7xl mx-auto">
            <span class="text-xl font-black text-white">Amalaj<span class="text-amber-400">Plus</span></span>
            <div class="flex space-x-6 text-xs font-semibold">
                <a href="/" class="text-amber-400">Home</a>
                <a href="#marketplace" class="text-slate-300">Marketplace</a>
                <a href="#toolRentals" class="text-slate-300">Tool Rentals</a>
            </div>
        </nav>
        <main class="max-w-7xl mx-auto px-6 py-12 text-center">
            <h1 class="text-3xl font-black text-white">Secured Digital Asset & Tool Rental Ecosystem</h1>
            <p class="text-slate-400 mt-2 text-xs">Trade Channels & Rent Repair Tools with Escrow Protection</p>
        </main>
    </body>
    </html>
    """