from typing import List
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
import os

app = FastAPI(title="Amalaj Plus API", version="20.0")

# Mount static files if directory exists
if os.path.exists("static"):
    app.mount("/static", StaticFiles(directory="static"), name="static")

# Mock Database for Marketplace and Tools
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

@app.get("/", response_class=HTMLResponse)
def read_root():
    # frontend ፎልደር ውስጥ ያለውን index.html አንብቦ ይመልሳል
    html_path = "frontend/index.html"
    if os.path.exists(html_path):
        with open(html_path, "r", encoding="utf-8") as f:
            return f.read()
    return "<h3>Amalaj Plus Backend Running. Please place index.html inside frontend folder.</h3>"