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
        <title>Amalaj Plus - Ethiopian Digital Assets & Tool Rental Marketplace</title>
        <script src="https://cdn.tailwindcss.com"></script>
        <!-- FontAwesome for Official Social Logos -->
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    </head>
    <body class="bg-[#0b132b] text-slate-100 min-h-screen font-sans selection:bg-amber-500 selection:text-slate-950">

        <!-- Header / Navigation -->
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
                    <a href="#toolRental" class="text-amber-400 font-semibold hover:underline py-2 flex items-center gap-1">Tool Rental ⚡</a>
                    <a href="#help" class="hover:text-amber-400 transition py-2">Resources</a>
                </div>

                <!-- Right Actions & Active Google Sign-In Button -->
                <div class="flex items-center space-x-4">
                    <button id="googleLoginBtn" onclick="handleGoogleLogin()" class="flex items-center space-x-2 bg-amber-500 hover:bg-amber-400 text-slate-950 font-bold px-4 py-2 rounded-xl transition shadow-md cursor-pointer">
                        <i class="fa-brands fa-google"></i>
                        <span class="text-xs">Sign In</span>
                    </button>
                </div>
            </div>
        </header>

        <!-- Hero Section (Ethiopian Market Focused) -->
        <section class="max-w-7xl mx-auto px-6 py-16 md:py-20">
            <div class="grid lg:grid-cols-12 gap-12 items-center">
                <div class="lg:col-span-7 space-y-8">
                    <h1 class="text-4xl md:text-6xl font-black tracking-tight text-white leading-tight">
                        The premier <span class="text-amber-400">Ethiopian marketplace</span> to buy, sell & rent digital assets.
                    </h1>

                    <p class="text-lg text-slate-300 max-w-xl leading-relaxed">
                        Join creators, developers & technicians across Ethiopia trading Telegram channels, TikTok, YouTube accounts, Facebook pages, and renting mobile repair software tools securely.
                    </p>

                    <div class="flex flex-wrap items-center gap-4 pt-2">
                        <a href="#marketplace" class="px-7 py-3.5 bg-amber-500 text-slate-950 font-bold rounded-xl hover:bg-amber-400 transition shadow-lg shadow-amber-500/20">
                            View Listings &rarr;
                        </a>
                        <a href="#toolRental" class="px-7 py-3.5 bg-slate-900 border border-slate-800 text-slate-200 font-semibold rounded-xl hover:bg-slate-800 transition">
                            ⚡ Rent Repair Tools
                        </a>
                    </div>
                </div>

                <!-- Right Side Hero Mockup Card -->
                <div class="lg:col-span-5 relative">
                    <div class="bg-[#1c2541] border border-slate-700/60 rounded-3xl p-6 shadow-2xl space-y-5">
                        <div class="flex justify-between items-center pb-4 border-b border-slate-800">
                            <div>
                                <span class="text-xs text-amber-400 font-bold uppercase tracking-wider">Verified Listing</span>
                                <h4 class="text-lg font-bold text-white mt-0.5">Ethiopian Tech & Media Channel</h4>
                            </div>
                            <span class="text-xl font-extrabold text-amber-400">ETB 85,000</span>
                        </div>

                        <div class="space-y-3 text-xs text-slate-300">
                            <div class="flex justify-between p-2.5 bg-slate-900/60 rounded-xl border border-slate-800">
                                <span class="text-slate-400">Platform:</span>
                                <span class="font-bold text-white">Telegram & YouTube</span>
                            </div>
                            <div class="flex justify-between p-2.5 bg-slate-900/60 rounded-xl border border-slate-800">
                                <span class="text-slate-400">Escrow Status:</span>
                                <span class="font-bold text-emerald-400">Secure & Protected</span>
                            </div>
                        </div>

                        <div class="pt-2 flex gap-3">
                            <button onclick="alert('Escrow process initiated for Ethiopian market.')" class="w-full py-2.5 bg-amber-500 text-slate-950 font-bold rounded-xl text-xs hover:bg-amber-400 transition cursor-pointer">Approve Escrow Request</button>
                        </div>
                    </div>
                </div>
            </div>
        </section>

        <!-- Marketplace Section -->
        <section id="marketplace" class="max-w-7xl mx-auto px-6 py-16 border-t border-slate-800">
            <div class="mb-12">
                <h2 class="text-3xl font-black text-white tracking-tight">Digital Asset Categories</h2>
                <p class="text-slate-400 mt-2 text-sm">Explore verified social media channels, groups, and accounts available for secure escrow exchange in Ethiopia.</p>
            </div>

            <div class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-4 gap-6">
                <!-- Telegram -->
                <div class="p-6 bg-[#16203a] border border-slate-700/60 rounded-2xl hover:border-[#229ED9] transition-all group shadow-xl">
                    <div class="w-12 h-12 rounded-xl bg-[#229ED9]/20 text-[#229ED9] flex items-center justify-center text-2xl mb-4">
                        <i class="fa-brands fa-telegram"></i>
                    </div>
                    <h3 class="font-bold text-white text-lg">Telegram</h3>
                    <p class="text-xs text-slate-400 mt-1">Channels, Groups & Bots</p>
                </div>

                <!-- TikTok -->
                <div class="p-6 bg-[#16203a] border border-slate-700/60 rounded-2xl hover:border-[#EE1D52] transition-all group shadow-xl">
                    <div class="w-12 h-12 rounded-xl bg-[#EE1D52]/20 text-[#EE1D52] flex items-center justify-center text-2xl mb-4">
                        <i class="fa-brands fa-tiktok"></i>
                    </div>
                    <h3 class="font-bold text-white text-lg">TikTok</h3>
                    <p class="text-xs text-slate-400 mt-1">Accounts & Live Access</p>
                </div>

                <!-- YouTube -->
                <div class="p-6 bg-[#16203a] border border-slate-700/60 rounded-2xl hover:border-[#FF0000] transition-all group shadow-xl">
                    <div class="w-12 h-12 rounded-xl bg-[#FF0000]/20 text-[#FF0000] flex items-center justify-center text-2xl mb-4">
                        <i class="fa-brands fa-youtube"></i>
                    </div>
                    <h3 class="font-bold text-white text-lg">YouTube</h3>
                    <p class="text-xs text-slate-400 mt-1">Monetized Channels</p>
                </div>

                <!-- Facebook -->
                <div class="p-6 bg-[#16203a] border border-slate-700/60 rounded-2xl hover:border-[#1877F2] transition-all group shadow-xl">
                    <div class="w-12 h-12 rounded-xl bg-[#1877F2]/20 text-[#1877F2] flex items-center justify-center text-2xl mb-4">
                        <i class="fa-brands fa-facebook"></i>
                    </div>
                    <h3 class="font-bold text-white text-lg">Facebook</h3>
                    <p class="text-xs text-slate-400 mt-1">Pages & Community Groups</p>
                </div>
            </div>
        </section>

        <!-- JavaScript for Login Action -->
        <script>
            function handleGoogleLogin() {
                alert("Google Sign-In integration ready for Amalaj Plus!");
            }
        </script>
    </body>
    </html>
    """