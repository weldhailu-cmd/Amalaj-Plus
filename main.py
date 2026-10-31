from typing import List
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

app = FastAPI(title="Amalaj Plus API", version="14.0")

app.mount("/static", StaticFiles(directory="static"), name="static")

DB_MARKETPLACE_LISTINGS = [
    {"id": 1, "title": "Telegram Channel - Crypto Hub", "platform": "Telegram", "subscribers": "12K", "views": "45K", "price": "15,000 ETB", "status": "ACTIVE"},
    {"id": 2, "title": "Sportsphere", "platform": "YouTube", "subscribers": "303K", "views": "14M", "price": "78,000 ETB", "status": "ACTIVE"},
    {"id": 3, "title": "Habesha Trends", "platform": "TikTok", "subscribers": "45K", "views": "1.2M", "price": "6,500 ETB", "status": "ACTIVE"},
    {"id": 4, "title": "thela.stone291", "platform": "Instagram", "subscribers": "1.1K", "views": "1 Avg Likes", "price": "910 ETB", "status": "ACTIVE"},
    {"id": 5, "title": "Osama Jami", "platform": "Facebook", "subscribers": "5.1K", "views": "12 Page Likes", "price": "1,950 ETB", "status": "ACTIVE"}
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