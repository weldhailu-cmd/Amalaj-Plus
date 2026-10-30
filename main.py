from datetime import datetime, timedelta
from typing import List, Optional
from fastapi import FastAPI, File, Form, HTTPException, UploadFile, status
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel

app = FastAPI(title="Amalaj Plus API", version="2.8")

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
    return {"success": True, "message": "Repair tool published successfully with packages!", "tool": new_tool}

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
            <!-- Header / Navigation -->
            <header class="border-b border-slate-800 bg-[#0b132b]/95 backdrop-blur sticky top-0 z-50">
                <div class="max-w-7xl mx-auto px-6 py-4 flex justify-between items-center">
                    <div class="flex items-center space-x-3">
                        <div class="w-10 h-10 rounded-full border-2 border-amber-500 overflow-hidden shadow-lg shadow-amber-500/20 bg-white flex items-center justify-center p-0.5">
                            <img src="/static/logo.png" alt="Logo" class="w-full h-full object-cover rounded-full">
                        </div>
                        <span class="text-2xl font-extrabold text-white tracking-tight">Amalaj<span class="text-amber-400">Plus</span></span>
                    </div>

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
                        <button onclick="alert('Google Sign-In integration ready')" class="flex items-center space-x-2 bg-slate-800 hover:bg-slate-700 text-white font-bold px-4 py-2 rounded-xl transition border border-slate-700 cursor-pointer text-xs">
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
                            Amalaj Plus is a trusted platform to buy and sell verified Telegram channels, TikTok accounts, and instant software tool rentals with flexible packages.
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
                                        <select id="listingPlatform" class="w-full bg-slate-900 border border-slate-700 rounded-xl px-2 py-2 text-white focus:outline-none focus:border-amber-500">
                                            <option value="Telegram">Telegram</option>
                                            <option value="TikTok">TikTok</option>
                                            <option value="YouTube">YouTube</option>
                                        </select>
                                    </div>
                                    <div>
                                        <label class="block text-slate-300 font-semibold mb-1">Asking Price (ETB) *</label>
                                        <input type="number" id="listingPrice" required placeholder="5000" class="w-full bg-slate-900 border border-slate-700 rounded-xl px-3 py-2 text-white focus:outline-none focus:border-amber-500">
                                    </div>
                                </div>
                                <button type="submit" class="w-full py-2.5 bg-amber-500 text-slate-950 font-bold rounded-xl hover:bg-amber-400 transition cursor-pointer shadow-md">
                                    Publish Asset &rarr;
                                </button>
                            </form>

                            <!-- 2. Post Repair Tool Form (Updated with Dropdowns & Packages) -->
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
                        <label class="block text-slate-300 font-semibold mb-1">Your AnyDesk ID / Telegram Username *</label>
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

            window.onload = function() {
                updateToolDescription();
                loadTools();
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

            function updateToolDescription() {
                const selectedTool = document.getElementById('toolNameInput').value;
                document.getElementById('toolDescInput').value = toolDescriptions[selectedTool] || "";
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
                } else {
                    alert(data.detail || "Rental failed");
                }
            }

            function handlePostListing(e) {
                e.preventDefault();
                alert("Digital asset published successfully!");
                e.target.reset();
            }
        </script>
    </body>
    </html>
    """