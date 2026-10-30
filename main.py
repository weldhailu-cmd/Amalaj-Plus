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

            <!-- Hero / About Section -->
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

                    <!-- Quick Listing Card / Post Ad Form -->
                    <div class="lg:col-span-5">
                        <div class="bg-[#1c2541] border border-slate-700/60 rounded-3xl p-6 shadow-2xl space-y-4">
                            <div class="flex justify-between items-center pb-3 border-b border-slate-800">
                                <h3 class="text-base font-bold text-white">Post New Digital Asset Ad</h3>
                                <span class="text-amber-400 text-xs font-bold">2% Escrow Protected</span>
                            </div>
                            <form onsubmit="handlePostListing(event)" class="space-y-3 text-xs">
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
                                        <select id="listingPlatform" class="w-full bg-slate-900 border border-slate-700 rounded-xl px-2 py-2 text-white focus:outline-none focus:border-amber-500">
                                            <option value="Telegram">Telegram</option>
                                            <option value="TikTok">TikTok</option>
                                            <option value="YouTube">YouTube</option>
                                            <option value="Facebook">Facebook</option>
                                        </select>
                                    </div>
                                    <div>
                                        <label class="block text-slate-300 font-semibold mb-1">Asset Type *</label>
                                        <select id="listingAssetType" class="w-full bg-slate-900 border border-slate-700 rounded-xl px-2 py-2 text-white focus:outline-none focus:border-amber-500">
                                            <option value="Channel">Channel / Page</option>
                                            <option value="Group">Group</option>
                                            <option value="Bot">Bot</option>
                                            <option value="Account">Account</option>
                                        </select>
                                    </div>
                                </div>
                                <div class="grid grid-cols-2 gap-2">
                                    <div>
                                        <label class="block text-slate-300 font-semibold mb-1">Subscribers</label>
                                        <input type="number" id="listingSubCount" placeholder="e.g., 303K" class="w-full bg-slate-900 border border-slate-700 rounded-xl px-3 py-2 text-white focus:outline-none focus:border-amber-500">
                                    </div>
                                    <div>
                                        <label class="block text-slate-300 font-semibold mb-1">Asking Price (ETB) *</label>
                                        <input type="number" id="listingPrice" required placeholder="5000" class="w-full bg-slate-900 border border-slate-700 rounded-xl px-3 py-2 text-white focus:outline-none focus:border-amber-500">
                                    </div>
                                </div>
                                <button type="submit" class="w-full py-2.5 bg-amber-500 text-slate-950 font-bold rounded-xl hover:bg-amber-400 transition cursor-pointer">
                                    Publish Ad with Escrow Protection &rarr;
                                </button>
                            </form>
                        </div>
                    </div>
                </div>
            </section>

            <!-- Digital Asset Categories Marketplace -->
            <section id="marketplace" class="max-w-7xl mx-auto px-6 py-10 border-t border-slate-800">
                <div class="mb-8">
                    <h2 class="text-2xl font-black text-white tracking-tight">Digital Assets Marketplace</h2>
                    <p class="text-slate-400 text-xs mt-1">Explore verified Telegram channels, TikTok, YouTube & Facebook accounts with secure Escrow & Chat.</p>
                </div>
                <!-- Dynamic Marketplace Listings Grid -->
                <div id="marketplaceListingsGrid" class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
                    <!-- Populated dynamically via JavaScript -->
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
                <div id="formErrorBox" class="hidden bg-red-500/10 border border-red-500/50 text-red-400 text-xs p-3 rounded-xl text-center"></div>
                <form id="authForm" onsubmit="handleFormSubmit(event)" class="space-y-4">
                    <div id="fullNameGroup">
                        <label class="block text-xs font-semibold text-slate-300 mb-1">Full Name</label>
                        <input type="text" id="fullNameInput" placeholder="Hailewelde Kidan" class="w-full bg-slate-900 border border-slate-700 rounded-xl px-4 py-2.5 text-sm text-white focus:outline-none focus:border-amber-500">
                    </div>
                    <div>
                        <label class="block text-xs font-semibold text-slate-300 mb-1">Email address</label>
                        <input type="email" id="emailInput" required placeholder="you@example.com" class="w-full bg-slate-900 border border-slate-700 rounded-xl px-4 py-2.5 text-sm text-white focus:outline-none focus:border-amber-500">
                    </div>
                    <div>
                        <label class="block text-xs font-semibold text-slate-300 mb-1">Password</label>
                        <div class="relative">
                            <input type="password" id="passwordInput" required placeholder="••••••••" class="w-full bg-slate-900 border border-slate-700 rounded-xl px-4 py-2.5 text-sm text-white focus:outline-none focus:border-amber-500 pr-10">
                            <button type="button" onclick="togglePassword('passwordInput', 'eyeIcon1')" class="absolute right-3 top-3 text-slate-400 hover:text-white text-xs cursor-pointer">
                                <i id="eyeIcon1" class="fa-solid fa-eye"></i>
                            </button>
                        </div>
                    </div>
                    <div id="confirmPasswordGroup">
                        <label class="block text-xs font-semibold text-slate-300 mb-1">Confirm Password</label>
                        <div class="relative">
                            <input type="password" id="confirmPasswordInput" placeholder="••••••••" class="w-full bg-slate-900 border border-slate-700 rounded-xl px-4 py-2.5 text-sm text-white focus:outline-none focus:border-amber-500 pr-10">
                            <button type="button" onclick="togglePassword('confirmPasswordInput', 'eyeIcon2')" class="absolute right-3 top-3 text-slate-400 hover:text-white text-xs cursor-pointer">
                                <i id="eyeIcon2" class="fa-solid fa-eye"></i>
                            </button>
                        </div>
                    </div>
                    <button type="submit" id="submitBtn" class="w-full bg-amber-500 hover:bg-amber-400 text-slate-950 font-bold py-3 rounded-xl transition text-sm shadow-md mt-2 cursor-pointer">
                        Create Account
                    </button>
                </form>
                <div class="text-center text-xs text-slate-400">
                    <span id="switchText">Already have an account?</span>
                    <button onclick="toggleAuthMode()" id="switchBtn" class="text-amber-400 font-bold hover:underline ml-1 cursor-pointer">Sign In</button>
                </div>
            </div>
        </div>

        <!-- JavaScript Logic -->
        <script>
            let currentMode = 'signup';

            // Initial Mock Listings
            const defaultListings = [
                { id: 1, platform: 'YouTube', title: 'Sportsphere', category: 'Sports', price: '78,000 ETB', subscribers: '303K', views: '14M', status: 'ACTIVE', image: 'https://images.unsplash.com/photo-1611162617474-5b21e879e113?w=100&h=100&fit=crop' },
                { id: 2, platform: 'YouTube', title: 'NextGoal', category: 'Entertainment', price: '14,950 ETB', subscribers: '33K', views: '3.3M', status: 'ACTIVE', image: 'https://images.unsplash.com/photo-1579783902614-a3fb3927b675?w=100&h=100&fit=crop' },
                { id: 3, platform: 'Instagram', title: 'thela.stone291', category: 'Lifestyle', price: '910 ETB', subscribers: '1.1K', views: '1 Avg Likes', status: 'ACTIVE', image: 'https://images.unsplash.com/photo-1516589178581-6cd7833ae3b2?w=100&h=100&fit=crop' },
                { id: 4, platform: 'Facebook', title: 'Osama Jami', category: 'Business', price: '1,950 ETB', subscribers: '5.1K', views: '12 Page Likes', status: 'ACTIVE', image: 'https://images.unsplash.com/photo-1561948955-570b270e7c36?w=100&h=100&fit=crop' }
            ];

            window.onload = function() {
                const savedUser = localStorage.getItem('amalaj_user');
                if (savedUser) {
                    updateNavbarUser(savedUser);
                }
                loadMarketplaceListings();
                loadUserListings();
                loadUserRentals();
            };

            function loadMarketplaceListings() {
                const grid = document.getElementById('marketplaceListingsGrid');
                let customListings = JSON.parse(localStorage.getItem('amalaj_custom_listings') || '[]');
                let allListings = [...defaultListings, ...customListings];

                grid.innerHTML = allListings.map(item => {
                    let brandBg = 'bg-red-600';
                    if (item.platform === 'Instagram') brandBg = 'bg-gradient-to-b from-purple-600 via-pink-600 to-amber-500';
                    if (item.platform === 'Facebook') brandBg = 'bg-blue-600';
                    if (item.platform === 'Telegram') brandBg = 'bg-[#229ED9]';

                    return `
                        <div class="bg-[#16203a] border border-slate-700/60 rounded-3xl overflow-hidden shadow-2xl flex relative">
                            <div class="${brandBg} w-10 flex items-center justify-center py-6 shrink-0">
                                <span class="text-white font-bold text-xs tracking-widest uppercase transform -rotate-90 whitespace-nowrap">
                                    ${item.platform}
                                </span>
                            </div>
                            <div class="p-5 flex-grow space-y-4">
                                <div class="flex items-start justify-between">
                                    <div class="flex items-center space-x-3">
                                        <img src="${item.image || 'https://images.unsplash.com/photo-1611162617474-5b21e879e113?w=100&h=100&fit=crop'}" alt="${item.title}" class="w-12 h-12 rounded-2xl object-cover border border-slate-700" />
                                        <div>
                                            <div class="flex items-center space-x-2">
                                                <span class="px-2 py-0.5 bg-blue-600 text-white rounded text-[10px] font-bold">NEW</span>
                                                <h3 class="font-bold text-white text-sm">${item.title}</h3>
                                            </div>
                                            <span class="text-[11px] text-slate-400 flex items-center gap-1 mt-0.5">
                                                <i class="fa-solid fa-globe"></i> Open on ${item.platform}
                                            </span>
                                        </div>
                                    </div>
                                    <button onclick="alert('Viewing Detail View... Escrow Protected!')" class="px-3 py-1 bg-slate-800 hover:bg-slate-700 text-slate-300 rounded-xl text-xs font-semibold border border-slate-700 transition cursor-pointer">
                                        Details
                                    </button>
                                </div>
                                <div class="flex items-center space-x-2 text-[11px]">
                                    <span class="px-2.5 py-1 bg-slate-900 text-slate-300 rounded-lg border border-slate-800">${item.category || 'Asset'}</span>
                                    <span class="px-2.5 py-1 bg-emerald-500/10 text-emerald-400 rounded-lg border border-emerald-500/20 font-semibold">Very Good Price</span>
                                </div>
                                <div class="bg-slate-900/80 border border-slate-800 rounded-2xl p-3 flex justify-between items-center text-xs">
                                    <div class="flex items-center space-x-2">
                                        <i class="fa-solid fa-users text-slate-400"></i>
                                        <div>
                                            <div class="font-extrabold text-white">${item.subscribers || 'Verified'}</div>
                                            <div class="text-[10px] text-slate-400">Subscribers</div>
                                        </div>
                                    </div>
                                    <div class="flex items-center space-x-2">
                                        <i class="fa-solid fa-eye text-slate-400"></i>
                                        <div>
                                            <div class="font-extrabold text-white">${item.views || 'Active'}</div>
                                            <div class="text-[10px] text-slate-400">Views</div>
                                        </div>
                                    </div>
                                    <div class="flex items-center space-x-1 px-2 py-1 bg-emerald-500/10 text-emerald-400 rounded-full text-[10px] font-bold">
                                        <span class="w-1.5 h-1.5 bg-emerald-500 rounded-full animate-pulse"></span>
                                        <span>ACTIVE</span>
                                    </div>
                                </div>
                                <div class="flex items-center justify-between pt-2 border-t border-slate-800">
                                    <div>
                                        <div class="text-[10px] text-slate-400 uppercase tracking-wider">Price</div>
                                        <div class="text-lg font-black text-white">${item.price} ETB</div>
                                    </div>
                                    <div class="flex space-x-2">
                                        <button onclick="alert('Opening Secure Admin-Mediated Chat for ${item.title}. Anti-scam guard active.')" class="px-3 py-2 bg-slate-800 hover:bg-slate-700 text-amber-400 font-bold rounded-xl text-xs border border-slate-700 transition cursor-pointer flex items-center gap-1">
                                            <i class="fa-solid fa-comments"></i> Chat
                                        </button>
                                        <button onclick="alert('Initiating Escrow Purchase for ${item.title} (${item.price} ETB). 2% fee applies.')" class="px-4 py-2 bg-red-600 hover:bg-red-500 text-white font-bold rounded-xl text-xs transition cursor-pointer shadow-lg flex items-center gap-1.5">
                                            <i class="fa-solid fa-cart-shopping"></i> Buy
                                        </button>
                                    </div>
                                </div>
                            </div>
                        </div>
                    `;
                }).join('');
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
                const title = document.getElementById('listingTitle').value.trim();
                const link = document.getElementById('listingLink').value.trim();
                const platform = document.getElementById('listingPlatform').value;
                const assetType = document.getElementById('listingAssetType').value;
                const subCount = document.getElementById('listingSubCount').value.trim();
                const price = document.getElementById('listingPrice').value.trim();

                if (!title || !price) return;

                let newItem = {
                    id: Date.now(),
                    platform: platform,
                    title: title,
                    category: assetType,
                    price: price,
                    subscribers: subCount ? subCount + 'K' : 'Verified',
                    views: 'Auto-scan',
                    status: 'ACTIVE',
                    link: link,
                    image: 'https://images.unsplash.com/photo-1611162617474-5b21e879e113?w=100&h=100&fit=crop'
                };

                let customListings = JSON.parse(localStorage.getItem('amalaj_custom_listings') || '[]');
                customListings.push(newItem);
                localStorage.setItem('amalaj_custom_listings', JSON.stringify(customListings));

                document.getElementById('listingTitle').value = '';
                document.getElementById('listingLink').value = '';
                document.getElementById('listingSubCount').value = '';
                document.getElementById('listingPrice').value = '';

                alert("Ad published successfully with Admin Escrow Protection! (2% fee applies)");
                loadMarketplaceListings();
                loadUserListings();
                switchDashboardTab('listings');
            }

            function loadUserListings() {
                const container = document.getElementById('userListingsContainer');
                let customListings = JSON.parse(localStorage.getItem('amalaj_custom_listings') || '[]');
                if (customListings.length === 0) {
                    container.innerHTML = `<div class="p-4 bg-slate-900/60 rounded-xl border border-slate-800 text-xs text-slate-400 flex justify-between items-center"><span>No active listings yet. Use the form above to add one!</span><span class="text-emerald-400 font-semibold">Escrow Ready</span></div>`;
                    return;
                }
                container.innerHTML = customListings.map(item => `
                    <div class="p-4 bg-slate-900/80 rounded-xl border border-slate-800 flex justify-between items-center text-xs">
                        <div>
                            <span class="text-amber-400 font-bold uppercase text-[10px]">${item.platform} (${item.category})</span>
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

            function openAuthModal(mode) {
                currentMode = mode;
                document.getElementById('authModal').classList.remove('hidden');
            }

            function closeAuthModal() {
                document.getElementById('authModal').classList.add('hidden');
            }

            function togglePassword(inputId, iconId) {
                const input = document.getElementById(inputId);
                const icon = document.getElementById(iconId);
                if (input.type === 'password') {
                    input.type = 'text';
                    icon.classList.remove('fa-eye');
                    icon.classList.add('fa-eye-slash');
                } else {
                    input.type = 'password';
                    icon.classList.remove('fa-eye-slash');
                    icon.classList.add('fa-eye');
                }
            }

            function handleGoogleAuth() {
                window.location.href = "/auth/google";
            }

            function handleFormSubmit(e) {
                e.preventDefault();
                const email = document.getElementById('emailInput').value.trim();
                const userName = email.split('@')[0];
                const capitalizedName = userName.charAt(0).toUpperCase() + userName.slice(1);
                localStorage.setItem('amalaj_user', capitalizedName);
                alert("Authentication successful!");
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