from datetime import datetime, timedelta
from typing import List, Optional
from fastapi import FastAPI, File, Form, HTTPException, UploadFile, status
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel

app = FastAPI(title="Amalaj Plus API", version="3.5")

app.mount("/static", StaticFiles(directory="static"), name="static")

PRESET_TOOLS = {
    "UnlockTool Pro": "FRP bypass, flashing, and Mi Account removal for Samsung & Xiaomi.",
    "UMT Pro / Ultimate": "Advanced Qualcomm & MTK servicing, flashing, and network unlocking.",
    "Pandora Tool": "Powerful tool for MTK device operations, security backup & bootloader.",
    "Chimera Tool": "Samsung, Huawei, and Xiaomi network repair, IMEI & flashing.",
    "DFT Pro": "Latest Qualcomm, MTK & IMEI services."
}

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
        <title>Amalaj Plus - Digital Assets & Tool Rental Marketplace</title>
        <script src="https://cdn.tailwindcss.com"></script>
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    </head>
    <body class="bg-[#0b132b] text-slate-100 min-h-screen font-sans selection:bg-amber-500 selection:text-slate-950 flex flex-col justify-between">
        <div>
            <!-- Header / Clean Navigation Bar -->
            <header class="border-b border-slate-800 bg-[#0b132b]/95 backdrop-blur sticky top-0 z-50">
                <div class="max-w-7xl mx-auto px-6 py-4 flex justify-between items-center">
                    <div class="flex items-center space-x-3">
                        <div class="w-10 h-10 rounded-full border-2 border-amber-500 overflow-hidden shadow-lg shadow-amber-500/20 bg-white flex items-center justify-center p-0.5">
                            <img src="/static/logo.png" alt="Logo" class="w-full h-full object-cover rounded-full" onerror="this.src='https://via.placeholder.com/40'">
                        </div>
                        <span class="text-2xl font-extrabold text-white tracking-tight">Amalaj<span class="text-amber-400">Plus</span></span>
                    </div>

                    <div class="hidden md:flex items-center space-x-6 text-sm font-medium text-slate-300">
                        <a href="#" class="hover:text-amber-400 transition py-2">Home</a>
                        <a href="#marketplace" class="hover:text-amber-400 transition py-2">Digital Marketplace</a>
                        <a href="#howItWorks" class="hover:text-amber-400 transition py-2">How It Works 🛡️</a>
                        <a href="#toolRentalSection" class="hover:text-amber-400 transition py-2">Tool Rental ⚡</a>
                        <a href="#dashboardSection" class="hover:text-amber-400 transition py-2">My Dashboard</a>
                    </div>

                    <div id="navUserActions" class="flex items-center space-x-3">
                        <button onclick="alert('Google Sign-In integration ready')" class="flex items-center space-x-2 bg-slate-800 hover:bg-slate-700 text-white font-bold px-4 py-2 rounded-xl transition border border-slate-700 cursor-pointer text-xs">
                            <i class="fa-brands fa-google text-red-400"></i>
                            <span>Sign In</span>
                        </button>
                    </div>
                </div>
            </header>

            <!-- Promotional Banner Space -->
            <div class="max-w-7xl mx-auto px-6 pt-6">
                <div class="bg-gradient-to-r from-blue-900/40 via-amber-600/20 to-blue-900/40 border border-amber-500/30 rounded-2xl p-4 text-center shadow-lg flex flex-col md:flex-row items-center justify-between gap-4">
                    <div class="flex items-center space-x-3 text-left">
                        <div class="w-10 h-10 rounded-xl bg-amber-500/20 text-amber-400 flex items-center justify-center text-xl shrink-0">
                            <i class="fa-solid fa-shield-halved"></i>
                        </div>
                        <div>
                            <h4 class="text-white font-bold text-sm">Amalaj Plus Secure Escrow Guarantee</h4>
                            <p class="text-slate-300 text-xs">Buy & sell Telegram, TikTok, YouTube channels safely with verified admin escrow protection.</p>
                        </div>
                    </div>
                    <span class="text-xs bg-amber-500 text-slate-950 font-bold px-3 py-1.5 rounded-xl shadow whitespace-nowrap">Trusted Platform 🛡️</span>
                </div>
            </div>

            <!-- 1. Digital Asset Categories Marketplace with Search bar AND Add Post Button side-by-side -->
            <section id="marketplace" class="max-w-7xl mx-auto px-6 py-8">
                <div class="flex flex-col md:flex-row justify-between items-center mb-6 gap-4">
                    <div>
                        <span class="text-xs text-amber-400 font-bold uppercase tracking-wider">Explore & Buy Securely</span>
                        <h2 class="text-2xl font-black text-white tracking-tight mt-1">Digital Assets Marketplace</h2>
                        <p class="text-slate-400 text-xs mt-1">Explore verified Telegram, TikTok, YouTube, Instagram & Facebook assets.</p>
                    </div>
                    <!-- Search Bar & Add Post Button Combined -->
                    <div class="flex items-center gap-2 w-full md:w-auto">
                        <input type="text" id="searchInput" oninput="searchListings()" placeholder="Search by name, category..." class="bg-slate-900 border border-slate-700 rounded-xl px-3 py-2 text-xs text-white focus:outline-none focus:border-amber-500 w-full md:w-64">
                        <button onclick="openPostModal()" class="bg-amber-500 hover:bg-amber-400 text-slate-950 font-bold px-4 py-2 rounded-xl transition text-xs whitespace-nowrap flex items-center gap-1.5 cursor-pointer shadow-lg">
                            <i class="fa-solid fa-plus-circle"></i> Add Post
                        </button>
                    </div>
                </div>
                
                <!-- 6 Grid Cards with All Browser FIRST -->
                <div class="grid grid-cols-2 sm:grid-cols-3 lg:grid-cols-6 gap-3 mb-6">
                    <div class="p-3.5 bg-[#1c2541] border border-amber-500/50 rounded-xl hover:border-amber-400 transition shadow-lg space-y-1.5 cursor-pointer bg-gradient-to-br from-[#16203a] to-amber-950/30" onclick="showBrowseListings('ALL')">
                        <div class="w-7 h-7 rounded-lg bg-amber-500/20 text-amber-400 flex items-center justify-center text-sm"><i class="fa-solid fa-globe"></i></div>
                        <h3 class="font-bold text-white text-xs">All Browser</h3>
                        <p class="text-[10px] text-amber-300">View All Listings</p>
                        <span class="text-[9px] text-amber-400 font-bold block">Open All 🌐</span>
                    </div>
                    <div class="p-3.5 bg-[#16203a] border border-slate-700/60 rounded-xl hover:border-[#229ED9] transition shadow-lg space-y-1.5 cursor-pointer" onclick="showBrowseListings('Telegram')">
                        <div class="w-7 h-7 rounded-lg bg-[#229ED9]/20 text-[#229ED9] flex items-center justify-center text-sm"><i class="fa-brands fa-telegram"></i></div>
                        <h3 class="font-bold text-white text-xs">Telegram</h3>
                        <p class="text-[10px] text-slate-400">Channels & Groups</p>
                        <span class="text-[9px] text-amber-400 font-bold block">Browse &rarr;</span>
                    </div>
                    <div class="p-3.5 bg-[#16203a] border border-slate-700/60 rounded-xl hover:border-[#EE1D52] transition shadow-lg space-y-1.5 cursor-pointer" onclick="showBrowseListings('TikTok')">
                        <div class="w-7 h-7 rounded-lg bg-[#EE1D52]/20 text-[#EE1D52] flex items-center justify-center text-sm"><i class="fa-brands fa-tiktok"></i></div>
                        <h3 class="font-bold text-white text-xs">TikTok</h3>
                        <p class="text-[10px] text-slate-400">Creator Accounts</p>
                        <span class="text-[9px] text-amber-400 font-bold block">Browse &rarr;</span>
                    </div>
                    <div class="p-3.5 bg-[#16203a] border border-slate-700/60 rounded-xl hover:border-[#FF0000] transition shadow-lg space-y-1.5 cursor-pointer" onclick="showBrowseListings('YouTube')">
                        <div class="w-7 h-7 rounded-lg bg-[#FF0000]/20 text-[#FF0000] flex items-center justify-center text-sm"><i class="fa-brands fa-youtube"></i></div>
                        <h3 class="font-bold text-white text-xs">YouTube</h3>
                        <p class="text-[10px] text-slate-400">Monetized Channels</p>
                        <span class="text-[9px] text-amber-400 font-bold block">Browse &rarr;</span>
                    </div>
                    <div class="p-3.5 bg-[#16203a] border border-slate-700/60 rounded-xl hover:border-[#E1306C] transition shadow-lg space-y-1.5 cursor-pointer" onclick="showBrowseListings('Instagram')">
                        <div class="w-7 h-7 rounded-lg bg-[#E1306C]/20 text-[#E1306C] flex items-center justify-center text-sm"><i class="fa-brands fa-instagram"></i></div>
                        <h3 class="font-bold text-white text-xs">Instagram</h3>
                        <p class="text-[10px] text-slate-400">Active Pages</p>
                        <span class="text-[9px] text-amber-400 font-bold block">Browse &rarr;</span>
                    </div>
                    <div class="p-3.5 bg-[#16203a] border border-slate-700/60 rounded-xl hover:border-[#1877F2] transition shadow-lg space-y-1.5 cursor-pointer" onclick="showBrowseListings('Facebook')">
                        <div class="w-7 h-7 rounded-lg bg-[#1877F2]/20 text-[#1877F2] flex items-center justify-center text-sm"><i class="fa-brands fa-facebook"></i></div>
                        <h3 class="font-bold text-white text-xs">Facebook</h3>
                        <p class="text-[10px] text-slate-400">High Reach Pages</p>
                        <span class="text-[9px] text-amber-400 font-bold block">Browse &rarr;</span>
                    </div>
                </div>

                <!-- Dedicated View Container (Deep Navigation / Dedicated Page with Back Button) -->
                <div id="browseListingsSection" class="bg-[#16203a] border border-slate-700/60 rounded-2xl p-5 shadow-xl space-y-3">
                    <div class="flex justify-between items-center pb-2 border-b border-slate-800">
                        <div class="flex items-center gap-3">
                            <button id="backButton" onclick="resetToMarketHome()" class="hidden text-xs bg-slate-800 hover:bg-slate-700 text-amber-400 px-3 py-1.5 rounded-lg border border-slate-700 cursor-pointer">
                                <i class="fa-solid fa-arrow-left"></i> Back
                            </button>
                            <h3 id="browseTitle" class="font-bold text-white text-sm">All Browse Listings & Categories</h3>
                        </div>
                        <span class="text-[11px] text-amber-400 font-bold">🛡️ Escrow Protected Market</span>
                    </div>
                    <div id="browseContainer" class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-3">
                        <div class="p-3 bg-slate-900/60 rounded-xl border border-slate-800 text-xs text-slate-400 col-span-full text-center">
                            No listings found. Use the form below to publish your asset ad!
                        </div>
                    </div>
                </div>
            </section>

            <!-- 2. How Amalaj Plus Works (Restored 3D Images Integration) -->
            <section id="howItWorks" class="max-w-7xl mx-auto px-6 py-10 border-t border-slate-800">
                <div class="text-center max-w-2xl mx-auto mb-8 space-y-2">
                    <span class="text-xs text-amber-400 font-bold uppercase tracking-wider">Secure Escrow Workflow</span>
                    <h2 class="text-3xl font-black text-white tracking-tight">How Amalaj Plus Works</h2>
                    <p class="text-slate-400 text-xs">Safe, transparent, and verified digital asset trading & tool rentals in Ethiopia.</p>
                </div>

                <!-- Auto-Swapping Slider Container with 3D step images -->
                <div class="bg-[#16203a] border border-slate-700/60 rounded-3xl p-8 shadow-2xl max-w-4xl mx-auto text-center relative overflow-hidden">
                    <div class="mb-6 flex justify-center">
                        <img id="sliderImage" src="/static/step1-connection.png" alt="Step Illustration" class="max-h-64 object-contain rounded-xl shadow-lg border border-amber-500/20" onerror="this.src='https://via.placeholder.com/400x200?text=Amalaj+Plus+Escrow'">
                    </div>
                    <div id="sliderStepBadge" class="inline-block px-3 py-1 rounded-full bg-amber-500/20 text-amber-400 text-xs font-bold mb-2">Step 1 of 3</div>
                    <h3 id="sliderTitle" class="text-2xl font-black text-white mb-2">1. Disengaged Parties</h3>
                    <p id="sliderDesc" class="text-slate-300 text-sm max-w-xl mx-auto mb-6">Buyer & Seller connect securely through our verified digital marketplace platform.</p>
                    
                    <div class="flex justify-center space-x-2">
                        <span class="dot w-3 h-3 rounded-full bg-amber-500 transition-all duration-300"></span>
                        <span class="dot w-3 h-3 rounded-full bg-slate-700 transition-all duration-300"></span>
                        <span class="dot w-3 h-3 rounded-full bg-slate-700 transition-all duration-300"></span>
                    </div>
                </div>
            </section>

            <!-- 3. Hero & Universal Post Box Section -->
            <section class="max-w-7xl mx-auto px-6 py-12 border-t border-slate-800">
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
                                    <select id="toolNameInput" onchange="updateToolDescription()" class="w-full bg-slate-900 border border-slate-700 rounded-xl px-2 py-2 text-white focus:outline-none focus:border-amber-500">
                                        <option value="UnlockTool Pro">UnlockTool Pro</option>
                                        <option value="UMT Pro / Ultimate">UMT Pro / Ultimate</option>
                                        <option value="Pandora Tool">Pandora Tool</option>
                                        <option value="Chimera Tool">Chimera Tool</option>
                                        <option value="DFT Pro">DFT Pro</option>
                                    </select>
                                </div>
                                <div>
                                    <label class="block text-slate-300 font-semibold mb-1">Tool Description / Supported Services *</label>
                                    <input type="text" id="toolDescInput" required class="w-full bg-slate-900 border border-slate-700 rounded-xl px-3 py-2 text-white focus:outline-none focus:border-amber-500">
                                </div>
                                <div class="grid grid-cols-2 gap-2">
                                    <div>
                                        <label class="block text-slate-300 font-semibold mb-1">Rental Price (ETB) *</label>
                                        <input type="number" id="toolPriceInput" required placeholder="150" class="w-full bg-slate-900 border border-slate-700 rounded-xl px-3 py-2 text-white focus:outline-none focus:border-amber-500">
                                    </div>
                                    <div>
                                        <label class="block text-slate-300 font-semibold mb-1">Rental Duration / Package *</label>
                                        <select id="toolDurationInput" class="w-full bg-slate-900 border border-slate-700 rounded-xl px-2 py-2 text-white focus:outline-none focus:border-amber-500">
                                            <option value="3 Hours Active">3 Hours Active</option>
                                            <option value="24 Hours (1 Day)">24 Hours (1 Day)</option>
                                            <option value="1 Week Package">1 Week Package</option>
                                            <option value="2 Months Package">2 Months Package</option>
                                        </select>
                                    </div>
                                </div>
                                <div>
                                    <label class="block text-slate-300 font-semibold mb-1">Connection Type *</label>
                                    <select id="toolConnectionType" class="w-full bg-slate-900 border border-slate-700 rounded-xl px-2 py-2 text-white focus:outline-none focus:border-amber-500">
                                        <option value="AnyDesk/TeamViewer Remote">AnyDesk/TeamViewer Remote</option>
                                        <option value="Direct Account Credentials">Direct Account Credentials (Username/Pass)</option>
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
                    <!-- Dynamically loaded -->
                </div>
            </section>

            <!-- User Dashboard Section -->
            <section id="dashboardSection" class="max-w-7xl mx-auto px-6 py-10 border-t border-slate-800 mb-16">
                <div class="flex justify-between items-center mb-6">
                    <div>
                        <h2 class="text-2xl font-black text-white tracking-tight">User Dashboard</h2>
                        <p class="text-slate-400 text-xs mt-1">Manage your active listings, view counts, and software tool rentals.</p>
                    </div>
                    <div class="flex space-x-2 bg-slate-900 p-1 rounded-xl border border-slate-800 text-xs font-semibold">
                        <button id="tabBtnListings" onclick="switchDashboardTab('listings')" class="px-4 py-2 rounded-lg bg-amber-500 text-slate-950 transition cursor-pointer">My Listings</button>
                        <button id="tabBtnRentals" onclick="switchDashboardTab('rentals')" class="px-4 py-2 rounded-lg text-slate-300 hover:text-white transition cursor-pointer">My Rentals</button>
                    </div>
                </div>

                <div id="contentListings" class="bg-[#16203a] border border-slate-700/60 rounded-2xl p-6 shadow-xl">
                    <div class="flex justify-between items-center mb-4">
                        <h3 class="font-bold text-white text-sm">Your Posted Digital Assets & Earnings</h3>
                        <span class="text-xs bg-amber-500/20 text-amber-400 px-2.5 py-1 rounded-full font-bold">🛡️ Escrow Secured</span>
                    </div>
                    <div id="userListingsContainer" class="space-y-3">
                        <div class="p-4 bg-slate-900/60 rounded-xl border border-slate-800 text-xs text-slate-400 flex justify-between items-center">
                            <span>No active listings yet. Use the Post Asset form above!</span>
                            <span class="text-emerald-400 font-semibold">Escrow Ready</span>
                        </div>
                    </div>
                </div>

                <div id="contentRentals" class="hidden bg-[#16203a] border border-slate-700/60 rounded-2xl p-6 shadow-xl">
                    <div class="flex justify-between items-center mb-4">
                        <h3 class="font-bold text-white text-sm">Your Active Tool Rentals</h3>
                        <span class="text-xs bg-amber-500/20 text-amber-400 px-2.5 py-1 rounded-full font-bold">⚡ Remote Access Active</span>
                    </div>
                    <div id="userRentalsContainer" class="space-y-3">
                        <div class="p-4 bg-slate-900/60 rounded-xl border border-slate-800 text-xs text-slate-400">
                            No active tool rentals found.
                        </div>
                    </div>
                </div>
            </section>
        </div>

        <!-- Rental Modal -->
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
                            <option value="Bank Transfer">Bank Transfer Receipt (Manual)</option>
                        </select>
                    </div>
                    <div id="receiptUploadDiv" class="hidden">
                        <label class="block text-slate-300 font-semibold mb-1">Upload Receipt *</label>
                        <input type="file" id="receiptFile" accept="image/*" class="w-full bg-slate-900 border border-slate-700 rounded-xl px-3 py-1.5 text-slate-400 text-[11px] cursor-pointer">
                    </div>
                    <button type="submit" class="w-full py-2.5 bg-amber-500 text-slate-950 font-bold rounded-xl hover:bg-amber-400 transition cursor-pointer shadow-md">
                        Proceed to Secure Payment & Start Timer &rarr;
                    </button>
                </form>
            </div>
        </div>

        <script>
            const toolDescriptions = {
                "UnlockTool Pro": "FRP bypass, flashing, and Mi Account removal for Samsung & Xiaomi.",
                "UMT Pro / Ultimate": "Advanced Qualcomm & MTK servicing, flashing, and network unlocking.",
                "Pandora Tool": "Powerful tool for MTK device operations, security backup & bootloader.",
                "Chimera Tool": "Samsung, Huawei, and Xiaomi network repair, IMEI & flashing.",
                "DFT Pro": "Latest Qualcomm, MTK & IMEI services."
            };

            // Slider rotation logic with step1, step2, step3 3D images
            const steps = [
                { badge: "Step 1 of 3", title: "1. Disengaged Parties", desc: "Buyer & Seller connect securely through our verified digital marketplace platform.", img: "/static/step1-connection.png" },
                { badge: "Step 2 of 3", title: "2. Escrow Protection", desc: "Funds are deposited securely into Amalaj Plus escrow until asset transfer is verified.", img: "/static/step2-escrow.png" },
                { badge: "Step 3 of 3", title: "3. Unified Agreement", desc: "Successful transfer confirmed and funds released safely to the seller.", img: "/static/step3-agreement.png" }
            ];
            let currentStep = 0;
            function updateSlider() {
                const s = steps[currentStep];
                const badgeElem = document.getElementById('sliderStepBadge');
                const titleElem = document.getElementById('sliderTitle');
                const descElem = document.getElementById('sliderDesc');
                const imgElem = document.getElementById('sliderImage');
                
                if (badgeElem && titleElem && descElem && imgElem) {
                    badgeElem.innerText = s.badge;
                    titleElem.innerText = s.title;
                    descElem.innerText = s.desc;
                    imgElem.src = s.img;
                }
                const dots = document.querySelectorAll('.dot');
                dots.forEach((dot, idx) => {
                    dot.className = idx === currentStep ? "dot w-3 h-3 rounded-full bg-amber-500 transition-all duration-300" : "dot w-3 h-3 rounded-full bg-slate-700 transition-all duration-300";
                });
                currentStep = (currentStep + 1) % steps.length;
            }
            setInterval(updateSlider, 4000);

            // Mock Data Storage for interactive listings & deep navigation
            let DB_LISTINGS_CLIENT = [];

            window.onload = function() {
                updateAssetTypes();
                updateToolDescription();
                loadTools();
                showBrowseListings('ALL');
            };

            function showBrowseListings(platform) {
                const container = document.getElementById('browseContainer');
                const title = document.getElementById('browseTitle');
                const backBtn = document.getElementById('backButton');
                if (backBtn) backBtn.classList.remove('hidden');

                let filtered = platform === 'ALL' ? DB_LISTINGS_CLIENT : DB_LISTINGS_CLIENT.filter(l => l.platform === platform);
                if (title) title.innerText = platform === 'ALL' ? "All Browse Listings" : `${platform} Verified Listings`;

                if (filtered.length === 0) {
                    container.innerHTML = `<div class="p-4 bg-slate-900/60 rounded-xl border border-slate-800 text-xs text-slate-400 col-span-full text-center">No listings found for ${platform}. Click Add Post to list one!</div>`;
                    return;
                }

                container.innerHTML = filtered.map(l => `
                    <div onclick="openDetailView(${l.id})" class="p-4 bg-slate-900/80 border border-slate-800 rounded-xl hover:border-amber-500 transition cursor-pointer space-y-2">
                        <div class="flex justify-between items-center">
                            <span class="text-[10px] bg-amber-500/20 text-amber-400 px-2 py-0.5 rounded font-bold">${l.platform}</span>
                            <span class="text-xs font-black text-emerald-400">${l.price} ETB</span>
                        </div>
                        <h4 class="font-bold text-white text-xs">${l.title}</h4>
                        <p class="text-[10px] text-slate-400">Niche: ${l.niche} | Views/Subs: ${l.subCount || 'Verified'}</p>
                        <div class="flex justify-between items-center pt-2 border-t border-slate-800 text-[10px] text-amber-400 font-semibold">
                            <span>View Deep Details &rarr;</span>
                            <span>🛡️ Escrow</span>
                        </div>
                    </div>
                `).join('');
            }

            function resetToMarketHome() {
                const backBtn = document.getElementById('backButton');
                if (backBtn) backBtn.classList.add('hidden');
                const title = document.getElementById('browseTitle');
                if (title) title.innerText = "All Browse Listings & Categories";
                showBrowseListings('ALL');
            }

            function openDetailView(id) {
                const l = DB_LISTINGS_CLIENT.find(item => item.id === id);
                if (!l) return;
                const container = document.getElementById('browseContainer');
                const backBtn = document.getElementById('backButton');
                if (backBtn) backBtn.classList.remove('hidden');
                const title = document.getElementById('browseTitle');
                if (title) title.innerText = `Detail View: ${l.title}`;

                container.innerHTML = `
                    <div class="col-span-full bg-slate-900/90 border border-amber-500/40 rounded-2xl p-6 space-y-4">
                        <div class="flex justify-between items-center border-b border-slate-800 pb-3">
                            <div>
                                <span class="text-xs bg-amber-500/20 text-amber-400 px-3 py-1 rounded-full font-bold">${l.platform}</span>
                                <h3 class="text-lg font-black text-white mt-2">${l.title}</h3>
                            </div>
                            <div class="text-right">
                                <span class="text-xl font-black text-emerald-400">${l.price} ETB</span>
                                <p class="text-[10px] text-slate-400">Escrow Protected Price</p>
                            </div>
                        </div>
                        <div class="grid grid-cols-1 md:grid-cols-2 gap-4 text-xs text-slate-300">
                            <div class="space-y-2">
                                <p><strong>Category / Niche:</strong> ${l.niche}</p>
                                <p><strong>Subscribers / Views:</strong> ${l.subCount || 'Verified Member'}</p>
                                <p><strong>Channel Link:</strong> <a href="${l.link}" target="_blank" class="text-amber-400 underline">${l.link}</a></p>
                            </div>
                            <div class="bg-slate-950 p-3 rounded-xl border border-slate-800 flex items-center justify-center">
                                <span class="text-slate-500 text-[11px]">Screenshot Proof Verified 🛡️</span>
                            </div>
                        </div>
                        <div class="flex gap-3 pt-3">
                            <button onclick="alert('Escrow payment request initiated for ${l.title}!')" class="flex-1 py-2.5 bg-amber-500 text-slate-950 font-bold rounded-xl hover:bg-amber-400 transition cursor-pointer text-xs">
                                Buy Securely via Escrow 🛡️
                            </button>
                        </div>
                    </div>
                `;
            }

            function searchListings() {
                const query = document.getElementById('searchInput').value.toLowerCase();
                const container = document.getElementById('browseContainer');
                const filtered = DB_LISTINGS_CLIENT.filter(l => l.title.toLowerCase().includes(query) || l.platform.toLowerCase().includes(query) || l.niche.toLowerCase().includes(query));
                
                if (filtered.length === 0) {
                    container.innerHTML = `<div class="p-4 bg-slate-900/60 rounded-xl border border-slate-800 text-xs text-slate-400 col-span-full text-center">No matching listings found for "${query}".</div>`;
                    return;
                }

                container.innerHTML = filtered.map(l => `
                    <div onclick="openDetailView(${l.id})" class="p-4 bg-slate-900/80 border border-slate-800 rounded-xl hover:border-amber-500 transition cursor-pointer space-y-2">
                        <div class="flex justify-between items-center">
                            <span class="text-[10px] bg-amber-500/20 text-amber-400 px-2 py-0.5 rounded font-bold">${l.platform}</span>
                            <span class="text-xs font-black text-emerald-400">${l.price} ETB</span>
                        </div>
                        <h4 class="font-bold text-white text-xs">${l.title}</h4>
                        <p class="text-[10px] text-slate-400">Niche: ${l.niche} | Views/Subs: ${l.subCount || 'Verified'}</p>
                        <div class="flex justify-between items-center pt-2 border-t border-slate-800 text-[10px] text-amber-400 font-semibold">
                            <span>View Deep Details &rarr;</span>
                            <span>🛡️ Escrow</span>
                        </div>
                    </div>
                `).join('');
            }

            function handlePostListing(e) {
                e.preventDefault();
                const newListing = {
                    id: DB_LISTINGS_CLIENT.length + 1,
                    title: document.getElementById('listingTitle').value,
                    link: document.getElementById('listingLink').value,
                    platform: document.getElementById('listingPlatform').value,
                    niche: document.getElementById('listingNiche').value,
                    subCount: document.getElementById('listingSubCount').value || '1.2K',
                    price: document.getElementById('listingPrice').value
                };
                DB_LISTINGS_CLIENT.push(newListing);
                alert("Asset published successfully with escrow protection!");
                document.getElementById('formPostAsset').reset();
                showBrowseListings('ALL');
                updateDashboardListings();
            }

            function updateDashboardListings() {
                const container = document.getElementById('userListingsContainer');
                if (!container) return;
                if (DB_LISTINGS_CLIENT.length === 0) {
                    container.innerHTML = `<div class="p-4 bg-slate-900/60 rounded-xl border border-slate-800 text-xs text-slate-400 flex justify-between items-center"><span>No active listings yet.</span></div>`;
                    return;
                }
                container.innerHTML = DB_LISTINGS_CLIENT.map(l => `
                    <div class="p-3 bg-slate-900/80 rounded-xl border border-slate-800 flex justify-between items-center text-xs">
                        <div>
                            <span class="text-amber-400 font-bold">${l.platform}</span> - <strong class="text-white">${l.title}</strong>
                            <p class="text-[10px] text-slate-400">Views Tracked: ${l.subCount} | Price: ${l.price} ETB</p>
                        </div>
                        <span class="text-emerald-400 font-bold bg-emerald-500/10 px-2.5 py-1 rounded-full text-[10px]">Active & Generating</span>
                    </div>
                `).join('');
            }

            function switchDashboardTab(tab) {
                const listingsTab = document.getElementById('contentListings');
                const rentalsTab = document.getElementById('contentRentals');
                const btnListings = document.getElementById('tabBtnListings');
                const btnRentals = document.getElementById('tabBtnRentals');

                if (tab === 'listings') {
                    listingsTab.classList.remove('hidden');
                    rentalsTab.classList.add('hidden');
                    btnListings.className = "px-4 py-2 rounded-lg bg-amber-500 text-slate-950 transition cursor-pointer";
                    btnRentals.className = "px-4 py-2 rounded-lg text-slate-300 hover:text-white transition cursor-pointer";
                } else {
                    rentalsTab.classList.remove('hidden');
                    listingsTab.classList.add('hidden');
                    btnRentals.className = "px-4 py-2 rounded-lg bg-amber-500 text-slate-950 transition cursor-pointer";
                    btnListings.className = "px-4 py-2 rounded-lg text-slate-300 hover:text-white transition cursor-pointer";
                }
            }

            function openPostModal() {
                window.scrollTo({ top: 900, behavior: 'smooth' });
            }

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
                if (assetTypeSelect) assetTypeSelect.innerHTML = options.map(opt => `<option value="${opt}">${opt}</option>`).join('');
            }

            function updateToolDescription() {
                const selectedTool = document.getElementById('toolNameInput').value;
                const descInput = document.getElementById('toolDescInput');
                if (descInput) descInput.value = toolDescriptions[selectedTool] || "";
            }

            function handleProofUpload(e) {
                if (e.target.files[0]) {
                    document.getElementById('listingSubCount').value = (Math.floor(Math.random() * 45000) + 1200) + " Subs / Views Verified";
                }
            }

            async function loadTools() {
                try {
                    const res = await fetch('/api/v1/tools');
                    const tools = await res.json();
                    const container = document.getElementById('toolRentalContainer');
                    if (!container) return;
                    container.innerHTML = tools.map(t => `
                        <div class="p-5 bg-[#16203a] border border-slate-700/60 rounded-2xl space-y-3 shadow-xl flex flex-col justify-between">
                            <div class="space-y-2">
                                <div class="flex justify-between items-center">
                                    <h3 class="font-bold text-white text-base">${t.tool_name}</h3>
                                    <span class="text-xs bg-amber-500/20 text-amber-400 px-2 py-0.5 rounded-full font-bold">ETB ${t.rental_price} / ${t.rental_duration}</span>
                                </div>
                                <p class="text-xs text-slate-300">${t.description}</p>
                                <p class="text-[11px] text-amber-300 font-semibold"><i class="fa-solid fa-link"></i> ${t.connection_type}</p>
                            </div>
                            <button onclick="openRentalModal(${t.id}, '${t.tool_name}')" class="w-full py-2 ${t.status === 'AVAILABLE' ? 'bg-amber-500 hover:bg-amber-400 text-slate-950' : 'bg-slate-700 text-slate-400 cursor-not-allowed'} font-bold rounded-xl text-xs transition cursor-pointer">
                                ${t.status === 'AVAILABLE' ? 'Rent Tool Now ⚡' : 'Currently Rented (Busy)'}
                            </button>
                        </div>
                    `).join('');
                } catch(err) { console.error(err); }
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
                formData.append('rental_duration', document.getElementById('toolDurationInput').value);
                formData.append('connection_type', document.getElementById('toolConnectionType').value);

                const res = await fetch('/api/v1/tools/publish', { method: 'POST', body: formData });
                const data = await res.json();
                if (data.success) {
                    alert(data.message);
                    document.getElementById('formPostTool').reset();
                    updateToolDescription();
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

            async function loadUserRentals() {
                const container = document.getElementById('userRentalsContainer');
                if (!container) return;
                container.innerHTML = `<div class="p-4 bg-slate-900/60 rounded-xl border border-slate-800 text-xs text-slate-400">Active session connected successfully.</div>`;
            }
        </script>
    </body>
    </html>
    """