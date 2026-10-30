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

                    <!-- Navigation Links -->
                    <div class="hidden md:flex items-center space-x-6 text-sm font-medium text-slate-300">
                        <a href="#marketplace" class="hover:text-amber-400 transition py-2">Digital Marketplace</a>
                        <a href="#toolRental" class="text-amber-400 font-semibold hover:underline py-2 flex items-center gap-1">Tool Rental ⚡</a>
                        <a href="#dashboardSection" class="hover:text-amber-400 transition py-2">Dashboard</a>
                    </div>

                    <!-- Right Actions -->
                    <div id="navUserActions" class="flex items-center space-x-3">
                        <button onclick="openAuthModal()" class="bg-amber-500 hover:bg-amber-400 text-slate-950 font-bold px-4 py-2 rounded-xl transition shadow-md cursor-pointer text-xs">
                            Sign In / Register
                        </button>
                    </div>
                </div>
            </header>

            <!-- Main Layout -->
            <div class="max-w-7xl mx-auto px-6 py-8 grid grid-cols-1 lg:grid-cols-12 gap-8">
                
                <!-- Sidebar -->
                <div class="lg:col-span-3 space-y-2">
                    <div class="bg-[#16203a] border border-slate-700/60 rounded-2xl p-4 shadow-xl space-y-1">
                        <a href="#dashboardSection" onclick="switchTab('dashboard')" id="sideBtnDashboard" class="flex items-center space-x-3 px-3 py-2.5 rounded-xl bg-amber-500 text-slate-950 font-bold text-xs transition cursor-pointer">
                            <i class="fa-solid fa-chart-pie w-5"></i>
                            <span>Dashboard</span>
                        </a>
                        <a href="#dashboardSection" onclick="switchTab('listings')" id="sideBtnListings" class="flex items-center space-x-3 px-3 py-2.5 rounded-xl text-slate-300 hover:bg-slate-800 hover:text-white font-medium text-xs transition cursor-pointer">
                            <i class="fa-solid fa-store w-5"></i>
                            <span>My Listings</span>
                        </a>
                        <a href="#dashboardSection" onclick="switchTab('rentals')" id="sideBtnRentals" class="flex items-center space-x-3 px-3 py-2.5 rounded-xl text-slate-300 hover:bg-slate-800 hover:text-white font-medium text-xs transition cursor-pointer">
                            <i class="fa-solid fa-bolt w-5"></i>
                            <span>Software Rentals</span>
                        </a>
                        <a href="#conductModal" onclick="openConductModal()" class="flex items-center space-x-3 px-3 py-2.5 rounded-xl text-slate-300 hover:bg-slate-800 hover:text-white font-medium text-xs transition cursor-pointer">
                            <i class="fa-solid fa-shield-halved w-5"></i>
                            <span>Code of Conduct</span>
                        </a>
                    </div>

                    <!-- Quick Help Card -->
                    <div class="bg-[#16203a] border border-slate-700/60 rounded-2xl p-4 shadow-xl space-y-2 text-xs">
                        <h4 class="font-bold text-white flex items-center gap-2">
                            <i class="fa-solid fa-headset text-amber-400"></i> Need Assistance?
                        </h4>
                        <p class="text-slate-400">Contact our admin team instantly via Telegram for secure deals.</p>
                        <a href="https://t.me/" target="_blank" class="block text-center py-2 bg-[#229ED9] hover:bg-[#1d8ebf] text-white font-bold rounded-xl transition">
                            Telegram Support
                        </a>
                    </div>
                </div>

                <!-- Content Area -->
                <div id="dashboardSection" class="lg:col-span-9 space-y-6">
                    
                    <!-- Dashboard Overview Tab -->
                    <div id="tabContentDashboard" class="space-y-6">
                        <div class="bg-[#1c2541] border border-slate-700/60 rounded-2xl p-6 shadow-xl space-y-4">
                            <div class="flex justify-between items-center">
                                <h3 class="text-lg font-bold text-white">Welcome back, <span id="welcomeUserName" class="text-amber-400">Trader</span>!</h3>
                                <span class="text-xs bg-emerald-500/20 text-emerald-400 px-3 py-1 rounded-full font-bold">100% Escrow Secured</span>
                            </div>
                            
                            <!-- Stats Grid -->
                            <div class="grid grid-cols-2 md:grid-cols-4 gap-4 pt-2">
                                <div class="bg-slate-900/80 border border-slate-800 p-4 rounded-xl text-center">
                                    <span class="text-xs text-slate-400">Active Listings</span>
                                    <h4 id="statListingsCount" class="text-2xl font-black text-white mt-1">0</h4>
                                </div>
                                <div class="bg-slate-900/80 border border-slate-800 p-4 rounded-xl text-center">
                                    <span class="text-xs text-slate-400">Tool Rentals</span>
                                    <h4 id="statRentalsCount" class="text-2xl font-black text-amber-400 mt-1">0</h4>
                                </div>
                                <div class="bg-slate-900/80 border border-slate-800 p-4 rounded-xl text-center">
                                    <span class="text-xs text-slate-400">Escrow Status</span>
                                    <h4 class="text-lg font-bold text-emerald-400 mt-1"><i class="fa-solid fa-shield-check"></i> Safe</h4>
                                </div>
                                <div class="bg-slate-900/80 border border-slate-800 p-4 rounded-xl text-center">
                                    <span class="text-xs text-slate-400">Market Rating</span>
                                    <h4 class="text-2xl font-black text-amber-400 mt-1">5.0 ★</h4>
                                </div>
                            </div>
                        </div>

                        <!-- Professional Listing Form (Fameswap/Acquire Style) -->
                        <div class="bg-[#16203a] border border-slate-700/60 rounded-2xl p-6 shadow-xl space-y-4">
                            <div class="flex justify-between items-center border-b border-slate-800 pb-3">
                                <h3 class="font-bold text-white text-sm">Post New Digital Asset or Software Rental</h3>
                                <button onclick="openConductModal()" class="text-xs text-amber-400 font-bold hover:underline cursor-pointer">Code of Conduct ⓘ</button>
                            </div>
                            <form onsubmit="handlePostListing(event)" class="space-y-4 text-xs">
                                <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
                                    <div>
                                        <label class="block text-slate-300 font-semibold mb-1">Listing Type</label>
                                        <select id="listingType" class="w-full bg-slate-900 border border-slate-700 rounded-xl px-3 py-2.5 text-white focus:outline-none focus:border-amber-500">
                                            <option value="Digital Asset">Digital Asset (Telegram / TikTok / YouTube)</option>
                                            <option value="Software Rental">Mobile Repair Tool Rental</option>
                                        </select>
                                    </div>
                                    <div>
                                        <label class="block text-slate-300 font-semibold mb-1">Asset Name / Channel Username</label>
                                        <input type="text" id="listingTitle" required placeholder="e.g., @TechChannelEthiopia" class="w-full bg-slate-900 border border-slate-700 rounded-xl px-3 py-2.5 text-white focus:outline-none focus:border-amber-500">
                                    </div>
                                </div>
                                <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
                                    <div>
                                        <label class="block text-slate-300 font-semibold mb-1">Asking Price (ETB)</label>
                                        <input type="number" id="listingPrice" required placeholder="e.g., 3500" class="w-full bg-slate-900 border border-slate-700 rounded-xl px-3 py-2.5 text-white focus:outline-none focus:border-amber-500">
                                    </div>
                                    <div>
                                        <label class="block text-slate-300 font-semibold mb-1">Description / Details</label>
                                        <input type="text" id="listingDesc" required placeholder="e.g., 50k active members, monetized." class="w-full bg-slate-900 border border-slate-700 rounded-xl px-3 py-2.5 text-white focus:outline-none focus:border-amber-500">
                                    </div>
                                </div>
                                <button type="submit" class="w-full py-3 bg-amber-500 text-slate-950 font-bold rounded-xl hover:bg-amber-400 transition cursor-pointer text-sm shadow-md">
                                    Publish Listing with Escrow Protection &rarr;
                                </button>
                            </form>
                        </div>
                    </div>

                    <!-- Listings Tab Content -->
                    <div id="tabContentListings" class="hidden space-y-4">
                        <div class="bg-[#16203a] border border-slate-700/60 rounded-2xl p-6 shadow-xl space-y-4">
                            <h3 class="font-bold text-white text-sm">Your Posted Digital Assets</h3>
                            <div id="userListingsContainer" class="space-y-3">
                                <div class="p-4 bg-slate-900/60 rounded-xl border border-slate-800 text-xs text-slate-400 flex justify-between items-center">
                                    <span>No active listings yet.</span>
                                    <span class="text-emerald-400 font-semibold">Escrow Secured</span>
                                </div>
                            </div>
                        </div>
                    </div>

                    <!-- Rentals Tab Content -->
                    <div id="tabContentRentals" class="hidden space-y-4">
                        <div class="bg-[#16203a] border border-slate-700/60 rounded-2xl p-6 shadow-xl space-y-4">
                            <h3 class="font-bold text-white text-sm">Your Active Software Rentals</h3>
                            <div id="userRentalsContainer" class="space-y-3">
                                <div class="p-4 bg-slate-900/60 rounded-xl border border-slate-800 text-xs text-slate-400 flex justify-between items-center">
                                    <span>No active software rentals.</span>
                                    <span class="text-amber-400 font-semibold">24/7 Available</span>
                                </div>
                            </div>
                        </div>
                    </div>

                </div>
            </div>

            <!-- Marketplace Categories -->
            <section id="marketplace" class="max-w-7xl mx-auto px-6 py-10 border-t border-slate-800">
                <div class="mb-8">
                    <h2 class="text-2xl font-black text-white tracking-tight">Digital Assets Marketplace</h2>
                    <p class="text-slate-400 text-xs mt-1">Explore verified Telegram channels, TikTok, YouTube, and Facebook accounts.</p>
                </div>
                <div class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-4 gap-6">
                    <div class="p-5 bg-[#16203a] border border-slate-700/60 rounded-2xl hover:border-[#229ED9] transition shadow-xl space-y-3">
                        <div class="w-10 h-10 rounded-xl bg-[#229ED9]/20 text-[#229ED9] flex items-center justify-center text-xl"><i class="fa-brands fa-telegram"></i></div>
                        <h3 class="font-bold text-white text-base">Telegram Channels</h3>
                        <p class="text-xs text-slate-400">Verified members & active engagement groups.</p>
                        <button onclick="alert('Viewing Telegram listings... Escrow protected!')" class="w-full py-2 bg-slate-900 hover:bg-slate-800 text-amber-400 font-bold rounded-xl text-xs border border-slate-700 transition cursor-pointer">Browse Listings</button>
                    </div>
                    <div class="p-5 bg-[#16203a] border border-slate-700/60 rounded-2xl hover:border-[#EE1D52] transition shadow-xl space-y-3">
                        <div class="w-10 h-10 rounded-xl bg-[#EE1D52]/20 text-[#EE1D52] flex items-center justify-center text-xl"><i class="fa-brands fa-tiktok"></i></div>
                        <h3 class="font-bold text-white text-base">TikTok Accounts</h3>
                        <p class="text-xs text-slate-400">Monetized & live-enabled creator accounts.</p>
                        <button onclick="alert('Viewing TikTok listings... Escrow protected!')" class="w-full py-2 bg-slate-900 hover:bg-slate-800 text-amber-400 font-bold rounded-xl text-xs border border-slate-700 transition cursor-pointer">Browse Listings</button>
                    </div>
                    <div class="p-5 bg-[#16203a] border border-slate-700/60 rounded-2xl hover:border-[#FF0000] transition shadow-xl space-y-3">
                        <div class="w-10 h-10 rounded-xl bg-[#FF0000]/20 text-[#FF0000] flex items-center justify-center text-xl"><i class="fa-brands fa-youtube"></i></div>
                        <h3 class="font-bold text-white text-base">YouTube Channels</h3>
                        <p class="text-xs text-slate-400">Ready monetization channels with subscribers.</p>
                        <button onclick="alert('Viewing YouTube listings... Escrow protected!')" class="w-full py-2 bg-slate-900 hover:bg-slate-800 text-amber-400 font-bold rounded-xl text-xs border border-slate-700 transition cursor-pointer">Browse Listings</button>
                    </div>
                    <div class="p-5 bg-[#16203a] border border-slate-700/60 rounded-2xl hover:border-[#1877F2] transition shadow-xl space-y-3">
                        <div class="w-10 h-10 rounded-xl bg-[#1877F2]/20 text-[#1877F2] flex items-center justify-center text-xl"><i class="fa-brands fa-facebook"></i></div>
                        <h3 class="font-bold text-white text-base">Facebook Pages</h3>
                        <p class="text-xs text-slate-400">Active community pages and business groups.</p>
                        <button onclick="alert('Viewing Facebook listings... Escrow protected!')" class="w-full py-2 bg-slate-900 hover:bg-slate-800 text-amber-400 font-bold rounded-xl text-xs border border-slate-700 transition cursor-pointer">Browse Listings</button>
                    </div>
                </div>
            </section>

            <!-- Tool Rental Section -->
            <section id="toolRental" class="max-w-7xl mx-auto px-6 py-10 border-t border-slate-800 mb-16">
                <div class="mb-8">
                    <span class="text-xs text-amber-400 font-bold uppercase tracking-wider">For Technicians</span>
                    <h2 class="text-2xl font-black text-white tracking-tight mt-1">Mobile Repair Software Tool Rentals ⚡</h2>
                    <p class="text-slate-400 text-xs mt-1">Rent professional flashing and unlocking software tools instantly.</p>
                </div>
                <div class="grid grid-cols-1 md:grid-cols-3 gap-6">
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
        </div>

        <!-- Code of Conduct Modal -->
        <div id="conductModal" class="fixed inset-0 bg-black/80 backdrop-blur-sm z-50 hidden flex items-center justify-center p-4">
            <div class="bg-[#1c2541] border border-slate-700 rounded-3xl max-w-lg w-full p-8 relative shadow-2xl space-y-6">
                <button onclick="closeConductModal()" class="absolute top-5 right-5 text-slate-400 hover:text-white text-xl cursor-pointer">
                    <i class="fa-solid fa-xmark"></i>
                </button>
                <div class="text-center space-y-2">
                    <div class="w-12 h-12 bg-amber-500/20 text-amber-400 rounded-2xl flex items-center justify-center mx-auto text-xl font-bold">
                        <i class="fa-solid fa-handshake"></i>
                    </div>
                    <h3 class="text-xl font-black text-white">Great relationships start here</h3>
                    <p class="text-xs text-slate-300">Please commit to our Code of Conduct to help build a fair and trusted community[cite: 12].</p>
                </div>
                <div class="grid grid-cols-3 gap-3 text-center text-xs">
                    <div class="bg-slate-900/80 p-4 rounded-2xl border border-slate-800 space-y-2">
                        <i class="fa-solid fa-briefcase text-amber-400 text-lg"></i>
                        <h4 class="font-bold text-white">Be professional</h4>
                    </div>
                    <div class="bg-slate-900/80 p-4 rounded-2xl border border-slate-800 space-y-2">
                        <i class="fa-solid fa-hand-holding-heart text-emerald-400 text-lg"></i>
                        <h4 class="font-bold text-white">Stay honest</h4>
                    </div>
                    <div class="bg-slate-900/80 p-4 rounded-2xl border border-slate-800 space-y-2">
                        <i class="fa-solid fa-shield-virus text-red-400 text-lg"></i>
                        <h4 class="font-bold text-white">Don't spam</h4>
                    </div>
                </div>
                <button onclick="closeConductModal()" class="w-full bg-amber-500 hover:bg-amber-400 text-slate-950 font-bold py-3 rounded-xl transition text-sm cursor-pointer">
                    OK, got it
                </button>
            </div>
        </div>

        <!-- Authentication Modal -->
        <div id="authModal" class="fixed inset-0 bg-black/80 backdrop-blur-sm z-50 hidden flex items-center justify-center p-4">
            <div class="bg-[#1c2541] border border-slate-700 rounded-3xl max-w-md w-full p-8 relative shadow-2xl space-y-6">
                <button onclick="closeAuthModal()" class="absolute top-5 right-5 text-slate-400 hover:text-white text-xl cursor-pointer">
                    <i class="fa-solid fa-xmark"></i>
                </button>
                <div class="text-center space-y-1">
                    <h3 class="text-2xl font-black text-white">Sign In or Register</h3>
                    <p class="text-xs text-slate-400">Amalaj Plus Marketplace</p>
                </div>
                <button onclick="handleGoogleAuth()" class="w-full bg-white hover:bg-slate-100 text-slate-900 font-bold py-3 px-4 rounded-xl flex items-center justify-center space-x-3 transition shadow-lg text-sm cursor-pointer">
                    <i class="fa-brands fa-google text-red-500 text-lg"></i>
                    <span>Sign in with Google</span>
                </button>
                <div class="relative flex py-1 items-center">
                    <div class="flex-grow border-t border-slate-700"></div>
                    <span class="flex-shrink mx-4 text-xs text-slate-500 uppercase">Or Username</span>
                    <div class="flex-grow border-t border-slate-700"></div>
                </div>
                <form onsubmit="handleLoginSubmit(event)" class="space-y-4">
                    <div>
                        <label class="block text-xs font-semibold text-slate-300 mb-1">Username / Email</label>
                        <input type="text" id="loginUsername" required placeholder="hailu_trader" class="w-full bg-slate-900 border border-slate-700 rounded-xl px-4 py-2.5 text-sm text-white focus:outline-none focus:border-amber-500">
                    </div>
                    <div>
                        <label class="block text-xs font-semibold text-slate-300 mb-1">Password</label>
                        <input type="password" id="loginPassword" required placeholder="••••••••" class="w-full bg-slate-900 border border-slate-700 rounded-xl px-4 py-2.5 text-sm text-white focus:outline-none focus:border-amber-500">
                    </div>
                    <button type="submit" class="w-full bg-amber-500 hover:bg-amber-400 text-slate-950 font-bold py-3 rounded-xl transition text-sm shadow-md cursor-pointer">
                        Access Dashboard
                    </button>
                </form>
            </div>
        </div>

        <!-- JavaScript Logic -->
        <script>
            window.onload = function() {
                const savedUser = localStorage.getItem('amalaj_user');
                if (savedUser) {
                    updateUserSession(savedUser);
                }
                loadUserListings();
                loadUserRentals();
            };

            function switchTab(tab) {
                const btnDash = document.getElementById('sideBtnDashboard');
                const btnListings = document.getElementById('sideBtnListings');
                const btnRentals = document.getElementById('sideBtnRentals');
                
                const contentDash = document.getElementById('tabContentDashboard');
                const contentListings = document.getElementById('tabContentListings');
                const contentRentals = document.getElementById('tabContentRentals');

                // Reset
                btnDash.className = "flex items-center space-x-3 px-3 py-2.5 rounded-xl text-slate-300 hover:bg-slate-800 hover:text-white font-medium text-xs transition cursor-pointer";
                btnListings.className = "flex items-center space-x-3 px-3 py-2.5 rounded-xl text-slate-300 hover:bg-slate-800 hover:text-white font-medium text-xs transition cursor-pointer";
                btnRentals.className = "flex items-center space-x-3 px-3 py-2.5 rounded-xl text-slate-300 hover:bg-slate-800 hover:text-white font-medium text-xs transition cursor-pointer";
                
                contentDash.classList.add('hidden');
                contentListings.classList.add('hidden');
                contentRentals.classList.add('hidden');

                if (tab === 'dashboard') {
                    btnDash.className = "flex items-center space-x-3 px-3 py-2.5 rounded-xl bg-amber-500 text-slate-950 font-bold text-xs transition cursor-pointer";
                    contentDash.classList.remove('hidden');
                } else if (tab === 'listings') {
                    btnListings.className = "flex items-center space-x-3 px-3 py-2.5 rounded-xl bg-amber-500 text-slate-950 font-bold text-xs transition cursor-pointer";
                    contentListings.classList.remove('hidden');
                } else if (tab === 'rentals') {
                    btnRentals.className = "flex items-center space-x-3 px-3 py-2.5 rounded-xl bg-amber-500 text-slate-950 font-bold text-xs transition cursor-pointer";
                    contentRentals.classList.remove('hidden');
                }
            }

            function openConductModal() {
                document.getElementById('conductModal').classList.remove('hidden');
            }

            function closeConductModal() {
                document.getElementById('conductModal').classList.add('hidden');
            }

            function handlePostListing(e) {
                e.preventDefault();
                const type = document.getElementById('listingType').value;
                const title = document.getElementById('listingTitle').value.trim();
                const price = document.getElementById('listingPrice').value.trim();
                const desc = document.getElementById('listingDesc').value.trim();

                if (!title || !price) return;

                let listings = JSON.parse(localStorage.getItem('amalaj_listings') || '[]');
                listings.push({ type, title, price, desc, date: new Date().toLocaleDateString() });
                localStorage.setItem('amalaj_listings', JSON.stringify(listings));

                document.getElementById('listingTitle').value = '';
                document.getElementById('listingPrice').value = '';
                document.getElementById('listingDesc').value = '';
                alert("Listing published successfully with Escrow protection!");
                loadUserListings();
                switchTab('listings');
            }

            function loadUserListings() {
                const container = document.getElementById('userListingsContainer');
                let listings = JSON.parse(localStorage.getItem('amalaj_listings') || '[]');
                document.getElementById('statListingsCount').innerText = listings.length;
                
                if (listings.length === 0) {
                    container.innerHTML = `<div class="p-4 bg-slate-900/60 rounded-xl border border-slate-800 text-xs text-slate-400 flex justify-between items-center"><span>No active listings yet.</span><span class="text-emerald-400 font-semibold">Escrow Secured</span></div>`;
                    return;
                }
                container.innerHTML = listings.map(item => `
                    <div class="p-4 bg-slate-900/80 rounded-xl border border-slate-800 flex justify-between items-center text-xs">
                        <div>
                            <span class="text-amber-400 font-bold uppercase text-[10px]">${item.type}</span>
                            <h4 class="font-bold text-white text-sm mt-0.5">${item.title}</h4>
                            <p class="text-slate-400 text-[11px] mt-0.5">${item.desc}</p>
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
                document.getElementById('statRentalsCount').innerText = rentals.length;
                alert(`${toolName} rented successfully! Access granted.`);
                loadUserRentals();
                switchTab('rentals');
            }

            function loadUserRentals() {
                const container = document.getElementById('userRentalsContainer');
                let rentals = JSON.parse(localStorage.getItem('amalaj_rentals') || '[]');
                document.getElementById('statRentalsCount').innerText = rentals.length;

                if (rentals.length === 0) {
                    container.innerHTML = `<div class="p-4 bg-slate-900/60 rounded-xl border border-slate-800 text-xs text-slate-400 flex justify-between items-center"><span>No active software rentals.</span><span class="text-amber-400 font-semibold">24/7 Available</span></div>`;
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

            function openAuthModal() {
                document.getElementById('authModal').classList.remove('hidden');
            }

            function closeAuthModal() {
                document.getElementById('authModal').classList.add('hidden');
            }

            function handleGoogleAuth() {
                window.location.href = "/auth/google";
            }

            function handleLoginSubmit(e) {
                e.preventDefault();
                const username = document.getElementById('loginUsername').value.trim();
                if (!username) return;
                localStorage.setItem('amalaj_user', username);
                alert("Login successful!");
                closeAuthModal();
                updateUserSession(username);
            }

            function updateUserSession(username) {
                document.getElementById('welcomeUserName').innerText = username;
                const navActions = document.getElementById('navUserActions');
                navActions.innerHTML = `
                    <div class="flex items-center space-x-3 bg-slate-800/80 border border-slate-700 px-3 py-1.5 rounded-xl">
                        <div class="w-8 h-8 rounded-full bg-amber-500 text-slate-950 font-bold flex items-center justify-center text-xs">
                            ${username.charAt(0).toUpperCase()}
                        </div>
                        <span class="text-xs font-semibold text-white">${username}</span>
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