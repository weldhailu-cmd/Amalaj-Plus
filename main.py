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
                        <a href="#" class="hover:text-amber-400 transition py-2">Home</a>
                        <a href="#marketplace" class="hover:text-amber-400 transition py-2">Digital Marketplace</a>
                        <a href="#toolRental" class="text-amber-400 font-semibold hover:underline py-2 flex items-center gap-1">Tool Rental ⚡</a>
                        <a href="#dashboardSection" class="hover:text-amber-400 transition py-2">My Dashboard</a>
                    </div>

                    <!-- Right Actions: Sign In / Sign Up -->
                    <div id="navUserActions" class="flex items-center space-x-3">
                        <button onclick="openAuthModal('signin')" class="flex items-center space-x-2 bg-amber-500 hover:bg-amber-400 text-slate-950 font-bold px-4 py-2 rounded-xl transition shadow-md cursor-pointer text-xs">
                            <i class="fa-brands fa-google"></i>
                            <span>Sign In</span>
                        </button>
                        <button onclick="openAuthModal('signup')" class="bg-slate-800 hover:bg-slate-700 text-white font-bold px-4 py-2 rounded-xl transition text-xs border border-slate-700 cursor-pointer">
                            Sign Up
                        </button>
                    </div>
                </div>
            </header>

            <!-- Hero / About Section with Post Ad Form on Right -->
            <section class="max-w-7xl mx-auto px-6 py-12">
                <div class="grid lg:grid-cols-12 gap-12 items-center">
                    <div class="lg:col-span-7 space-y-6">
                        <div class="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-amber-500/10 border border-amber-500/30 text-amber-400 text-xs font-semibold">
                            <span>🛡️ Secure Escrow Protected Ethiopian Marketplace</span>
                        </div>
                        <h1 class="text-4xl md:text-5xl font-black tracking-tight text-white leading-tight">
                            Buy & Sell Digital Assets & <span class="text-amber-400">Rent Mobile Repair Tools</span> Securely.
                        </h1>
                        <p class="text-sm md:text-base text-slate-300 max-w-xl leading-relaxed">
                            Amalaj Plus is a trusted platform to buy and sell verified Telegram channels, TikTok accounts, and rent professional mobile repair software tools backed by safe escrow protection.
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

                    <!-- Post New Asset or Tool Form (Restored properly on right side) -->
                    <div class="lg:col-span-5">
                        <div class="bg-[#1c2541] border border-slate-700/60 rounded-3xl p-6 shadow-2xl space-y-4">
                            <div class="flex justify-between items-center pb-3 border-b border-slate-800">
                                <h3 class="text-base font-bold text-white">Post New Asset or Tool</h3>
                                <button onclick="openConductModal()" class="text-xs text-amber-400 font-bold hover:underline cursor-pointer">Code of Conduct ⓘ</button>
                            </div>
                            <form onsubmit="handlePostListing(event)" class="space-y-3 text-xs">
                                <div>
                                    <label class="block text-slate-300 font-semibold mb-1">Listing Type</label>
                                    <select id="listingType" class="w-full bg-slate-900 border border-slate-700 rounded-xl px-3 py-2 text-white focus:outline-none focus:border-amber-500">
                                        <option value="Telegram Channel">Telegram Channel</option>
                                        <option value="TikTok Account">TikTok Account</option>
                                        <option value="YouTube Channel">YouTube Channel</option>
                                        <option value="Facebook Page">Facebook Page</option>
                                    </select>
                                </div>
                                <div>
                                    <label class="block text-slate-300 font-semibold mb-1">Channel / Username</label>
                                    <input type="text" id="listingTitle" required placeholder="e.g., @TechChannelEthiopia" class="w-full bg-slate-900 border border-slate-700 rounded-xl px-3 py-2 text-white focus:outline-none focus:border-amber-500">
                                </div>
                                <div>
                                    <label class="block text-slate-300 font-semibold mb-1">Price (ETB)</label>
                                    <input type="number" id="listingPrice" required placeholder="e.g., 2500" class="w-full bg-slate-900 border border-slate-700 rounded-xl px-3 py-2 text-white focus:outline-none focus:border-amber-500">
                                </div>
                                <button type="submit" class="w-full py-2.5 bg-amber-500 text-slate-950 font-bold rounded-xl hover:bg-amber-400 transition cursor-pointer">
                                    Publish to Marketplace &rarr;
                                </button>
                            </form>
                        </div>
                    </div>
                </div>
            </section>

            <!-- Digital Asset Categories Marketplace -->
            <section id="marketplace" class="max-w-7xl mx-auto px-6 py-10 border-t border-slate-800">
                <div class="flex justify-between items-center mb-8">
                    <div>
                        <h2 class="text-2xl font-black text-white tracking-tight">Digital Assets Marketplace</h2>
                        <p class="text-slate-400 text-xs mt-1">Explore verified Telegram channels, TikTok, YouTube & Facebook accounts.</p>
                    </div>
                    <button onclick="showBrowseListings('ALL')" class="px-4 py-2 bg-amber-500 hover:bg-amber-400 text-slate-950 font-bold rounded-xl text-xs transition cursor-pointer shadow-md">
                        Browse All Listings 🌐
                    </button>
                </div>
                
                <!-- 4 Main Platform Cards -->
                <div class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-4 gap-6 mb-8">
                    <div class="p-5 bg-[#16203a] border border-slate-700/60 rounded-2xl hover:border-[#229ED9] transition shadow-xl space-y-3">
                        <div class="w-10 h-10 rounded-xl bg-[#229ED9]/20 text-[#229ED9] flex items-center justify-center text-xl"><i class="fa-brands fa-telegram"></i></div>
                        <h3 class="font-bold text-white text-base">Telegram Channels</h3>
                        <p class="text-xs text-slate-400">Verified members & high engagement groups.</p>
                        <button onclick="showBrowseListings('Telegram Channel')" class="w-full py-2 bg-slate-900 hover:bg-slate-800 text-amber-400 font-bold rounded-xl text-xs border border-slate-700 transition cursor-pointer">Browse Listings</button>
                    </div>
                    <div class="p-5 bg-[#16203a] border border-slate-700/60 rounded-2xl hover:border-[#EE1D52] transition shadow-xl space-y-3">
                        <div class="w-10 h-10 rounded-xl bg-[#EE1D52]/20 text-[#EE1D52] flex items-center justify-center text-xl"><i class="fa-brands fa-tiktok"></i></div>
                        <h3 class="font-bold text-white text-base">TikTok Accounts</h3>
                        <p class="text-xs text-slate-400">Monetized & live-enabled creator accounts.</p>
                        <button onclick="showBrowseListings('TikTok Account')" class="w-full py-2 bg-slate-900 hover:bg-slate-800 text-amber-400 font-bold rounded-xl text-xs border border-slate-700 transition cursor-pointer">Browse Listings</button>
                    </div>
                    <div class="p-5 bg-[#16203a] border border-slate-700/60 rounded-2xl hover:border-[#FF0000] transition shadow-xl space-y-3">
                        <div class="w-10 h-10 rounded-xl bg-[#FF0000]/20 text-[#FF0000] flex items-center justify-center text-xl"><i class="fa-brands fa-youtube"></i></div>
                        <h3 class="font-bold text-white text-base">YouTube Channels</h3>
                        <p class="text-xs text-slate-400">Ready monetization channels with subscribers.</p>
                        <button onclick="showBrowseListings('YouTube Channel')" class="w-full py-2 bg-slate-900 hover:bg-slate-800 text-amber-400 font-bold rounded-xl text-xs border border-slate-700 transition cursor-pointer">Browse Listings</button>
                    </div>
                    <div class="p-5 bg-[#16203a] border border-slate-700/60 rounded-2xl hover:border-[#1877F2] transition shadow-xl space-y-3">
                        <div class="w-10 h-10 rounded-xl bg-[#1877F2]/20 text-[#1877F2] flex items-center justify-center text-xl"><i class="fa-brands fa-facebook"></i></div>
                        <h3 class="font-bold text-white text-base">Facebook Pages</h3>
                        <p class="text-xs text-slate-400">Active community pages and groups.</p>
                        <button onclick="showBrowseListings('Facebook Page')" class="w-full py-2 bg-slate-900 hover:bg-slate-800 text-amber-400 font-bold rounded-xl text-xs border border-slate-700 transition cursor-pointer">Browse Listings</button>
                    </div>
                </div>

                <!-- Dynamic Browse Listings Container -->
                <div id="browseListingsSection" class="bg-[#16203a] border border-slate-700/60 rounded-2xl p-6 shadow-2xl space-y-4">
                    <div class="flex justify-between items-center pb-3 border-b border-slate-800">
                        <h3 id="browseTitle" class="font-bold text-white text-base">Browse Listings & Categories</h3>
                        <span class="text-xs text-amber-400 font-bold">🛡️ Escrow Protected Market</span>
                    </div>
                    <div id="browseContainer" class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
                        <div class="p-4 bg-slate-900/60 rounded-xl border border-slate-800 text-xs text-slate-400 col-span-full text-center">
                            Click on any "Browse Listings" button above or "Browse All Listings" to view active digital assets.
                        </div>
                    </div>
                </div>
            </section>

            <!-- Tool Rental Section -->
            <section id="toolRental" class="max-w-7xl mx-auto px-6 py-10 border-t border-slate-800">
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

        <!-- Telegram Direct Support Floating Widget -->
        <a href="https://t.me/" target="_blank" class="fixed bottom-6 right-6 bg-[#229ED9] hover:bg-[#1d8ebf] text-white w-14 h-14 rounded-full flex items-center justify-center shadow-2xl z-50 transition transform hover:scale-105 cursor-pointer" title="Contact Support on Telegram">
            <i class="fa-brands fa-telegram text-2xl"></i>
        </a>

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
                    <p class="text-xs text-slate-300">Please commit to our Code of Conduct to help build a fair and trusted community.</p>
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
                    <h3 id="modalTitle" class="text-2xl font-black text-white">Create Account</h3>
                    <p id="modalSubtitle" class="text-xs text-slate-400">Join Amalaj Plus Universal Marketplace</p>
                </div>
                <button onclick="handleGoogleAuth()" class="w-full bg-white hover:bg-slate-100 text-slate-900 font-bold py-3 px-4 rounded-xl flex items-center justify-center space-x-3 transition shadow-lg text-sm cursor-pointer">
                    <i class="fa-brands fa-google text-red-500 text-lg"></i>
                    <span>Sign in with Google</span>
                </button>
                <div class="relative flex py-1 items-center">
                    <div class="flex-grow border-t border-slate-700"></div>
                    <span class="flex-shrink mx-4 text-xs text-slate-500 uppercase">Or</span>
                    <div class="flex-grow border-t border-slate-700"></div>
                </div>
                <form id="authForm" onsubmit="handleFormSubmit(event)" class="space-y-4">
                    <input type="email" id="emailInput" required placeholder="you@example.com" class="w-full bg-slate-900 border border-slate-700 rounded-xl px-4 py-2.5 text-sm text-white focus:outline-none focus:border-amber-500">
                    <button type="submit" id="submitBtn" class="w-full bg-amber-500 hover:bg-amber-400 text-slate-950 font-bold py-3 rounded-xl transition text-sm shadow-md mt-2 cursor-pointer">
                        Continue
                    </button>
                </form>
            </div>
        </div>

        <!-- JavaScript Logic -->
        <script>
            window.onload = function() {
                const savedUser = localStorage.getItem('amalaj_user');
                if (savedUser) {
                    updateNavbarUser(savedUser);
                }
                loadUserListings();
                loadUserRentals();
                showBrowseListings('ALL');
            };

            function showBrowseListings(category) {
                const container = document.getElementById('browseContainer');
                const titleElem = document.getElementById('browseTitle');
                let listings = JSON.parse(localStorage.getItem('amalaj_listings') || '[]');

                if (category === 'ALL') {
                    titleElem.innerText = "All Browse Listings & Categories";
                } else {
                    titleElem.innerText = `Browse Listings: ${category}`;
                }

                let filtered = category === 'ALL' ? listings : listings.filter(item => item.type === category);

                if (filtered.length === 0) {
                    container.innerHTML = `
                        <div class="p-4 bg-slate-900/60 rounded-xl border border-slate-800 text-xs text-slate-400 col-span-full text-center space-y-1">
                            <p>No active listings found for ${category === 'ALL' ? 'any category' : category}.</p>
                            <p class="text-[10px] text-amber-400">Use the form above to publish a new listing!</p>
                        </div>
                    `;
                    return;
                }

                container.innerHTML = filtered.map(item => `
                    <div class="p-4 bg-slate-900/80 rounded-xl border border-slate-800 space-y-3">
                        <div class="flex justify-between items-center">
                            <span class="text-amber-400 font-bold uppercase text-[10px]">${item.type}</span>
                            <span class="text-xs bg-emerald-500/20 text-emerald-400 px-2 py-0.5 rounded-full font-bold">🛡️ Escrow Active</span>
                        </div>
                        <h4 class="font-bold text-white text-sm">${item.title}</h4>
                        <div class="flex justify-between items-center pt-2 border-t border-slate-800 text-xs">
                            <span class="font-black text-amber-400">ETB ${item.price}</span>
                            <button onclick="alert('Connecting to seller via secure Escrow Chat for ${item.title}...') " class="px-3 py-1.5 bg-amber-500 text-slate-950 font-bold rounded-lg hover:bg-amber-400 transition cursor-pointer">
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

            function handlePostListing(e) {
                e.preventDefault();
                const type = document.getElementById('listingType').value;
                const title = document.getElementById('listingTitle').value.trim();
                const price = document.getElementById('listingPrice').value.trim();

                if (!title || !price) return;

                let listings = JSON.parse(localStorage.getItem('amalaj_listings') || '[]');
                listings.push({ type, title, price, date: new Date().toLocaleDateString() });
                localStorage.setItem('amalaj_listings', JSON.stringify(listings));

                document.getElementById('listingTitle').value = '';
                document.getElementById('listingPrice').value = '';
                alert("Listing published successfully with Escrow protection!");
                loadUserListings();
                showBrowseListings('ALL');
                switchDashboardTab('listings');
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
                            <span class="text-amber-400 font-bold uppercase text-[10px]">${item.type}</span>
                            <h4 class="font-bold text-white text-sm mt-0.5">${item.title}</h4>
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

            function openConductModal() { document.getElementById('conductModal').classList.remove('hidden'); }
            function closeConductModal() { document.getElementById('conductModal').classList.add('hidden'); }
            function openAuthModal(mode) { document.getElementById('authModal').classList.remove('hidden'); }
            function closeAuthModal() { document.getElementById('authModal').classList.add('hidden'); }
            function handleGoogleAuth() { window.location.href = "/auth/google"; }
            function handleFormSubmit(e) {
                e.preventDefault();
                const email = document.getElementById('emailInput').value.trim();
                const userName = email.split('@')[0];
                const capitalizedName = userName.charAt(0).toUpperCase() + userName.slice(1);
                localStorage.setItem('amalaj_user', capitalizedName);
                closeAuthModal();
                updateNavbarUser(capitalizedName);
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