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
    <body class="bg-[#0b132b] text-slate-100 min-h-screen font-sans">

        <!-- Header -->
        <header class="border-b border-slate-800 bg-[#0b132b]/95 backdrop-blur sticky top-0 z-50">
            <div class="max-w-7xl mx-auto px-6 py-4 flex justify-between items-center">
                <div class="flex items-center space-x-3">
                    <div class="w-10 h-10 rounded-full border-2 border-amber-500 overflow-hidden bg-white flex items-center justify-center p-0.5 shadow-lg shadow-amber-500/20">
                        <img src="/static/logo.png" alt="Amalaj Plus Logo" class="w-full h-full object-cover rounded-full">
                    </div>
                    <span class="text-2xl font-extrabold text-white tracking-tight">Amalaj<span class="text-amber-400">Plus</span></span>
                </div>
                <div class="hidden md:flex items-center space-x-8 text-sm font-medium text-slate-300">
                    <a href="#marketplace" class="hover:text-amber-400 transition py-2">Marketplace</a>
                    <a href="#toolRental" class="text-amber-400 font-semibold hover:underline py-2">Tool Rental ⚡</a>
                </div>
            </div>
        </header>

        <!-- Hero Section -->
        <section class="max-w-7xl mx-auto px-6 py-16">
            <div class="grid lg:grid-cols-12 gap-12 items-center">
                <div class="lg:col-span-7 space-y-6">
                    <h1 class="text-4xl md:text-6xl font-black text-white leading-tight">
                        Buy, Sell & Rent <span class="text-amber-400">Digital Assets</span> & Repair Tools.
                    </h1>
                    <p class="text-lg text-slate-300">
                        Secure escrow platform for Telegram channels, TikTok, YouTube accounts, and hourly mobile repair tool rentals.
                    </p>
                    <div class="flex flex-wrap gap-4">
                        <a href="#marketplace" class="px-7 py-3.5 bg-amber-500 text-slate-950 font-bold rounded-xl hover:bg-amber-400 transition shadow-lg">Explore Marketplace &rarr;</a>
                        <a href="#toolRental" class="px-7 py-3.5 bg-slate-900 border border-slate-800 text-slate-200 font-semibold rounded-xl hover:bg-slate-800 transition">⚡ Rent Repair Tools</a>
                    </div>
                </div>
            </div>
        </section>

        <!-- Digital Asset Categories with Branded Colors & Logos -->
        <section id="marketplace" class="max-w-7xl mx-auto px-6 py-16 border-t border-slate-800">
            <div class="mb-10">
                <h2 class="text-3xl font-black text-white">Digital Asset Categories</h2>
                <p class="text-slate-400 text-sm mt-1">Explore verified social media channels, groups, and accounts available for secure escrow exchange.</p>
            </div>

            <div class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-4 gap-6">
                <!-- Telegram -->
                <div class="p-6 bg-[#16203a] border border-slate-700/60 rounded-2xl hover:border-[#229ED9] transition-all group shadow-xl hover:-translate-y-1">
                    <div class="w-12 h-12 rounded-xl bg-[#229ED9]/10 text-[#229ED9] flex items-center justify-center text-2xl mb-4 group-hover:scale-110 transition">
                        <i class="fa-brands fa-telegram"></i>
                    </div>
                    <h3 class="font-bold text-white text-lg group-hover:text-[#229ED9] transition">Telegram</h3>
                    <p class="text-xs text-slate-400 mt-1">Channels, Groups & Bots</p>
                </div>

                <!-- TikTok -->
                <div class="p-6 bg-[#16203a] border border-slate-700/60 rounded-2xl hover:border-[#EE1D52] transition-all group shadow-xl hover:-translate-y-1">
                    <div class="w-12 h-12 rounded-xl bg-[#EE1D52]/10 text-[#EE1D52] flex items-center justify-center text-2xl mb-4 group-hover:scale-110 transition">
                        <i class="fa-brands fa-tiktok"></i>
                    </div>
                    <h3 class="font-bold text-white text-lg group-hover:text-[#EE1D52] transition">TikTok</h3>
                    <p class="text-xs text-slate-400 mt-1">Accounts & Live Access</p>
                </div>

                <!-- YouTube -->
                <div class="p-6 bg-[#16203a] border border-slate-700/60 rounded-2xl hover:border-[#FF0000] transition-all group shadow-xl hover:-translate-y-1">
                    <div class="w-12 h-12 rounded-xl bg-[#FF0000]/10 text-[#FF0000] flex items-center justify-center text-2xl mb-4 group-hover:scale-110 transition">
                        <i class="fa-brands fa-youtube"></i>
                    </div>
                    <h3 class="font-bold text-white text-lg group-hover:text-[#FF0000] transition">YouTube</h3>
                    <p class="text-xs text-slate-400 mt-1">Monetized Channels</p>
                </div>

                <!-- Facebook -->
                <div class="p-6 bg-[#16203a] border border-slate-700/60 rounded-2xl hover:border-[#1877F2] transition-all group shadow-xl hover:-translate-y-1">
                    <div class="w-12 h-12 rounded-xl bg-[#1877F2]/10 text-[#1877F2] flex items-center justify-center text-2xl mb-4 group-hover:scale-110 transition">
                        <i class="fa-brands fa-facebook"></i>
                    </div>
                    <h3 class="font-bold text-white text-lg group-hover:text-[#1877F2] transition">Facebook</h3>
                    <p class="text-xs text-slate-400 mt-1">Pages & Community Groups</p>
                </div>

                <!-- Instagram -->
                <div class="p-6 bg-[#16203a] border border-slate-700/60 rounded-2xl hover:border-[#E4405F] transition-all group shadow-xl hover:-translate-y-1">
                    <div class="w-12 h-12 rounded-xl bg-[#E4405F]/10 text-[#E4405F] flex items-center justify-center text-2xl mb-4 group-hover:scale-110 transition">
                        <i class="fa-brands fa-instagram"></i>
                    </div>
                    <h3 class="font-bold text-white text-lg group-hover:text-[#E4405F] transition">Instagram</h3>
                    <p class="text-xs text-slate-400 mt-1">Active Accounts</p>
                </div>

                <!-- X (Twitter) -->
                <div class="p-6 bg-[#16203a] border border-slate-700/60 rounded-2xl hover:border-slate-300 transition-all group shadow-xl hover:-translate-y-1">
                    <div class="w-12 h-12 rounded-xl bg-slate-800 text-white flex items-center justify-center text-2xl mb-4 group-hover:scale-110 transition">
                        <i class="fa-brands fa-x-twitter"></i>
                    </div>
                    <h3 class="font-bold text-white text-lg group-hover:text-slate-300 transition">X (Twitter)</h3>
                    <p class="text-xs text-slate-400 mt-1">Verified & Aged Profiles</p>
                </div>

                <!-- LinkedIn -->
                <div class="p-6 bg-[#16203a] border border-slate-700/60 rounded-2xl hover:border-[#0A66C2] transition-all group shadow-xl hover:-translate-y-1">
                    <div class="w-12 h-12 rounded-xl bg-[#0A66C2]/10 text-[#0A66C2] flex items-center justify-center text-2xl mb-4 group-hover:scale-110 transition">
                        <i class="fa-brands fa-linkedin-in"></i>
                    </div>
                    <h3 class="font-bold text-white text-lg group-hover:text-[#0A66C2] transition">LinkedIn</h3>
                    <p class="text-xs text-slate-400 mt-1">Company & Profiles</p>
                </div>

                <!-- Gaming & Misc -->
                <div class="p-6 bg-[#16203a] border border-slate-700/60 rounded-2xl hover:border-amber-400 transition-all group shadow-xl hover:-translate-y-1">
                    <div class="w-12 h-12 rounded-xl bg-amber-500/10 text-amber-400 flex items-center justify-center text-2xl mb-4 group-hover:scale-110 transition">
                        <i class="fa-solid fa-gamepad"></i>
                    </div>
                    <h3 class="font-bold text-white text-lg group-hover:text-amber-400 transition">Gaming & Misc</h3>
                    <p class="text-xs text-slate-400 mt-1">PUBG, Discord & More</p>
                </div>
            </div>
        </section>

        <!-- Tool Rental Section -->
        <section id="toolRental" class="max-w-7xl mx-auto px-6 py-16 border-t border-slate-800">
            <div class="bg-gradient-to-r from-blue-950/60 to-[#1c2541] border border-amber-500/30 rounded-3xl p-8 md:p-12 shadow-2xl">
                <span class="px-3 py-1 bg-amber-500/10 text-amber-400 border border-amber-500/30 rounded-full text-xs font-bold uppercase">Hourly & Daily Rental</span>
                <h2 class="text-3xl font-black text-white mt-4">Professional Repair Tool Rentals</h2>
                <p class="text-slate-300 mt-2 mb-8">Rent official mobile repair tools & software licenses by the hour.</p>

                <div class="grid md:grid-cols-3 gap-6">
                    <div class="bg-slate-900/80 border border-slate-800 rounded-2xl p-6 space-y-4">
                        <h3 class="text-xl font-bold text-white">UnlockTool Access</h3>
                        <p class="text-xs text-slate-400">FRP bypass and multi-brand repair solution.</p>
                        <div class="flex justify-between items-center pt-4 border-t border-slate-800">
                            <span class="text-amber-400 font-extrabold">$2.00 / hour</span>
                            <button class="px-4 py-2 bg-amber-500 text-slate-950 text-xs font-bold rounded-lg hover:bg-amber-400">Rent Now</button>
                        </div>
                    </div>
                    <div class="bg-slate-900/80 border border-slate-800 rounded-2xl p-6 space-y-4">
                        <h3 class="text-xl font-bold text-white">DFT Pro License</h3>
                        <p class="text-xs text-slate-400">Advanced Android repair utility software.</p>
                        <div class="flex justify-between items-center pt-4 border-t border-slate-800">
                            <span class="text-amber-400 font-extrabold">$2.50 / hour</span>
                            <button class="px-4 py-2 bg-amber-500 text-slate-950 text-xs font-bold rounded-lg hover:bg-amber-400">Rent Now</button>
                        </div>
                    </div>
                    <div class="bg-slate-900/80 border border-slate-800 rounded-2xl p-6 space-y-4">
                        <h3 class="text-xl font-bold text-white">Chimera Tool</h3>
                        <p class="text-xs text-slate-400">Professional tool for Samsung, Huawei & Xiaomi.</p>
                        <div class="flex justify-between items-center pt-4 border-t border-slate-800">
                            <span class="text-amber-400 font-extrabold">$3.00 / hour</span>
                            <button class="px-4 py-2 bg-amber-500 text-slate-950 text-xs font-bold rounded-lg hover:bg-amber-400">Rent Now</button>
                        </div>
                    </div>
                </div>
            </div>
        </section>

    </body>
    </html>
    """