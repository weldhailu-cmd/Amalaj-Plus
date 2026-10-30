from datetime import datetime, timedelta
from typing import List, Optional
from fastapi import FastAPI, File, Form, HTTPException, UploadFile, status
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel

app = FastAPI(title="Amalaj Plus API", version="2.5")

app.mount("/static", StaticFiles(directory="static"), name="static")

# In-Memory Database Simulation
DB_TOOLS = [
    {
        "id": 1,
        "tool_name": "UnlockTool Pro",
        "description": "FRP bypass, flashing, and Mi Account removal for Samsung & Xiaomi.",
        "rental_price": 150.0,
        "rental_duration_hours": 3,
        "connection_type": "AnyDesk/TeamViewer Remote",
        "status": "AVAILABLE",
    },
    {
        "id": 2,
        "tool_name": "UMT Pro / Ultimate",
        "description": (
            "Advanced Qualcomm & MTK servicing, flashing, and network"
            " unlocking."
        ),
        "rental_price": 120.0,
        "rental_duration_hours": 3,
        "connection_type": "Direct Account Credentials",
        "status": "AVAILABLE",
    },
    {
        "id": 3,
        "tool_name": "Pandora Tool",
        "description": (
            "Powerful tool for MTK device operations, security backup &"
            " bootloader."
        ),
        "rental_price": 130.0,
        "rental_duration_hours": 3,
        "connection_type": "AnyDesk/TeamViewer Remote",
        "status": "AVAILABLE",
    },
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
    rental_duration_hours: int = Form(...),
    connection_type: str = Form(...),
):
  new_tool = {
      "id": len(DB_TOOLS) + 1,
      "tool_name": tool_name,
      "description": description,
      "rental_price": rental_price,
      "rental_duration_hours": rental_duration_hours,
      "connection_type": connection_type,
      "status": "AVAILABLE",
  }
  DB_TOOLS.append(new_tool)
  return {
      "success": True,
      "message": "Repair tool published successfully for rental!",
      "tool": new_tool,
  }


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
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, detail="Tool not found"
    )

  if tool["status"] != "AVAILABLE":
    raise HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST,
        detail="Tool is currently rented or busy by another user.",
    )

  receipt_filename = receipt_file.filename if receipt_file else None

  start_time = datetime.now()
  end_time = start_time + timedelta(hours=tool["rental_duration_hours"])

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
      "message": (
          f"Tool {tool['tool_name']} rented successfully! Session active until"
          f" {end_time.strftime('%H:%M:%S')}"
      ),
      "session": session_data,
  }


@app.get("/api/v1/admin/active-sessions")
def get_active_rental_sessions():
  current_time = datetime.now()
  for session in DB_RENTAL_SESSIONS:
    if session["status"] == "ACTIVE":
      if current_time >= datetime.fromisoformat(session["end_time"]):
        session["status"] = "EXPIRED"
        tool = next(
            (t for t in DB_TOOLS if t["id"] == session["tool_id"]), None
        )
        if tool:
          tool["status"] = "AVAILABLE"
  return {"current_server_time": current_time.isoformat(), "sessions": DB_RENTAL_SESSIONS}


@app.get("/", response_class=HTMLResponse)
def read_root():
  return """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Amalaj Plus - Digital Assets & Tool Rental Marketplace</title>
        <script src="https://cdn.tailwindcss.com"></script>
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    </head>
    <body class="bg-[#0b132b] text-slate-100 min-h-screen font-sans selection:bg-amber-500 selection:text-slate-950 flex flex-col justify-between">

        <div>
            <!-- Header / Navigation -->
            <header class="border-b border-slate-800 bg-[#0b132b]/95 backdrop-blur sticky top-0 z-50">
                <div class="max-w-7xl mx-auto px-6 py-4 flex justify-between items-center">
                    <div class="flex items-center space-x-3">
                        <div class="w-10 h-10 rounded-full border-2 border-amber-500 overflow-hidden shadow-lg shadow-amber-500/20 bg-white flex items-center justify-center p-0.5">
                            <img src="/static/logo.png" alt="Logo" class="w-full h-full object-cover rounded-full">
                        </div>
                        <span class="text-2xl font-extrabold text-white tracking-tight">Amalaj<span class="text-amber-400">Plus</span></span>
                    </div>

                    <!-- Properly Aligned Navigation Links & Action Buttons -->
                    <div class="hidden md:flex items-center space-x-6 text-sm font-medium text-slate-300">
                        <a href="#" class="hover:text-amber-400 transition py-2">Home</a>
                        <a href="#marketplace" class="hover:text-amber-400 transition py-2">Digital Marketplace</a>
                        <a href="#toolRentalSection" class="hover:text-amber-400 transition py-2">Tool Rental ⚡</a>
                        <a href="#dashboardSection" class="hover:text-amber-400 transition py-2">My Dashboard</a>
                        
                        <div class="flex items-center space-x-2 pl-2 border-l border-slate-800">
                            <button onclick="switchPostFormTab('asset')" class="bg-amber-500 hover:bg-amber-400 text-slate-950 font-bold px-4 py-2 rounded-xl transition shadow-lg shadow-amber-500/20 flex items-center gap-1.5 cursor-pointer text-xs">
                                <i class="fa-solid fa-plus-circle"></i>
                                <span>Post Asset</span>
                            </button>
                            <button onclick="switchPostFormTab('tool')" class="bg-slate-800 hover:bg-slate-700 text-amber-400 font-bold px-4 py-2 rounded-xl transition border border-slate-700 flex items-center gap-1.5 cursor-pointer text-xs">
                                <i class="fa-solid fa-screwdriver-wrench"></i>
                                <span>Rent Tool</span>
                            </button>
                        </div>
                    </div>

                    <div id="navUserActions" class="flex items-center space-x-3">
                        <button onclick="openAuthModal('signin')" class="flex items-center space-x-2 bg-slate-800 hover:bg-slate-700 text-white font-bold px-4 py-2 rounded-xl transition border border-slate-700 cursor-pointer text-xs">
                            <i class="fa-brands fa-google text-red-400"></i>
                            <span>Sign In</span>
                        </button>
                    </div>
                </div>
            </header>

            <!-- Hero Section with Universal Post Box -->
            <section class="max-w-7xl mx-auto px-6 py-12">
                <div class="grid lg:grid-cols-12 gap-12 items-start">
                    <div class="lg:col-span-7 space-y-6">
                        <div class="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-amber-500/10 border border-amber-500/30 text-amber-400 text-xs font-semibold">
                            <span>🛡️ Secure Escrow Protected Ethiopian Marketplace</span>
                        </div>
                        <h1 class="text-4xl md:text-5xl font-black tracking-tight text-white leading-tight">
                            Buy & Sell Digital Assets & <span class="text-amber-400">Rent Mobile Repair Tools</span> Securely.
                        </h1>
                        <p class="text-sm md:text-base text-slate-300 max-w-xl leading-relaxed">
                            Amalaj Plus is a trusted platform to buy and sell verified Telegram channels, TikTok accounts, YouTube channels, Instagram & Facebook pages with full screenshot verification and safe admin escrow protection.
                        </p>
                        <div class="flex items-center gap-3 p-3.5 bg-emerald-500/10 border border-emerald-500/30 rounded-2xl max-w-lg">
                            <div class="w-10 h-10 rounded-xl bg-emerald-500/20 text-emerald-400 flex items-center justify-center text-lg shrink-0">
                                <i class="fa-solid fa-shield-halved"></i>
                            </div>
                            <div class="text-xs">
                                <h5 class="font-bold text-emerald-400">Escrow Protected Transactions</h5>
                                <p class="text-slate-300 mt-0.5">Funds are securely held until asset transfer or tool session is fully verified.</p>
                            </div>
                        </div>
                    </div>

                    <!-- Single Centralized Universal Post Box -->
                    <div id="mainPostBoxContainer" class="lg:col-span-5">
                        <div class="bg-[#1c2541] border border-slate-700/60 rounded-3xl p-6 shadow-2xl space-y-4">
                            <div class="flex justify-between items-center pb-3 border-b border-slate-800">
                                <div class="flex space-x-2 bg-slate-900 p-1 rounded-xl border border-slate-800 text-xs font-bold">
                                    <button id="postTabAssetBtn" onclick="switchPostFormTab('asset')" class="px-3 py-1.5 rounded-lg bg-amber-500 text-slate-950 transition cursor-pointer">
                                        Post Asset
                                    </button>
                                    <button id="postTabToolBtn" onclick="switchPostFormTab('tool')" class="px-3 py-1.5 rounded-lg text-slate-400 hover:text-white transition cursor-pointer">
                                        Post Tool Rental
                                    </button>
                                </div>
                                <span class="text-amber-400 font-bold text-xs">Escrow Protected</span>
                            </div>

                            <!-- 1. Post Digital Asset Form -->
                            <form id="formPostAsset" onsubmit="handlePostListing(event)" class="space-y-3 text-xs">
                                <div>
                                    <label class="block text-slate-300 font-semibold mb-1">Asset Name / Title *</label>
                                    <input type="text" id="listingTitle" required placeholder="e.g., Habesha Tech Channel" class="w-full bg-slate-900 border border-slate-700 rounded-xl px-3 py-2 text-white focus:outline-none focus:border-amber-500">
                                </div>
                                <div>
                                    <label class="block text-slate-300 font-semibold mb-1">Channel / Page Link *</label>
                                    <input type="url" id="listingLink" required placeholder="https://t.me/your_channel" class="w-full bg-slate-900 border border-slate-700 rounded-xl px-3 py-2 text-white focus:outline-none focus:border-amber-500">
                                </div>
                                <div class="grid grid-cols-2 gap-2">
                                    <div>
                                        <label class="block text-slate-300 font-semibold mb-1">Platform *</label>
                                        <select id="listingPlatform" onchange="updateAssetTypes()" class="w-full bg-slate-900 border border-slate-700 rounded-xl px-2 py-2 text-white focus:outline-none focus:border-amber-500">
                                            <option value="Telegram">Telegram</option>
                                            <option value="TikTok">TikTok</option>
                                            <option value="YouTube">YouTube</option>
                                            <option value="Instagram">Instagram</option>
                                            <option value="Facebook">Facebook</option>
                                        </select>
                                    </div>
                                    <div>
                                        <label class="block text-slate-300 font-semibold mb-1">Asset Type *</label>
                                        <select id="listingAssetType" class="w-full bg-slate-900 border border-slate-700 rounded-xl px-2 py-2 text-white focus:outline-none focus:border-amber-500">
                                            <!-- Dynamically populated -->
                                        </select>
                                    </div>
                                </div>
                                <div>
                                    <label class="block text-slate-300 font-semibold mb-1">Category (Niche) *</label>
                                    <select id="listingNiche" class="w-full bg-slate-900 border border-slate-700 rounded-xl px-2 py-2 text-white focus:outline-none focus:border-amber-500">
                                        <option value="Entertainment">Entertainment & Music</option>
                                        <option value="Education">Education & Training</option>
                                        <option value="Technology">Technology & Software</option>
                                        <option value="Sport">Sport & Fitness</option>
                                        <option value="Business">Business & Finance</option>
                                    </select>
                                </div>
                                <div>
                                    <label class="block text-slate-300 font-semibold mb-1">Screenshot Proof *</label>
                                    <input type="file" id="listingProof" accept="image/*" required onchange="handleProofUpload(event)" class="w-full bg-slate-900 border border-slate-700 rounded-xl px-3 py-1.5 text-slate-400 text-[11px] cursor-pointer">
                                </div>
                                <div class="grid grid-cols-2 gap-2">
                                    <div>
                                        <label class="block text-slate-300 font-semibold mb-1">Subscribers / Views</label>
                                        <input type="text" id="listingSubCount" placeholder="Auto-filled via OCR" class="w-full bg-slate-900 border border-slate-700 rounded-xl px-3 py-2 text-white focus:outline-none focus:border-amber-500">
                                    </div>
                                    <div>
                                        <label class="block text-slate-300 font-semibold mb-1">Asking Price (ETB) *</label>
                                        <input type="number" id="listingPrice" required placeholder="5000" class="w-full bg-slate-900 border border-slate-700 rounded-xl px-3 py-2 text-white focus:outline-none focus:border-amber-500">
                                    </div>
                                </div>
                                <button type="submit" class="w-full py-2.5 bg-amber-500 text-slate-950 font-bold rounded-xl hover:bg-amber-400 transition cursor-pointer shadow-md">
                                    Publish Asset with Escrow Protection &rarr;
                                </button>
                            </form>

                            <!-- 2. Post Repair Tool Form -->
                            <form id="formPostTool" onsubmit="handlePostTool(event)" class="hidden space-y-3 text-xs">
                                <div>
                                    <label class="block text-slate-300 font-semibold mb-1">Tool Name *</label>
                                    <input type="text" id="toolNameInput" required placeholder="e.g., DFT Pro / Chimera Tool" class="w-full bg-slate-900 border border-slate-700 rounded-xl px-3 py-2 text-white focus:outline-none focus:border-amber-500">
                                </div>
                                <div>
                                    <label class="block text-slate-300 font-semibold mb-1">Tool Description / Supported Services *</label>
                                    <input type="text" id="toolDescInput" required placeholder="e.g., FRP Bypass, Flashing & Mi Account removal." class="w-full bg-slate-900 border border-slate-700 rounded-xl px-3 py-2 text-white focus:outline-none focus:border-amber-500">
                                </div>
                                <div class="grid grid-cols-2 gap-2">
                                    <div>
                                        <label class="block text-slate-300 font-semibold mb-1">Rental Price (ETB) *</label>
                                        <input type="number" id="toolPriceInput" required placeholder="150" class="w-full bg-slate-900 border border-slate-700 rounded-xl px-3 py-2 text-white focus:outline-none focus:border-amber-500">
                                    </div>
                                    <div>
                                        <label class="block text-slate-300 font-semibold mb-1">Duration (Hours) *</label>
                                        <input type="number" id="toolDurationInput" value="3" required class="w-full bg-slate-900 border border-slate-700 rounded-xl px-3 py-2 text-white focus:outline-none focus:border-amber-500">
                                    </div>
                                </div>
                                <div>
                                    <label class="block text-slate-300 font-semibold mb-1">Connection Type *</label>
                                    <select id="toolConnectionType" class="w-full bg-slate-900 border border-slate-700 rounded-xl px-2 py-2 text-white focus:outline-none focus:border-amber-500">
                                        <option value="AnyDesk/TeamViewer Remote">AnyDesk/TeamViewer Remote</option>
                                        <option value="Direct Account Credentials">Direct Account Credentials</option>
                                    </select>
                                </div>
                                <button type="submit" class="w-full py-2.5 bg-amber-500 text-slate-950 font-bold rounded-xl hover:bg-amber-400 transition cursor-pointer shadow-md">
                                    Publish Rental Tool &rarr;
                                </button>
                            </form>
                        </div>
                    </div>
                </div>
            </section>

            <!-- Digital Asset Categories Marketplace -->
            <section id="marketplace" class="max-w-7xl mx-auto px-6 py-10 border-t border-slate-800">
                <div class="flex flex-col md:flex-row justify-between items-center mb-8 gap-4">
                    <div>
                        <h2 class="text-2xl font-black text-white tracking-tight">Digital Assets Marketplace</h2>
                        <p class="text-slate-400 text-xs mt-1">Explore verified Telegram channels, TikTok, YouTube & Facebook accounts.</p>
                    </div>
                    <div class="flex items-center gap-2 w-full md:w-auto">
                        <input type="text" id="searchInput" oninput="searchListings()" placeholder="Search by name, category..." class="bg-slate-900 border border-slate-700 rounded-xl px-3 py-2 text-xs text-white focus:outline-none focus:border-amber-500 w-full md:w-64">
                        <button onclick="showBrowseListings('ALL')" class="px-4 py-2 bg-amber-500 hover:bg-amber-400 text-slate-950 font-bold rounded-xl text-xs transition cursor-pointer shadow-md whitespace-nowrap">
                            Browse All 🌐
                        </button>
                    </div>
                </div>
                
                <div class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-5 gap-4 mb-8">
                    <div class="p-5 bg-[#16203a] border border-slate-700/60 rounded-2xl hover:border-[#229ED9] transition shadow-xl space-y-3 cursor-pointer" onclick="showBrowseListings('Telegram')">
                        <div class="w-10 h-10 rounded-xl bg-[#229ED9]/20 text-[#229ED9] flex items-center justify-center text-xl"><i class="fa-brands fa-telegram"></i></div>
                        <h3 class="font-bold text-white text-base">Telegram Channels</h3>
                        <p class="text-xs text-slate-400">Verified members & groups.</p>
                        <span class="text-xs text-amber-400 font-bold">Browse Listings &rarr;</span>
                    </div>
                    <div class="p-5 bg-[#16203a] border border-slate-700/60 rounded-2xl hover:border-[#EE1D52] transition shadow-xl space-y-3 cursor-pointer" onclick="showBrowseListings('TikTok')">
                        <div class="w-10 h-10 rounded-xl bg-[#EE1D52]/20 text-[#EE1D52] flex items-center justify-center text-xl"><i class="fa-brands fa-tiktok"></i></div>
                        <h3 class="font-bold text-white text-base">TikTok Accounts</h3>
                        <p class="text-xs text-slate-400">Monetized creator accounts.</p>
                        <span class="text-xs text-amber-400 font-bold">Browse Listings &rarr;</span>
                    </div>
                    <div class="p-5 bg-[#16203a] border border-slate-700/60 rounded-2xl hover:border-[#FF0000] transition shadow-xl space-y-3 cursor-pointer" onclick="showBrowseListings('YouTube')">
                        <div class="w-10 h-10 rounded-xl bg-[#FF0000]/20 text-[#FF0000] flex items-center justify-center text-xl"><i class="fa-brands fa-youtube"></i></div>
                        <h3 class="font-bold text-white text-base">YouTube Channels</h3>
                        <p class="text-xs text-slate-400">Monetization ready channels.</p>
                        <span class="text-xs text-amber-400 font-bold">Browse Listings &rarr;</span>
                    </div>
                    <div class="p-5 bg-[#16203a] border border-slate-700/60 rounded-2xl hover:border-[#E1306C] transition shadow-xl space-y-3 cursor-pointer" onclick="showBrowseListings('Instagram')">
                        <div class="w-10 h-10 rounded-xl bg-[#E1306C]/20 text-[#E1306C] flex items-center justify-center text-xl"><i class="fa-brands fa-instagram"></i></div>
                        <h3 class="font-bold text-white text-base">Instagram Pages</h3>
                        <p class="text-xs text-slate-400">Active community profiles.</p>
                        <span class="text-xs text-amber-400 font-bold">Browse Listings &rarr;</span>
                    </div>
                    <div class="p-5 bg-[#16203a] border border-slate-700/60 rounded-2xl hover:border-[#1877F2] transition shadow-xl space-y-3 cursor-pointer" onclick="showBrowseListings('Facebook')">
                        <div class="w-10 h-10 rounded-xl bg-[#1877F2]/20 text-[#1877F2] flex items-center justify-center text-xl"><i class="fa-brands fa-facebook"></i></div>
                        <h3 class="font-bold text-white text-base">Facebook Pages</h3>
                        <p class="text-xs text-slate-400">High reach pages & groups.</p>
                        <span class="text-xs text-amber-400 font-bold">Browse Listings &rarr;</span>
                    </div>
                </div>

                <div id="browseListingsSection" class="bg-[#16203a] border border-slate-700/60 rounded-2xl p-6 shadow-2xl space-y-4">
                    <div class="flex justify-between items-center pb-3 border-b border-slate-800">
                        <h3 id="browseTitle" class="font-bold text-white text-base">All Browse Listings & Categories</h3>
                        <span class="text-xs text-amber-400 font-bold">🛡️ Escrow Protected Market</span>
                    </div>
                    <div id="browseContainer" class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
                        <div class="p-4 bg-slate-900/60 rounded-xl border border-slate-800 text-xs text-slate-400 col-span-full text-center">
                            No listings found. Use the form above to publish your asset ad!
                        </div>
                    </div>
                </div>
            </section>

            <!-- Tool Rental Section -->
            <section id="toolRentalSection" class="max-w-7xl mx-auto px-6 py-10 border-t border-slate-800">
                <div class="flex justify-between items-center mb-8">
                    <div>
                        <span class="text-xs text-amber-400 font-bold uppercase tracking-wider">For Technicians</span>
                        <h2 class="text-2xl font-black text-white tracking-tight mt-1">Mobile Repair Software Tool Rentals ⚡</h2>
                        <p class="text-slate-400 text-xs mt-1">Rent professional flashing software tools instantly.</p>
                    </div>
                </div>

                <div id="toolRentalContainer" class="grid grid-cols-1 md:grid-cols-3 gap-6">
                    <!-- Dynamically loaded from DB_TOOLS -->
                </div>
            </section>

            <!-- User Dashboard Section -->
            <section id="dashboardSection" class="max-w-7xl mx-auto px-6 py-10 border-t border-slate-800 mb-16">
                <div class="flex justify-between items-center mb-6">
                    <div>
                        <h2 class="text-2xl font-black text-white tracking-tight">User Dashboard</h2>
                        <p class="text-slate-400 text-xs mt-1">Manage your active listings and software tool rentals.</p>
                    </div>
                    <div class="flex space-x-2 bg-slate-900 p-1 rounded-xl border border-slate-800 text-xs font-semibold">
                        <button id="tabBtnListings" onclick="switchDashboardTab('listings')" class="px-4 py-2 rounded-lg bg-amber-500 text-slate-950 transition cursor-pointer">My Listings</button>
                        <button id="tabBtnRentals" onclick="switchDashboardTab('rentals')" class="px-4 py-2 rounded-lg text-slate-300 hover:text-white transition cursor-pointer">My Rentals</button>
                    </div>
                </div>

                <div id="contentListings" class="bg-[#16203a] border border-slate-700/60 rounded-2xl p-6 shadow-xl">
                    <div class="flex justify-between items-center mb-4">
                        <h3 class="font-bold text-white text-sm">Your Posted Digital Assets</h3>
                        <span class="text-xs bg-amber-500/20 text-amber-400 px-2.5 py-1 rounded-full font-bold">🛡️ Escrow Secured</span>
                    </div>
                    <div id="userListingsContainer" class="space-y-3">
                        <div class="p-4 bg-slate-900/60 rounded-xl border border-slate-800 text-xs text-slate-400 flex justify-between items-center">
                            <span>No active listings yet. Use the form above to add one!</span>
                            <span class="text-emerald-400 font-semibold">Escrow Ready</span>
                        </div>
                    </div>
                </div>

                <div id="contentRentals" class="hidden bg-[#16203a] border border-slate-700/60 rounded-2xl p-6 shadow-xl">
                    <div class="flex justify-between items-center mb-4">
                        <h3 class="font-bold text-white text-sm">Your Active Tool Rentals</h3>
                        <span class="text-xs bg-amber-500/20 text-amber-400 px-2.5 py-1 rounded-full font-bold">⚡ Instant Access</span>
                    </div>
                    <div id="userRentalsContainer" class="space-y-3">
                        <div class="p-4 bg-slate-900/60 rounded-xl border border-slate-800 text-xs text-slate-400 flex justify-between items-center">
                            <span>No active tool rentals. Choose a tool below to rent instantly.</span>
                            <span class="text-amber-400 font-semibold">Available 24/7</span>
                        </div>
                    </div>
                </div>
            </section>
        </div>

        <!-- Rental Modal with AnyDesk/Telegram & Chapa Inputs -->
        <div id="rentalModal" class="hidden fixed inset-0 bg-black/70 backdrop-blur-sm z-50 flex items-center justify-center p-4">
            <div class="bg-[#1c2541] border border-slate-700 rounded-3xl p-6 max-w-md w-full space-y-4 shadow-2xl text-xs">
                <div class="flex justify-between items-center pb-2 border-b border-slate-800">
                    <h3 id="modalToolTitle" class="font-bold text-white text-sm">Rent Tool</h3>
                    <button onclick="closeRentalModal()" class="text-slate-400 hover:text-white cursor-pointer"><i class="fa-solid fa-xmark text-base"></i></button>
                </div>
                <form id="rentalForm" onsubmit="submitToolRental(event)" class="space-y-3">
                    <input type="hidden" id="modalToolId">
                    <div>
                        <label class="block text-slate-300 font-semibold mb-1">Your AnyDesk ID / Remote ID *</label>
                        <input type="text" id="renterAnydesk" required placeholder="e.g., 1 234 567 890" class="w-full bg-slate-900 border border-slate-700 rounded-xl px-3 py-2 text-white focus:outline-none focus:border-amber-500">
                    </div>
                    <div>
                        <label class="block text-slate-300 font-semibold mb-1">Telegram Username *</label>
                        <input type="text" id="renterTelegram" required placeholder="e.g., @myusername" class="w-full bg-slate-900 border border-slate-700 rounded-xl px-3 py-2 text-white focus:outline-none focus:border-amber-500">
                    </div>
                    <div>
                        <label class="block text-slate-300 font-semibold mb-1">Payment Method *</label>
                        <select id="paymentMethod" onchange="toggleReceiptInput()" class="w-full bg-slate-900 border border-slate-700 rounded-xl px-2 py-2 text-white focus:outline-none focus:border-amber-500">
                            <option value="Chapa">Chapa Payment Gateway (Instant)</option>
                            <option value="Bank Transfer">Bank Transfer Receipt (Manual Verification)</option>
                        </select>
                    </div>
                    <div id="receiptUploadDiv" class="hidden">
                        <label class="block text-slate-300 font-semibold mb-1">Upload Bank Transfer Receipt *</label>
                        <input type="file" id="receiptFile" accept="image/*" class="w-full bg-slate-900 border border-slate-700 rounded-xl px-3 py-1.5 text-slate-400 text-[11px] cursor-pointer">
                    </div>
                    <button type="submit" class="w-full py-2.5 bg-amber-500 text-slate-950 font-bold rounded-xl hover:bg-amber-400 transition cursor-pointer shadow-md">
                        Proceed to Secure Payment & Start Timer &rarr;
                    </button>
                </form>
            </div>
        </div>

        <script>
            window.onload = function() {
                updateAssetTypes();
                loadTools();
                loadUserListings();
                loadUserRentals();
                showBrowseListings('ALL');
            };

            function switchPostFormTab(type) {
                const formAsset = document.getElementById('formPostAsset');
                const formTool = document.getElementById('formPostTool');
                const tabAssetBtn = document.getElementById('postTabAssetBtn');
                const tabToolBtn = document.getElementById('postTabToolBtn');

                if (type === 'asset') {
                    formAsset.classList.remove('hidden');
                    formTool.classList.add('hidden');
                    tabAssetBtn.className = "px-3 py-1.5 rounded-lg bg-amber-500 text-slate-950 transition cursor-pointer";
                    tabToolBtn.className = "px-3 py-1.5 rounded-lg text-slate-400 hover:text-white transition cursor-pointer";
                } else {
                    formTool.classList.remove('hidden');
                    formAsset.classList.add('hidden');
                    tabToolBtn.className = "px-3 py-1.5 rounded-lg bg-amber-500 text-slate-950 transition cursor-pointer";
                    tabAssetBtn.className = "px-3 py-1.5 rounded-lg text-slate-400 hover:text-white transition cursor-pointer";
                }
                document.getElementById('mainPostBoxContainer').scrollIntoView({ behavior: 'smooth' });
            }

            function updateAssetTypes() {
                const platform = document.getElementById('listingPlatform').value;
                const assetTypeSelect = document.getElementById('listingAssetType');
                let options = [];
                if (platform === 'Telegram') options = ['Channel', 'Group', 'Bot'];
                else if (platform === 'TikTok') options = ['Account (Live Enabled)', 'Monetized Account'];
                else if (platform === 'YouTube') options = ['Monetized Channel', 'Subscriber Channel'];
                else if (platform === 'Instagram') options = ['Page', 'Account'];
                else if (platform === 'Facebook') options = ['Page', 'Group'];
                assetTypeSelect.innerHTML = options.map(opt => `<option value="${opt}">${opt}</option>`).join('');
            }

            function handleProofUpload(e) {
                if (e.target.files[0]) {
                    document.getElementById('listingSubCount').value = (Math.floor(Math.random() * 45000) + 1200) + " Subs / Views Verified";
                }
            }

            async function loadTools() {
                const res = await fetch('/api/v1/tools');
                const tools = await res.json();
                const container = document.getElementById('toolRentalContainer');
                container.innerHTML = tools.map(t => `
                    <div class="p-5 bg-[#16203a] border border-slate-700/60 rounded-2xl space-y-3 shadow-xl flex flex-col justify-between">
                        <div class="space-y-2">
                            <div class="flex justify-between items-center">
                                <h3 class="font-bold text-white text-base">${t.tool_name}</h3>
                                <span class="text-xs bg-amber-500/20 text-amber-400 px-2 py-0.5 rounded-full font-bold">ETB ${t.rental_price} / ${t.rental_duration_hours} Hrs</span>
                            </div>
                            <p class="text-xs text-slate-300">${t.description}</p>
                            <p class="text-[11px] text-amber-300 font-semibold"><i class="fa-solid fa-link"></i> ${t.connection_type}</p>
                        </div>
                        <button onclick="openRentalModal(${t.id}, '${t.tool_name}')" class="w-full py-2 ${t.status === 'AVAILABLE' ? 'bg-amber-500 hover:bg-amber-400 text-slate-950' : 'bg-slate-700 text-slate-400 cursor-not-allowed'} font-bold rounded-xl text-xs transition cursor-pointer">
                            ${t.status === 'AVAILABLE' ? 'Rent Tool Now ⚡' : 'Currently Rented (Busy)'}
                        </button>
                    </div>
                `).join('');
            }

            function openRentalModal(id, name) {
                document.getElementById('modalToolId').value = id;
                document.getElementById('modalToolTitle').innerText = `Rent Tool: ${name}`;
                document.getElementById('rentalModal').classList.remove('hidden');
            }

            function closeRentalModal() {
                document.getElementById('rentalModal').classList.add('hidden');
            }

            function toggleReceiptInput() {
                const method = document.getElementById('paymentMethod').value;
                const uploadDiv = document.getElementById('receiptUploadDiv');
                if (method === 'Bank Transfer') uploadDiv.classList.remove('hidden');
                else uploadDiv.classList.add('hidden');
            }

            async function handlePostTool(e) {
                e.preventDefault();
                const formData = new FormData();
                formData.append('tool_name', document.getElementById('toolNameInput').value);
                formData.append('description', document.getElementById('toolDescInput').value);
                formData.append('rental_price', document.getElementById('toolPriceInput').value);
                formData.append('rental_duration_hours', document.getElementById('toolDurationInput').value);
                formData.append('connection_type', document.getElementById('toolConnectionType').value);

                const res = await fetch('/api/v1/tools/publish', { method: 'POST', body: formData });
                const data = await res.json();
                if (data.success) {
                    alert(data.message);
                    document.getElementById('formPostTool').reset();
                    loadTools();
                    switchPostFormTab('asset');
                }
            }

            async function submitToolRental(e) {
                e.preventDefault();
                const formData = new FormData();
                formData.append('tool_id', document.getElementById('modalToolId').value);
                formData.append('renter_anydesk_id', document.getElementById('renterAnydesk').value);
                formData.append('renter_telegram', document.getElementById('renterTelegram').value);
                formData.append('payment_method', document.getElementById('paymentMethod').value);
                
                const receiptFile = document.getElementById('receiptFile').files[0];
                if (receiptFile) formData.append('receipt_file', receiptFile);

                const res = await fetch('/api/v1/tools/rent', { method: 'POST', body: formData });
                const data = await res.json();
                if (data.success) {
                    alert(data.message);
                    closeRentalModal();
                    loadTools();
                    loadUserRentals();
                    switchDashboardTab('rentals');
                } else {
                    alert(data.detail || "Rental failed");
                }
            }

            function handlePostListing(e) {
                e.preventDefault();
                const title = document.getElementById('listingTitle').value.trim();
                const link = document.getElementById('listingLink').value.trim();
                const platform = document.getElementById('listingPlatform').value;
                const assetType = document.getElementById('listingAssetType').value;
                const niche = document.getElementById('listingNiche').value;
                const price = document.getElementById('listingPrice').value.trim();
                const subCount = document.getElementById('listingSubCount').value.trim();

                let listings = JSON.parse(localStorage.getItem('amalaj_listings') || '[]');
                listings.push({ platform: `${platform} (${assetType})`, niche, title, price, subCount, link });
                localStorage.setItem('amalaj_listings', JSON.stringify(listings));

                alert("Asset published successfully!");
                e.target.reset();
                loadUserListings();
                switchDashboardTab('listings');
            }

            function showBrowseListings(category) {
                const container = document.getElementById('browseContainer');
                const titleElem = document.getElementById('browseTitle');
                let listings = JSON.parse(localStorage.getItem('amalaj_listings') || '[]');
                titleElem.innerText = category === 'ALL' ? "All Browse Listings & Categories" : `Browse Listings: ${category}`;
                let filtered = category === 'ALL' ? listings : listings.filter(i => i.platform && i.platform.toLowerCase().includes(category.toLowerCase()));
                
                if (filtered.length === 0) {
                    container.innerHTML = `<div class="p-4 bg-slate-900/60 rounded-xl border border-slate-800 text-xs text-slate-400 col-span-full text-center">No listings found.</div>`;
                    return;
                }
                container.innerHTML = filtered.map(item => `
                    <div class="p-4 bg-slate-900/80 rounded-xl border border-slate-800 space-y-3 shadow-xl">
                        <div class="flex justify-between items-center"><span class="text-amber-400 font-bold uppercase text-[10px]">${item.platform}</span><span class="text-xs bg-emerald-500/20 text-emerald-400 px-2 py-0.5 rounded-full font-bold">🛡️ Escrow Active</span></div>
                        <h4 class="font-bold text-white text-sm">${item.title}</h4>
                        <div class="text-[11px] text-slate-300 space-y-1"><p>Category: <span class="text-amber-300 font-semibold">${item.niche}</span></p><p>Subscribers: <span class="font-semibold text-white">${item.subCount}</span></p></div>
                        <div class="flex justify-between items-center pt-2 border-t border-slate-800 text-xs"><span class="font-black text-amber-400">ETB ${item.price}</span><button onclick="alert('Connecting to seller...')" class="px-3 py-1.5 bg-amber-500 text-slate-950 font-bold rounded-lg hover:bg-amber-400 transition cursor-pointer">Buy / Chat</button></div>
                    </div>
                `).join('');
            }

            function searchListings() {
                const query = document.getElementById('searchInput').value.toLowerCase().trim();
                let listings = JSON.parse(localStorage.getItem('amalaj_listings') || '[]');
                const container = document.getElementById('browseContainer');
                let filtered = listings.filter(i => (i.title && i.title.toLowerCase().includes(query)) || (i.platform && i.platform.toLowerCase().includes(query)));
                if (filtered.length === 0) {
                    container.innerHTML = `<div class="p-4 bg-slate-900/60 rounded-xl border border-slate-800 text-xs text-slate-400 col-span-full text-center">No matching listings found.</div>`;
                    return;
                }
                container.innerHTML = filtered.map(item => `
                    <div class="p-4 bg-slate-900/80 rounded-xl border border-slate-800 space-y-3 shadow-xl">
                        <span class="text-amber-400 font-bold uppercase text-[10px]">${item.platform}</span>
                        <h4 class="font-bold text-white text-sm">${item.title}</h4>
                        <span class="font-black text-amber-400">ETB ${item.price}</span>
                    </div>
                `).join('');
            }

            function switchDashboardTab(tab) {
                const btnList = document.getElementById('tabBtnListings');
                const btnRent = document.getElementById('tabBtnRentals');
                const contentList = document.getElementById('contentListings');
                const contentRent = document.getElementById('contentRentals');
                if (tab === 'listings') {
                    btnList.className = "px-4 py-2 rounded-lg bg-amber-500 text-slate-950 transition cursor-pointer";
                    btnRent.className = "px-4 py-2 rounded-lg text-slate-300 hover:text-white transition cursor-pointer";
                    contentList.classList.remove('hidden');
                    contentRent.classList.add('hidden');
                } else {
                    btnRent.className = "px-4 py-2 rounded-lg bg-amber-500 text-slate-950 transition cursor-pointer";
                    btnList.className = "px-4 py-2 rounded-lg text-slate-300 hover:text-white transition cursor-pointer";
                    contentRent.classList.remove('hidden');
                    contentList.classList.add('hidden');
                }
            }

            function loadUserListings() {
                const container = document.getElementById('userListingsContainer');
                let listings = JSON.parse(localStorage.getItem('amalaj_listings') || '[]');
                if (listings.length === 0) {
                    container.innerHTML = `<div class="p-4 bg-slate-900/60 rounded-xl border border-slate-800 text-xs text-slate-400 flex justify-between items-center"><span>No active listings yet.</span><span class="text-emerald-400 font-semibold">Escrow Ready</span></div>`;
                    return;
                }
                container.innerHTML = listings.map(item => `
                    <div class="p-4 bg-slate-900/80 rounded-xl border border-slate-800 flex justify-between items-center text-xs">
                        <div><span class="text-amber-400 font-bold uppercase text-[10px]">${item.platform}</span><h4 class="font-bold text-white text-sm mt-0.5">${item.title}</h4></div>
                        <span class="font-extrabold text-emerald-400 text-sm">ETB ${item.price}</span>
                    </div>
                `).join('');
            }

            function loadUserRentals() {
                const container = document.getElementById('userRentalsContainer');
                let rentals = JSON.parse(localStorage.getItem('amalaj_rentals') || '[]');
                if (rentals.length === 0) {
                    container.innerHTML = `<div class="p-4 bg-slate-900/60 rounded-xl border border-slate-800 text-xs text-slate-400 flex justify-between items-center"><span>No active tool rentals.</span><span class="text-amber-400 font-semibold">Available 24/7</span></div>`;
                    return;
                }
                container.innerHTML = rentals.map(item => `
                    <div class="p-4 bg-slate-900/80 rounded-xl border border-slate-800 flex justify-between items-center text-xs">
                        <div><span class="text-amber-400 font-bold text-[10px]">TOOL RENTAL</span><h4 class="font-bold text-white text-sm mt-0.5">${item.name}</h4></div>
                        <span class="font-extrabold text-amber-400 text-sm">ETB ${item.price}</span>
                    </div>
                `).join('');
            }
        </script>
    </body>
    </html>
    """