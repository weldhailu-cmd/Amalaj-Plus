from datetime import datetime, timedelta
from typing import List, Optional
from fastapi import FastAPI, File, Form, HTTPException, UploadFile, status
from fastapi.responses import RedirectResponse
from fastapi.staticfiles import StaticFiles

app = FastAPI(title="Amalaj Plus API", version="4.0")

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