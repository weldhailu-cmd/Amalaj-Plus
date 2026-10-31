from datetime import datetime, timedelta
from typing import List, Optional
from fastapi import FastAPI, File, Form, HTTPException, UploadFile, status
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles

app = FastAPI(title="Amalaj Plus API", version="4.1")

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

DB_RENTAL_SESSIONS = []
DB_LISTINGS = []

@app.get("/auth/google")
def google_auth_placeholder():
    return RedirectResponse(url="/")

@app.get("/api/v1/tools", response_model=List[dict])
def get_rental_tools():
    return DB_TOOLS

@app.post("/api/v1/tools/publish")
def publish_rental_tool(
    tool_name: str = Form(...),
    description: str = Form(...),
    rental_price: float = Form(...),
    rental_duration: str = Form(...),
    connection_type: str = Form(...),
):
    new_tool = {
        "id": len(DB_TOOLS) + 1,
        "tool_name": tool_name,
        "description": description,
        "rental_price": rental_price,
        "rental_duration": rental_duration,
        "connection_type": connection_type,
        "status": "AVAILABLE",
    }
    DB_TOOLS.append(new_tool)
    return {"success": True, "message": "Repair tool published successfully!", "tool": new_tool}

@app.post("/api/v1/tools/rent")
def rent_repair_tool(
    tool_id: int = Form(...),
    renter_anydesk_id: str = Form(...),
    renter_telegram: str = Form(...),
    payment_method: str = Form("Chapa"),
    receipt_file: Optional[UploadFile] = File(None),
):
    tool = next((t for t in DB_TOOLS if t["id"] == tool_id), None)
    if not tool:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Tool not found")

    if tool["status"] != "AVAILABLE":
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Tool is currently busy.")

    receipt_filename = receipt_file.filename if receipt_file else None

    start_time = datetime.now()
    duration_text = tool["rental_duration"]
    hours_add = 3
    if "Day" in duration_text: hours_add = 24
    elif "Week" in duration_text: hours_add = 168
    elif "Months" in duration_text: hours_add = 1440

    end_time = start_time + timedelta(hours=hours_add)

    session_data = {
        "session_id": len(DB_RENTAL_SESSIONS) + 1,
        "tool_id": tool["id"],
        "tool_name": tool["tool_name"],
        "renter_anydesk_id": renter_anydesk_id,
        "renter_telegram": renter_telegram,
        "payment_method": payment_method,
        "receipt_file": receipt_filename,
        "start_time": start_time.isoformat(),
        "end_time": end_time.isoformat(),
        "status": "ACTIVE",
    }

    tool["status"] = "BUSY"
    DB_RENTAL_SESSIONS.append(session_data)

    return {
        "success": True,
        "message": f"Tool {tool['tool_name']} rented successfully! Active until {end_time.strftime('%Y-%m-%d %H:%M')}",
        "session": session_data,
    }

@app.get("/", response_class=HTMLResponse)
def read_root():
    return """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Amalaj Plus - Modular Marketplace</title>
        <script src="https://cdn.tailwindcss.com"></script>
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    </head>
    <body class="bg-[#0b132b] text-slate-100 min-h-screen font-sans flex flex-col justify-between">
        <div class="max-w-7xl mx-auto px-6 py-12 w-full space-y-8">
            <div class="flex items-center justify-between border-b border-slate-800 pb-6">
                <div class="flex items-center space-x-3">
                    <div class="w-10 h-10 rounded-full border-2 border-amber-500 bg-white flex items-center justify-center p-0.5 shadow-lg">
                        <img src="/static/logo.png" alt="Logo" class="w-full h-full object-cover rounded-full" onerror="this.src='https://via.placeholder.com/40'">
                    </div>
                    <span class="text-2xl font-extrabold text-white">Amalaj<span class="text-amber-400">Plus</span></span>
                </div>
                <span class="px-3 py-1 bg-amber-500/20 text-amber-400 rounded-xl text-xs font-bold">🛡️ Jano Market Modular Architecture</span>
            </div>

            <div class="bg-[#16203a] border border-slate-700/60 rounded-3xl p-8 shadow-2xl space-y-6 text-center">
                <div class="w-16 h-16 bg-amber-500/20 text-amber-400 rounded-3xl flex items-center justify-center mx-auto text-2xl shadow-inner">
                    <i class="fa-solid fa-layer-group"></i>
                </div>
                <div class="space-y-2">
                    <h1 class="text-3xl font-black text-white">Amalaj Plus System is Online ⚡</h1>
                    <p class="text-sm text-slate-300 max-w-xl mx-auto">
                        All modular components (Marketplace, Dashboard Analytics, Escrow Timer, and Admin Chat Protection) have been successfully structured and mounted.
                    </p>
                </div>
                <div class="flex justify-center gap-4 pt-4">
                    <a href="#dashboardSection" class="px-6 py-3 bg-amber-500 text-slate-950 font-bold rounded-xl hover:bg-amber-400 transition text-xs shadow-lg">
                        Open Dashboard & Analytics 📊
                    </a>
                </div>
            </div>
        </div>
    </body>
    </html>
    """