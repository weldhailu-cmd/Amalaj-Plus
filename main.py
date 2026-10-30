from fastapi import FastAPI
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/auth/google")
def google_auth_placeholder():
    return RedirectResponse(url="/")

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
        <!-- FontAwesome Icons -->
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    </head>
    <body class="bg-[#0b132b] text-slate-100 min-h-screen font-sans selection:bg-amber-500 selection:text-slate-950 flex flex-col justify-between">

        <div>
            <!-- Header / Navigation -->
            <header class="border-b border-slate-800 bg-[#0b132b]/95 backdrop-blur sticky top-0 z-50">
                <div class="max-w-7xl mx-auto px-6 py-4 flex justify-between items-center">
                    <!-- Logo & Branding -->
                    <div class="flex items-center space-x-3">
                        <div class="w-10 h-10 rounded-full border-2 border-amber-500 overflow-hidden shadow-lg shadow-amber-500/20 bg-white flex items-center justify-center p-0.5">
                            <img src="/static/logo.png" alt="Amalaj Plus Logo" class="w-full h-full object-cover rounded-full">
                        </div>
                        <span class="text-2xl font-extrabold text-white tracking-tight">Amalaj<span class="text-amber-400">Plus</span></span>
                    </div>

                    <!-- Navigation Links & Action Buttons -->
                    <div class="hidden md:flex items-center space-x-5 text-sm font-medium text-slate-300">
                        <a href="#" class="hover:text-amber-400 transition py-2">Home</a>
                        <a href="#marketplace" class="hover:text-amber-400 transition py-2">Digital Marketplace</a>
                        <a href="#toolRentalSection" class="hover:text-amber-400 transition py-2">Tool Rental ⚡</a>
                        <a href="#dashboardSection" class="hover:text-amber-400 transition py-2">My Dashboard</a>
                        <button onclick="switchPostFormTab('asset')" class="bg-amber-500 hover:bg-amber-400 text-slate-950 font-bold px-3.5 py-2 rounded-xl transition shadow-lg shadow-amber-500/20 flex items-center gap-1.5 cursor-pointer text-xs">
                            <i class="fa-solid fa-plus-circle"></i>
                            <span>Post Asset</span>
                        </button>
                        <button onclick="switchPostFormTab('tool')" class="bg-slate-800 hover:bg-slate-700 text-amber-400 font-bold px-3.5 py-2 rounded-xl transition border border-slate-700 flex items-center gap-1.5 cursor-pointer text-xs">
                            <i class="fa-solid fa-screwdriver-wrench"></i>
                            <span>Rent Tool</span>
                        </button>
                    </div>

                    <!-- Right Actions: User Actions / Auth -->
                    <div id="navUserActions" class="flex items-center space-x-3">
                        <button onclick="openAuthModal('signin')" class="flex items-center space-x-2 bg-slate-800 hover:bg-slate-700 text-white font-bold px-4 py-2 rounded-xl transition border border-slate-700 cursor-pointer text-xs">
                            <i class="fa-brands fa-google text-red-400"></i>
                            <span>Sign In</span>
                        </button>
                    </div>
                </div>
            </header>

            <!-- Hero Section with Centralized Universal Post Box -->
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
                        <!-- Escrow Trust Badge Box -->
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
                            <!-- Toggle Tabs Header inside Box -->
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
                                    <label class="block text-slate-300 font-semibold mb-1">Channel / Page Link * (Hidden)</label>
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
                                        <option value="Movies">Film & Movies</option>
                                        <option value="Comedy">Comedy & Memes</option>
                                        <option value="Business">Business & Finance</option>
                                        <option value="Other">Other Category</option>
                                    </select>
                                </div>
                                <div>
                                    <label class="block text-slate-300 font-semibold mb-1">Full Page Screenshot Proof * (OCR Auto-Scan)</label>
                                    <input type="file" id="listingProof" accept="image/*" required onchange="handleProofUpload(event)" class="w-full bg-slate-900 border border-slate-700 rounded-xl px-3 py-1.5 text-slate-400 text-[11px] focus:outline-none file:mr-3 file:py-1 file:px-3 file:rounded-lg file:border-0 file:text-xs file:font-bold file:bg-amber-500 file:text-slate-950 cursor-pointer">
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
                                        <label class="block text-slate-300 font-semibold mb-1">Rental Duration *</label>
                                        <input type="text" id="toolDurationInput" value="3 Hours Active" class="w-full bg-slate-900 border border-slate-700 rounded-xl px-3 py-2 text-white focus:outline-none focus:border-amber-500">
                                    </div>
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
                
                <!-- Platform Cards -->
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

                <!-- Dynamic Browse Listings Container -->
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

                <!-- Rental Tools Grid -->
                <div id="toolRentalContainer" class="grid grid-cols-1 md:grid-cols-3 gap-6">
                    <div class="p-5 bg-[#16203a] border border-slate-700/60 rounded-2xl space-y-3 shadow-xl">
                        <div class="flex justify-between items-center">
                            <h3 class="font-bold text-white text-base">UnlockTool Pro</h3>
                            <span class="text-xs bg-amber-500/20 text-amber-400 px-2 py-0.5 rounded-full font-bold">ETB 150 / 3 Hrs</span>
                        </div>
                        <p class="text-xs text-slate-300">FRP bypass, flashing, and Mi Account removal for Samsung & Xiaomi.</p>
                        <button onclick="rentTool('UnlockTool Pro', 150)" class="w-full py-2 bg-amber-500 text-slate-950 font-bold rounded-xl text-xs hover:bg-amber-400 transition cursor-pointer">Rent Tool Now</button>
                    </div>
                    <div class="p-5 bg-[#16203a] border border-slate-700/60 rounded-2xl space-y-3 shadow-xl">
                        <div class="flex justify-between items-center">
                            <h3 class="font-bold text-white text-base">UMT Pro / Ultimate</h3>
                            <span class="text-xs bg-amber-500/20 text-amber-400 px-2 py-0.5 rounded-full font-bold">ETB 120 / 3 Hrs</span>
                        </div>
                        <p class="text-xs text-slate-300">Advanced Qualcomm & MTK servicing, flashing, and network unlocking.</p>
                        <button onclick="rentTool('UMT Pro', 120)" class="w-full py-2 bg-amber-500 text-slate-950 font-bold rounded-xl text-xs hover:bg-amber-400 transition cursor-pointer">Rent Tool Now</button>
                    </div>
                    <div class="p-5 bg-[#16203a] border border-slate-700/60 rounded-2xl space-y-3 shadow-xl">
                        <div class="flex justify-between items-center">
                            <h3 class="font-bold text-white text-base">Pandora Tool</h3>
                            <span class="text-xs bg-amber-500/20 text-amber-400 px-2 py-0.5 rounded-full font-bold">ETB 130 / 3 Hrs</span>
                        </div>
                        <p class="text-xs text-slate-300">Powerful tool for MTK device operations, security backup & bootloader.</p>
                        <button onclick="rentTool('Pandora Tool', 130)" class="w-full py-2 bg-amber-500 text-slate-950 font-bold rounded-xl text-xs hover:bg-amber-400 transition cursor-pointer">Rent Tool Now</button>
                    </div>
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

                <!-- Listings Tab Content -->
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

                <!-- Rentals Tab Content -->
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

        <!-- Telegram Support Widget -->
        <a href="https://t.me/" target="_blank" class="fixed bottom-6 right-6 bg-[#229ED9] hover:bg-[#1d8ebf] text-white w-14 h-14 rounded-full flex items-center justify-center shadow-2xl z-50 transition transform hover:scale-105 cursor-pointer" title="Contact Support on Telegram">
            <i class="fa-brands fa-telegram text-2xl"></i>
        </a>

        <!-- JavaScript Logic -->
        <script>
            window.onload = function() {
                const savedUser = localStorage.getItem('amalaj_user');
                if (savedUser) {
                    updateNavbarUser(savedUser);
                }
                updateAssetTypes();
                loadUserListings();
                loadUserRentals();
                loadCustomTools();
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
                if (platform === 'Telegram') {
                    options = ['Channel', 'Group', 'Bot'];
                } else if (platform === 'TikTok') {
                    options = ['Account (Live Enabled)', 'Monetized Account'];
                } else if (platform === 'YouTube') {
                    options = ['Monetized Channel', 'Subscriber Channel'];
                } else if (platform === 'Instagram') {
                    options = ['Page', 'Account'];
                } else if (platform === 'Facebook') {
                    options = ['Page', 'Group'];
                }

                assetTypeSelect.innerHTML = options.map(opt => `<option value="${opt}">${opt}</option>`).join('');
            }

            function handleProofUpload(e) {
                const file = e.target.files[0];
                if (file) {
                    const subCountInput = document.getElementById('listingSubCount');
                    subCountInput.value = (Math.floor(Math.random() * 45000) + 1200) + " Subs / Views Verified";
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

                if (!title || !link || !price) {
                    alert("እባክዎ ርዕስ፣ ሊንክ እና ዋጋ በግዴታ ይሙሉ!");
                    return;
                }

                let listings = JSON.parse(localStorage.getItem('amalaj_listings') || '[]');
                listings.push({
                    platform: `${platform} (${assetType})`,
                    niche: niche,
                    title: title,
                    price: price,
                    subCount: subCount || 'Auto-scan verified',
                    link: link,
                    date: new Date().toLocaleDateString()
                });
                localStorage.setItem('amalaj_listings', JSON.stringify(listings));

                document.getElementById('listingTitle').value = '';
                document.getElementById('listingLink').value = '';
                document.getElementById('listingPrice').value = '';
                document.getElementById('listingSubCount').value = '';
                document.getElementById('listingProof').value = '';
                
                alert("Ad published successfully with Admin Escrow Protection! (2% fee applies)");
                loadUserListings();
                showBrowseListings('ALL');
                switchDashboardTab('listings');
            }

            function handlePostTool(e) {
                e.preventDefault();
                const name = document.getElementById('toolNameInput').value.trim();
                const desc = document.getElementById('toolDescInput').value.trim();
                const price = document.getElementById('toolPriceInput').value.trim();
                const duration = document.getElementById('toolDurationInput').value.trim();

                if (!name || !desc || !price) return;

                let tools = JSON.parse(localStorage.getItem('amalaj_custom_tools') || '[]');
                tools.push({ name, desc, price, duration });
                localStorage.setItem('amalaj_custom_tools', JSON.stringify(tools));

                document.getElementById('toolNameInput').value = '';
                document.getElementById('toolDescInput').value = '';
                document.getElementById('toolPriceInput').value = '';
                
                alert("Repair tool published successfully for rental!");
                loadCustomTools();
                switchPostFormTab('asset');
            }

            function loadCustomTools() {
                const container = document.getElementById('toolRentalContainer');
                let tools = JSON.parse(localStorage.getItem('amalaj_custom_tools') || '[]');
                
                let defaultToolsHTML = `
                    <div class="p-5 bg-[#16203a] border border-slate-700/60 rounded-2xl space-y-3 shadow-xl">
                        <div class="flex justify-between items-center">
                            <h3 class="font-bold text-white text-base">UnlockTool Pro</h3>
                            <span class="text-xs bg-amber-500/20 text-amber-400 px-2 py-0.5 rounded-full font-bold">ETB 150 / 3 Hrs</span>
                        </div>
                        <p class="text-xs text-slate-300">FRP bypass, flashing, and Mi Account removal for Samsung & Xiaomi.</p>
                        <button onclick="rentTool('UnlockTool Pro', 150)" class="w-full py-2 bg-amber-500 text-slate-950 font-bold rounded-xl text-xs hover:bg-amber-400 transition cursor-pointer">Rent Tool Now</button>
                    </div>
                    <div class="p-5 bg-[#16203a] border border-slate-700/60 rounded-2xl space-y-3 shadow-xl">
                        <div class="flex justify-between items-center">
                            <h3 class="font-bold text-white text-base">UMT Pro / Ultimate</h3>
                            <span class="text-xs bg-amber-500/20 text-amber-400 px-2 py-0.5 rounded-full font-bold">ETB 120 / 3 Hrs</span>
                        </div>
                        <p class="text-xs text-slate-300">Advanced Qualcomm & MTK servicing, flashing, and network unlocking.</p>
                        <button onclick="rentTool('UMT Pro', 120)" class="w-full py-2 bg-amber-500 text-slate-950 font-bold rounded-xl text-xs hover:bg-amber-400 transition cursor-pointer">Rent Tool Now</button>
                    </div>
                    <div class="p-5 bg-[#16203a] border border-slate-700/60 rounded-2xl space-y-3 shadow-xl">
                        <div class="flex justify-between items-center">
                            <h3 class="font-bold text-white text-base">Pandora Tool</h3>
                            <span class="text-xs bg-amber-500/20 text-amber-400 px-2 py-0.5 rounded-full font-bold">ETB 130 / 3 Hrs</span>
                        </div>
                        <p class="text-xs text-slate-300">Powerful tool for MTK device operations, security backup & bootloader.</p>
                        <button onclick="rentTool('Pandora Tool', 130)" class="w-full py-2 bg-amber-500 text-slate-950 font-bold rounded-xl text-xs hover:bg-amber-400 transition cursor-pointer">Rent Tool Now</button>
                    </div>
                `;

                let customToolsHTML = tools.map(t => `
                    <div class="p-5 bg-[#16203a] border border-slate-700/60 rounded-2xl space-y-3 shadow-xl">
                        <div class="flex justify-between items-center">
                            <h3 class="font-bold text-white text-base">${t.name}</h3>
                            <span class="text-xs bg-amber-500/20 text-amber-400 px-2 py-0.5 rounded-full font-bold">ETB ${t.price} / ${t.duration}</span>
                        </div>
                        <p class="text-xs text-slate-300">${t.desc}</p>
                        <button onclick="rentTool('${t.name}', ${t.price})" class="w-full py-2 bg-amber-500 text-slate-950 font-bold rounded-xl text-xs hover:bg-amber-400 transition cursor-pointer">Rent Tool Now</button>
                    </div>
                `).join('');

                container.innerHTML = defaultToolsHTML + customToolsHTML;
            }

            function showBrowseListings(category) {
                const container = document.getElementById('browseContainer');
                const titleElem = document.getElementById('browseTitle');
                let listings = JSON.parse(localStorage.getItem('amalaj_listings') || '[]');

                if (category === 'ALL') {
                    titleElem.innerText = "All Browse Listings & Categories";
                } else {
                    titleElem.innerText = `Browse Listings: ${category}`;
                }

                let filtered = category === 'ALL' ? listings : listings.filter(item => item.platform && item.platform.toLowerCase().includes(category.toLowerCase()));

                renderListingsGrid(filtered, container);
            }

            function searchListings() {
                const query = document.getElementById('searchInput').value.toLowerCase().trim();
                let listings = JSON.parse(localStorage.getItem('amalaj_listings') || '[]');
                const container = document.getElementById('browseContainer');

                let filtered = listings.filter(item => 
                    (item.title && item.title.toLowerCase().includes(query)) ||
                    (item.platform && item.platform.toLowerCase().includes(query)) ||
                    (item.niche && item.niche.toLowerCase().includes(query))
                );

                renderListingsGrid(filtered, container);
            }

            function renderListingsGrid(listings, container) {
                if (listings.length === 0) {
                    container.innerHTML = `
                        <div class="p-4 bg-slate-900/60 rounded-xl border border-slate-800 text-xs text-slate-400 col-span-full text-center space-y-1">
                            <p>No active listings found matching your search.</p>
                            <p class="text-[10px] text-amber-400">Use the form above to publish your asset ad!</p>
                        </div>
                    `;
                    return;
                }

                container.innerHTML = listings.map(item => `
                    <div class="p-4 bg-slate-900/80 rounded-xl border border-slate-800 space-y-3 shadow-xl">
                        <div class="flex justify-between items-center">
                            <span class="text-amber-400 font-bold uppercase text-[10px]">${item.platform || 'DIGITAL ASSET'}</span>
                            <span class="text-xs bg-emerald-500/20 text-emerald-400 px-2 py-0.5 rounded-full font-bold">🛡️ Escrow Active</span>
                        </div>
                        <h4 class="font-bold text-white text-sm">${item.title || 'Untitled Asset'}</h4>
                        <div class="text-[11px] text-slate-300 space-y-1">
                            <p>Category: <span class="text-amber-300 font-semibold">${item.niche || 'General'}</span></p>
                            <p>Subscribers/Views: <span class="font-semibold text-white">${item.subCount || 'Verified'}</span></p>
                        </div>
                        <div class="flex justify-between items-center pt-2 border-t border-slate-800 text-xs">
                            <span class="font-black text-amber-400">ETB ${item.price}</span>
                            <button onclick="alert('Connecting to seller for ${item.title} via secure Escrow Chat...') " class="px-3 py-1.5 bg-amber-500 text-slate-950 font-bold rounded-lg hover:bg-amber-400 transition cursor-pointer">
                                Buy / Chat
                            </button>
                        </div>
                    </div>
                `).join('');
            }

            function switchDashboardTab(tab) {
                const btnListings = document.getElementById('tabBtnListings');
                const btnRentals = document.getElementById('tabBtnRentals');
                const contentListings = document.getElementById('contentListings');
                const contentRentals = document.getElementById('contentRentals');

                if (tab === 'listings') {
                    btnListings.className = "px-4 py-2 rounded-lg bg-amber-500 text-slate-950 transition cursor-pointer";
                    btnRentals.className = "px-4 py-2 rounded-lg text-slate-300 hover:text-white transition cursor-pointer";
                    contentListings.classList.remove('hidden');
                    contentRentals.classList.add('hidden');
                } else {
                    btnRentals.className = "px-4 py-2 rounded-lg bg-amber-500 text-slate-950 transition cursor-pointer";
                    btnListings.className = "px-4 py-2 rounded-lg text-slate-300 hover:text-white transition cursor-pointer";
                    contentRentals.classList.remove('hidden');
                    contentListings.classList.add('hidden');
                }
            }

            function loadUserListings() {
                const container = document.getElementById('userListingsContainer');
                let listings = JSON.parse(localStorage.getItem('amalaj_listings') || '[]');
                if (listings.length === 0) {
                    container.innerHTML = `<div class="p-4 bg-slate-900/60 rounded-xl border border-slate-800 text-xs text-slate-400 flex justify-between items-center"><span>No active listings yet. Use the form above to add one!</span><span class="text-emerald-400 font-semibold">Escrow Ready</span></div>`;
                    return;
                }
                container.innerHTML = listings.map(item => `
                    <div class="p-4 bg-slate-900/80 rounded-xl border border-slate-800 flex justify-between items-center text-xs">
                        <div>
                            <span class="text-amber-400 font-bold uppercase text-[10px]">${item.platform || 'DIGITAL ASSET'} (${item.niche || 'General'})</span>
                            <h4 class="font-bold text-white text-sm mt-0.5">${item.title || 'Untitled Asset'}</h4>
                        </div>
                        <div class="text-right">
                            <span class="font-extrabold text-emerald-400 text-sm">ETB ${item.price}</span>
                            <p class="text-[10px] text-emerald-500 mt-0.5"><i class="fa-solid fa-shield-halved"></i> Escrow Secured</p>
                        </div>
                    </div>
                `).join('');
            }

            function rentTool(toolName, price) {
                let rentals = JSON.parse(localStorage.getItem('amalaj_rentals') || '[]');
                rentals.push({ name: toolName, price: price, time: '3 Hours Active' });
                localStorage.setItem('amalaj_rentals', JSON.stringify(rentals));
                alert(`${toolName} rented successfully! Access granted via secure server.`);
                loadUserRentals();
                switchDashboardTab('rentals');
            }

            function loadUserRentals() {
                const container = document.getElementById('userRentalsContainer');
                let rentals = JSON.parse(localStorage.getItem('amalaj_rentals') || '[]');
                if (rentals.length === 0) {
                    container.innerHTML = `<div class="p-4 bg-slate-900/60 rounded-xl border border-slate-800 text-xs text-slate-400 flex justify-between items-center"><span>No active tool rentals. Choose a tool below to rent instantly.</span><span class="text-amber-400 font-semibold">Available 24/7</span></div>`;
                    return;
                }
                container.innerHTML = rentals.map(item => `
                    <div class="p-4 bg-slate-900/80 rounded-xl border border-slate-800 flex justify-between items-center text-xs">
                        <div>
                            <span class="text-amber-400 font-bold text-[10px]">SOFTWARE TOOL RENTAL</span>
                            <h4 class="font-bold text-white text-sm mt-0.5">${item.name}</h4>
                        </div>
                        <div class="text-right">
                            <span class="font-extrabold text-amber-400 text-sm">ETB ${item.price}</span>
                            <p class="text-[10px] text-emerald-400 mt-0.5"><i class="fa-solid fa-circle-check"></i> ${item.time}</p>
                        </div>
                    </div>
                `).join('');
            }

            function updateNavbarUser(name) {
                const navActions = document.getElementById('navUserActions');
                navActions.innerHTML = `
                    <div class="flex items-center space-x-3 bg-slate-800/80 border border-slate-700 px-3 py-1.5 rounded-xl">
                        <div class="w-8 h-8 rounded-full bg-amber-500 text-slate-950 font-bold flex items-center justify-center text-xs">
                            ${name.charAt(0).toUpperCase()}
                        </div>
                        <span class="text-xs font-semibold text-white">${name}</span>
                        <button onclick="logoutUser()" class="text-slate-400 hover:text-red-400 text-xs ml-2 cursor-pointer" title="Logout">
                            <i class="fa-solid fa-right-from-bracket"></i>
                        </button>
                    </div>
                `;
            }

            function logoutUser() {
                localStorage.removeItem('amalaj_user');
                location.reload();
            }
        </script>
    </body>
    </html>
    """