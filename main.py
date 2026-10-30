from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles

app = FastAPI()

# static ፎልደርን ማገናኘት
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
    </head>
    <body class="bg-[#0b132b] text-slate-100 min-h-screen font-sans">

        <!-- Header / Navigation -->
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
        <section class="max-w-7xl mx-auto px-6 py-16 text-center md:text-left">
            <div class="grid lg:grid-cols-12 gap-12 items-center">
                <div class="lg:col-span-7 space-y-6">
                    <h1 class="text-4xl md:text-6xl font-black text-white leading-tight">
                        Buy, Sell & Rent <span class="text-amber-400">Digital Assets</span> & Repair Tools.
                    </h1>
                    <p class="text-lg text-slate-300">
                        Secure escrow platform for Telegram channels, TikTok, YouTube accounts, and hourly mobile repair tool rentals.
                    </p>
                    <div class="flex flex-wrap gap-4 justify-center md:justify-start">
                        <a href="#marketplace" class="px-7 py-3.5 bg-amber-500 text-slate-950 font-bold rounded-xl hover:bg-amber-400 transition shadow-lg">Explore Marketplace</a>
                        <a href="#toolRental" class="px-7 py-3.5 bg-slate-900 border border-slate-800 text-slate-200 font-semibold rounded-xl hover:bg-slate-800 transition">⚡ Rent Repair Tools</a>
                    </div>
                </div>
            </div>
        </section>

        <!-- Marketplace Categories -->
        <section id="marketplace" class="max-w-7xl mx-auto px-6 py-16 border-t border-slate-800">
            <h2 class="text-3xl font-extrabold text-white mb-8">Digital Asset Categories</h2>
            <div class="grid grid-cols-2 md:grid-cols-4 gap-6">
                <div class="p-6 bg-[#1c2541] border border-slate-700/60 rounded-2xl hover:border-amber-500 transition shadow-lg">
                    <div class="text-3xl mb-3">✈️</div>
                    <h3 class="font-bold text-white">Telegram</h3>
                    <p class="text-xs text-slate-400 mt-1">Channels, Groups & Bots</p>
                </div>
                <div class="p-6 bg-[#1c2541] border border-slate-700/60 rounded-2xl hover:border-amber-500 transition shadow-lg">
                    <div class="text-3xl mb-3">🎵</div>
                    <h3 class="font-bold text-white">TikTok</h3>
                    <p class="text-xs text-slate-400 mt-1">Accounts & Live Access</p>
                </div>
                <div class="p-6 bg-[#1c2541] border border-slate-700/60 rounded-2xl hover:border-amber-500 transition shadow-lg">
                    <div class="text-3xl mb-3">▶️</div>
                    <h3 class="font-bold text-white">YouTube</h3>
                    <p class="text-xs text-slate-400 mt-1">Monetized Channels</p>
                </div>
                <div class="p-6 bg-[#1c2541] border border-slate-700/60 rounded-2xl hover:border-amber-500 transition shadow-lg">
                    <div class="text-3xl mb-3">📘</div>
                    <h3 class="font-bold text-white">Facebook</h3>
                    <p class="text-xs text-slate-400 mt-1">Pages & Groups</p>
                </div>
                <div class="p-6 bg-[#1c2541] border border-slate-700/60 rounded-2xl hover:border-amber-500 transition shadow-lg">
                    <div class="text-3xl mb-3">📸</div>
                    <h3 class="font-bold text-white">Instagram</h3>
                    <p class="text-xs text-slate-400 mt-1">Active Accounts</p>
                </div>
                <div class="p-6 bg-[#1c2541] border border-slate-700/60 rounded-2xl hover:border-amber-500 transition shadow-lg">
                    <div class="text-3xl mb-3">🅧</div>
                    <h3 class="font-bold text-white">X (Twitter)</h3>
                    <p class="text-xs text-slate-400 mt-1">Verified Profiles</p>
                </div>
                <div class="p-6 bg-[#1c2541] border border-slate-700/60 rounded-2xl hover:border-amber-500 transition shadow-lg">
                    <div class="text-3xl mb-3">💼</div>
                    <h3 class="font-bold text-white">LinkedIn</h3>
                    <p class="text-xs text-slate-400 mt-1">Company & Profiles</p>
                </div>
                <div class="p-6 bg-[#1c2541] border border-slate-700/60 rounded-2xl hover:border-amber-500 transition shadow-lg">
                    <div class="text-3xl mb-3">🎮</div>
                    <h3 class="font-bold text-white">Gaming & Misc</h3>
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