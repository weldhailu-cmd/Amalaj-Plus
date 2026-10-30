from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

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
        <!-- FontAwesome for Official Social Logos -->
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    </head>
    <body class="bg-[#0b132b] text-slate-100 min-h-screen font-sans selection:bg-amber-500 selection:text-slate-950">

        <!-- Header / Navigation (Acquire.com Style) -->
        <header class="border-b border-slate-800 bg-[#0b132b]/95 backdrop-blur sticky top-0 z-50">
            <div class="max-w-7xl mx-auto px-6 py-4 flex justify-between items-center relative">
                <!-- Circular Logo & Branding -->
                <div class="flex items-center space-x-3">
                    <div class="w-10 h-10 rounded-full border-2 border-amber-500 overflow-hidden shadow-lg shadow-amber-500/20 bg-white flex items-center justify-center p-0.5">
                        <img src="/static/logo.png" alt="Amalaj Plus Logo" class="w-full h-full object-cover rounded-full">
                    </div>
                    <span class="text-2xl font-extrabold text-white tracking-tight">Amalaj<span class="text-amber-400">Plus</span></span>
                </div>

                <!-- Navigation Links -->
                <div class="hidden md:flex items-center space-x-8 text-sm font-medium text-slate-300">
                    <a href="#marketplace" class="hover:text-amber-400 transition py-2">Marketplace</a>
                    
                    <div class="relative group">
                        <button class="flex items-center gap-1 hover:text-amber-400 transition py-2">
                            Sellers <span class="text-xs">▾</span>
                        </button>
                        <div class="absolute top-full left-0 w-64 bg-[#1c2541] border border-slate-700 shadow-2xl rounded-xl py-3 px-4 hidden group-hover:block z-50">
                            <a href="#sellers" class="block py-2 text-xs hover:text-amber-400">🏷️ List Your Asset</a>
                            <a href="#sellers" class="block py-2 text-xs hover:text-amber-400">🛡️ Escrow Protection</a>
                        </div>
                    </div>

                    <a href="#buyers" class="hover:text-amber-400 transition py-2">Buyers</a>
                    
                    <div class="relative group">
                        <button class="flex items-center gap-1 hover:text-amber-400 transition py-2">
                            Pricing <span class="text-xs">▾</span>
                        </button>
                        <div class="absolute top-full left-0 w-56 bg-[#1c2541] border border-slate-700 shadow-2xl rounded-xl py-3 px-4 hidden group-hover:block z-50">
                            <a href="#pricing" class="block py-2 text-xs hover:text-amber-400">Commission Rates</a>
                            <a href="#toolRental" class="block py-2 text-xs text-amber-400 font-bold">⚡ Tool Rental Rates</a>
                        </div>
                    </div>

                    <a href="#toolRental" class="text-amber-400 font-semibold hover:underline py-2 flex items-center gap-1">Tool Rental ⚡</a>
                    <a href="#help" class="hover:text-amber-400 transition py-2">Resources</a>
                </div>

                <!-- Right Actions -->
                <div class="flex items-center space-x-4">
                    <button class="hidden sm:inline-block text-xs font-semibold px-4 py-2 bg-amber-500/10 border border-amber-500/30 text-amber-400 rounded-xl hover:bg-amber-500/20 transition">
                        Free Asset Valuation
                    </button>
                    <button class="flex items-center space-x-2 bg-[#1c2541] border border-slate-700 hover:border-amber-500/50 px-3 py-1.5 rounded-xl transition shadow-md">
                        <svg class="w-5 h-5 text-slate-300" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16M4 18h16"></path>
                        </svg>
                        <div class="w-7 h-7 bg-amber-500/20 text-amber-400 rounded-full flex items-center justify-center text-xs font-bold">👤</div>
                    </button>
                </div>
            </div>
        </header>

        <!-- Hero Section (Acquire Layout) -->
        <section class="max-w-7xl mx-auto px-6 py-16 md:py-20">
            <div class="grid lg:grid-cols-12 gap-12 items-center">
                <div class="lg:col-span-7 space-y-8">
                    <h1 class="text-4xl md:text-6xl font-black tracking-tight text-white leading-tight">
                        The largest marketplace to <span class="text-amber-400">buy, sell & rent</span> digital assets.
                    </h1>

                    <p class="text-lg text-slate-300 max-w-xl leading-relaxed">
                        Join 10k+ creators & technicians trading Telegram channels, TikTok, YouTube accounts, Facebook pages, and renting mobile repair software tools.
                    </p>

                    <div class="flex flex-wrap items-center gap-4 pt-2">
                        <a href="#marketplace" class="px-7 py-3.5 bg-amber-500 text-slate-950 font-bold rounded-xl hover:bg-amber-400 transition shadow-lg shadow-amber-500/20">
                            View Listings &rarr;
                        </a>
                        <a href="#toolRental" class="px-7 py-3.5 bg-slate-900 border border-slate-800 text-slate-200 font-semibold rounded-xl hover:bg-slate-800 transition">
                            ⚡ Rent Repair Tools
                        </a>
                    </div>

                    <!-- Social Proof Ratings -->
                    <div class="flex items-center space-x-3 text-xs text-slate-400 pt-2">
                        <span class="text-amber-400 text-sm">⭐⭐⭐⭐⭐</span>
                        <span class="font-medium text-slate-300">4.9 average rating based on 500+ verified escrow deals</span>
                    </div>
                </div>

                <!-- Right Side Hero Mockup Card (Acquire Style) -->
                <div class="lg:col-span-5 relative">
                    <div class="bg-[#1c2541] border border-slate-700/60 rounded-3xl p-6 shadow-2xl space-y-5">
                        <div class="flex justify-between items-center pb-4 border-b border-slate-800">
                            <div>
                                <span class="text-xs text-amber-400 font-bold uppercase tracking-wider">Verified Listing</span>
                                <h4 class="text-lg font-bold text-white mt-0.5">Monetized Tech Channel</h4>
                            </div>
                            <span class="text-xl font-extrabold text-amber-400">$1,500</span>
                        </div>

                        <div class="space-y-3 text-xs text-slate-300">
                            <div class="flex justify-between p-2.5 bg-slate-900/60 rounded-xl border border-slate-800">
                                <span class="text-slate-400">Platform:</span>
                                <span class="font-bold text-white">YouTube (45k Subscribers)</span>
                            </div>
                            <div class="flex justify-between p-2.5 bg-slate-900/60 rounded-xl border border-slate-800">
                                <span class="text-slate-400">Monthly Revenue:</span>
                                <span class="font-bold text-emerald-400">$320 / mo</span>
                            </div>
                        </div>

                        <div class="pt-2 flex gap-3">
                            <button class="w-full py-2.5 bg-amber-500 text-slate-950 font-bold rounded-xl text-xs hover:bg-amber-400 transition">Approve Escrow Request</button>
                        </div>
                    </div>
                </div>
            </div>
        </section>

        <!-- Digital Asset Categories (Official High-Contrast Logos) -->
        <section id="marketplace" class="max-w-7xl mx-auto px-6 py-16 border-t border-slate-800">
            <div class="mb-12">
                <h2 class="text-3xl font-black text-white tracking-tight">Digital Asset Categories</h2>
                <p class="text-slate-400 mt-2 text-sm">Explore verified social media channels, groups, and accounts available for secure escrow exchange.</p>
            </div>

            <div class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-4 gap-6">
                <!-- Telegram -->
                <div class="p-6 bg-[#16203a] border border-slate-700/60 rounded-2xl hover:border-[#229ED9] transition-all group shadow-xl hover:-translate-y-1">
                    <div class="w-12 h-12 rounded-xl bg-[#229ED9]/20 text-[#229ED9] flex items-center justify-center text-2xl mb-4 group-hover:scale-110 transition">
                        <i class="fa-brands fa-telegram"></i>
                    </div>
                    <h3 class="font-bold text-white text-lg group-hover:text-[#229ED9] transition">Telegram</h3>
                    <p class="text-xs text-slate-400 mt-1">Channels, Groups & Bots</p>
                </div>

                <!-- TikTok -->
                <div class="p-6 bg-[#16203a] border border-slate-700/60 rounded-2xl hover:border-[#EE1D52] transition-all group shadow-xl hover:-translate-y-1">
                    <div class="w-12 h-12 rounded-xl bg-[#EE1D52]/20 text-[#EE1D52] flex items-center justify-center text-2xl mb-4 group-hover:scale-110 transition">
                        <i class="fa-brands fa-tiktok"></i>
                    </div>
                    <h3 class="font-bold text-white text-lg group-hover:text-[#EE1D52] transition">TikTok</h3>
                    <p class="text-xs text-slate-400 mt-1">Accounts & Live Access</p>
                </div>

                <!-- YouTube -->
                <div class="p-6 bg-[#16203a] border border-slate-700/60 rounded-2xl hover:border-[#FF0000] transition-all group shadow-xl hover:-translate-y-1">
                    <div class="w-12 h-12 rounded-xl bg-[#FF0000]/20 text-[#FF0000] flex items-center justify-center text-2xl mb-4 group-hover:scale-110 transition">
                        <i class="fa-brands fa-youtube"></i>
                    </div>
                    <h3 class="font-bold text-white text-lg group-hover:text-[#FF0000] transition">YouTube</h3>
                    <p class="text-xs text-slate-400 mt-1">Monetized Channels</p>
                </div>

                <!-- Facebook -->
                <div class="p-6 bg-[#16203a] border border-slate-700/60 rounded-2xl hover:border-[#1877F2] transition-all group shadow-xl hover:-translate-y-1">
                    <div class="w-12 h-12 rounded-xl bg-[#1877F2]/20 text-[#1877F2] flex items-center justify-center text-2xl mb-4 group-hover:scale-110 transition">
                        <i class="fa-brands fa-facebook"></i>
                    </div>
                    <h3 class="font-bold text-white text-lg group-hover:text-[#1877F2] transition">Facebook</h3>
                    <p class="text-xs text-slate-400 mt-1">Pages & Community Groups</p>
                </div>

                <!-- Instagram -->
                <div class="p-6 bg-[#16203a] border border-slate-700/60 rounded-2xl hover:border-[#E4405F] transition-all group shadow-xl hover:-translate-y-1">
                    <div class="w-12 h-12 rounded-xl bg-[#E4405F]/20 text-[#E4405F] flex items-center justify-center text-2xl mb-4 group-hover:scale-110 transition">
                        <i class="fa-brands fa-instagram"></i>
                    </div>
                    <h3 class="font-bold text-white text-lg group-hover:text-[#E4405F] transition">Instagram</h3>
                    <p class="text-xs text-slate-400 mt-1">Active Accounts</p>
                </div>

                <!-- X (Twitter) -->
                <div class="p-6 bg-[#16203a] border border-slate-700/60 rounded-2xl hover:border-slate-200 transition-all group shadow-xl hover:-translate-y-1">
                    <div class="w-12 h-12 rounded-xl bg-slate-200 text-slate-950 flex items-center justify-center text-2xl mb-4 group-hover:scale-110 transition font-black">
                        <i class="fa-brands fa-x-twitter"></i>
                    </div>
                    <h3 class="font-bold text-white text-lg group-hover:text-slate-200 transition">X (Twitter)</h3>
                    <p class="text-xs text-slate-400 mt-1">Verified & Aged Profiles</p>
                </div>

                <!-- LinkedIn -->
                <div class="p-6 bg-[#16203a] border border-slate-700/60 rounded-2xl hover:border-[#0A66C2] transition-all group shadow-xl hover:-translate-y-1">
                    <div class="w-12 h-12 rounded-xl bg-[#0A66C2]/20 text-[#0A66C2] flex items-center justify-center text-2xl mb-4 group-hover:scale-110 transition">
                        <i class="fa-brands fa-linkedin-in"></i>
                    </div>
                    <h3 class="font-bold text-white text-lg group-hover:text-[#0A66C2] transition">LinkedIn</h3>
                    <p class="text-xs text-slate-400 mt-1">Company & Profiles</p>
                </div>

                <!-- Gaming & Misc -->
                <div class="p-6 bg-[#16203a] border border-slate-700/60 rounded-2xl hover:border-amber-400 transition-all group shadow-xl hover:-translate-y-1">
                    <div class="w-12 h-12 rounded-xl bg-amber-500/20 text-amber-400 flex items-center justify-center text-2xl mb-4 group-hover:scale-110 transition">
                        <i class="fa-solid fa-gamepad"></i>
                    </div>
                    <h3 class="font-bold text-white text-lg group-hover:text-amber-400 transition">Gaming & Misc</h3>
                    <p class="text-xs text-slate-400 mt-1">PUBG, Discord & More</p>
                </div>
            </div>
        </section>

        <!-- Software Tool Rental Section -->
        <section id="toolRental" class="max-w-7xl mx-auto px-6 py-16 border-t border-slate-800">
            <div class="bg-gradient-to-r from-blue-950/60 to-[#1c2541] border border-amber-500/30 rounded-3xl p-8 md:p-12 shadow-2xl">
                <div class="max-w-2xl mb-10">
                    <span class="px-3 py-1 bg-amber-500/10 text-amber-400 border border-amber-500/30 rounded-full text-xs font-bold uppercase tracking-wider">Hourly & Daily Rental</span>
                    <h2 class="text-3xl md:text-4xl font-black text-white mt-4">Professional Repair Tool Rentals</h2>
                    <p class="text-slate-300 mt-2">Rent official mobile repair tools & software licenses by the hour. Affordable access for technicians across all cities.</p>
                </div>

                <div class="grid md:grid-cols-3 gap-6">
                    <div class="bg-slate-900/80 border border-slate-800 rounded-2xl p-6 space-y-4">
                        <div class="flex justify-between items-start">
                            <span class="text-xl font-bold text-white">UnlockTool Access</span>
                            <span class="text-xs px-2.5 py-1 bg-emerald-500/10 text-emerald-400 rounded-full font-bold">Available</span>
                        </div>
                        <p class="text-xs text-slate-400">Multi-brand mobile flashing, FRP bypass, and repair solution.</p>
                        <div class="pt-4 border-t border-slate-800 flex justify-between items-center">
                            <span class="text-amber-400 font-extrabold">$2.00 / hour</span>
                            <button class="px-4 py-2 bg-amber-500 text-slate-950 text-xs font-bold rounded-lg hover:bg-amber-400 transition">Rent Now</button>
                        </div>
                    </div>

                    <div class="bg-slate-900/80 border border-slate-800 rounded-2xl p-6 space-y-4">
                        <div class="flex justify-between items-start">
                            <span class="text-xl font-bold text-white">DFT Pro License</span>
                            <span class="text-xs px-2.5 py-1 bg-emerald-500/10 text-emerald-400 rounded-full font-bold">Available</span>
                        </div>
                        <p class="text-xs text-slate-400">Advanced Android repair and servicing software utility.</p>
                        <div class="pt-4 border-t border-slate-800 flex justify-between items-center">
                            <span class="text-amber-400 font-extrabold">$2.50 / hour</span>
                            <button class="px-4 py-2 bg-amber-500 text-slate-950 text-xs font-bold rounded-lg hover:bg-amber-400 transition">Rent Now</button>
                        </div>
                    </div>

                    <div class="bg-slate-900/80 border border-slate-800 rounded-2xl p-6 space-y-4">
                        <div class="flex justify-between items-start">
                            <span class="text-xl font-bold text-white">Chimera Tool</span>
                            <span class="text-xs px-2.5 py-1 bg-emerald-500/10 text-emerald-400 rounded-full font-bold">Available</span>
                        </div>
                        <p class="text-xs text-slate-400">Professional tool for Samsung, Huawei, and Xiaomi devices.</p>
                        <div class="pt-4 border-t border-slate-800 flex justify-between items-center">
                            <span class="text-amber-400 font-extrabold">$3.00 / hour</span>
                            <button class="px-4 py-2 bg-amber-500 text-slate-950 text-xs font-bold rounded-lg hover:bg-amber-400 transition">Rent Now</button>
                        </div>
                    </div>
                </div>
            </div>
        </section>

    </body>
    </html>
    """