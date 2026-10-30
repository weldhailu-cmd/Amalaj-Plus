from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles

app = FastAPI()

# staticfiles ን ማገናኘት
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/", response_class=HTMLResponse)
def read_root():
    return """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Amalaj Plus - Modern & Secure Digital Asset & Tool Rental Escrow</title>
        <script src="https://cdn.tailwindcss.com"></script>
        <style>
            @keyframes float {
                0% { transform: translateY(0px); }
                50% { transform: translateY(-10px); }
                100% { transform: translateY(0px); }
            }
            .floating-card {
                animation: float 4s ease-in-out infinite;
            }
        </style>
    </head>
    <body class="bg-[#0b132b] text-slate-100 min-h-screen font-sans selection:bg-amber-500 selection:text-slate-950">

        <!-- Header / Navigation -->
        <header class="border-b border-slate-800 bg-[#0b132b]/95 backdrop-blur sticky top-0 z-50">
            <div class="max-w-7xl mx-auto px-6 py-4 flex justify-between items-center relative">
                <!-- Circular Logo & Branding -->
                <div class="flex items-center space-x-3">
                    <div class="w-10 h-10 rounded-full border-2 border-amber-500 overflow-hidden shadow-lg shadow-amber-500/20 bg-[#1c2541] flex items-center justify-center">
                        <img src="/static/logo.png" alt="Amalaj Plus Logo" class="w-full h-full object-cover">
                    </div>
                    <span class="text-2xl font-extrabold text-white tracking-tight">Amalaj<span class="text-amber-400">Plus</span></span>
                </div>

                <!-- Desktop Nav Links -->
                <div class="hidden md:flex items-center space-x-8 text-sm font-medium text-slate-300">
                    <a href="#marketplace" class="hover:text-amber-400 transition py-2">Marketplace</a>
                    <a href="#toolRental" class="hover:text-amber-400 transition py-2 text-amber-400 font-semibold">Tool Rental ⚡</a>
                    
                    <!-- Sellers Dropdown -->
                    <div class="static group">
                        <button class="flex items-center gap-1 hover:text-amber-400 transition py-2">
                            Sellers <span class="text-xs">▾</span>
                        </button>
                        <div class="absolute top-full left-0 w-full bg-[#1c2541] border-t border-b border-slate-700 shadow-2xl py-8 px-12 hidden group-hover:block z-50 transition-all">
                            <div class="max-w-7xl mx-auto grid grid-cols-2 gap-8">
                                <a href="#sellers" class="flex items-start space-x-4 p-4 rounded-xl hover:bg-slate-800/60 transition group/item">
                                    <div class="text-2xl p-3 bg-amber-500/10 text-amber-400 rounded-lg">🏷️</div>
                                    <div>
                                        <h4 class="font-bold text-white group-hover/item:text-amber-400 transition">List Your Asset</h4>
                                        <p class="text-xs text-slate-400 mt-1">Create and publish your digital listing or software tool to buyers safely.</p>
                                    </div>
                                </a>
                                <a href="#sellers" class="flex items-start space-x-4 p-4 rounded-xl hover:bg-slate-800/60 transition group/item">
                                    <div class="text-2xl p-3 bg-blue-500/10 text-blue-400 rounded-lg">🛡️</div>
                                    <div>
                                        <h4 class="font-bold text-white group-hover/item:text-amber-400 transition">Get Help Selling</h4>
                                        <p class="text-xs text-slate-400 mt-1">Escrow advisory service tailored for secure account & channel transfers.</p>
                                    </div>
                                </a>
                            </div>
                        </div>
                    </div>

                    <a href="#help" onclick="openHelpCenter()" class="hover:text-amber-400 transition py-2">Help Center</a>
                </div>

                <!-- Right Actions: Language & User Menu -->
                <div class="flex items-center space-x-4">
                    <!-- Language Switcher -->
                    <button onclick="toggleLanguage()" id="langBtn" class="text-xs px-3 py-1.5 border border-slate-700 bg-slate-900 rounded-lg text-slate-300 hover:border-amber-500/50 transition flex items-center gap-1.5">
                        🌐 <span id="langText">አማርኛ</span>
                    </button>

                    <!-- User Menu Dropdown -->
                    <div class="relative">
                        <button onclick="toggleMenu()" class="flex items-center space-x-2 bg-[#1c2541] border border-slate-700 hover:border-amber-500/50 px-3 py-1.5 rounded-xl transition shadow-md">
                            <svg class="w-5 h-5 text-slate-300" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16M4 18h16"></path>
                            </svg>
                            <div class="w-7 h-7 bg-amber-500/20 text-amber-400 rounded-full flex items-center justify-center text-xs font-bold">
                                👤
                            </div>
                        </button>

                        <div id="dropdownMenu" class="hidden absolute right-0 mt-2 w-48 bg-white text-slate-900 rounded-2xl shadow-2xl py-2 z-50 border border-slate-200">
                            <a href="/docs" class="block px-4 py-2.5 text-sm font-semibold hover:bg-slate-100 transition">Join now</a>
                            <a href="/docs" class="block px-4 py-2.5 text-sm font-semibold hover:bg-slate-100 transition">Log In</a>
                            <div class="border-t border-slate-200 my-1"></div>
                            <a href="#help" onclick="openHelpCenter()" class="block px-4 py-2.5 text-sm text-slate-700 hover:bg-slate-100 transition">Help center</a>
                        </div>
                    </div>
                </div>
            </div>
        </header>

        <!-- Hero Section -->
        <section id="mainHero" class="max-w-7xl mx-auto px-6 py-16 md:py-24">
            <div class="grid lg:grid-cols-12 gap-12 items-center">
                
                <div class="lg:col-span-7 space-y-8">
                    <div class="inline-flex items-center gap-2 px-3 py-1.5 bg-amber-500/10 border border-amber-500/30 rounded-full text-xs font-medium text-amber-400">
                        <span class="w-2 h-2 rounded-full bg-amber-400 animate-pulse"></span>
                        <span id="badgeText">Trusted & Secure Escrow & Tool Rental Platform</span>
                    </div>

                    <h1 id="heroTitle" class="text-4xl md:text-6xl font-black tracking-tight text-white leading-tight">
                        The ultimate marketplace to <span class="text-amber-400">buy, sell & rent</span> digital assets & repair tools.
                    </h1>

                    <p id="heroDesc" class="text-lg text-slate-300 max-w-xl leading-relaxed">
                        Seamlessly transfer Telegram channels, TikTok accounts, YouTube channels, Facebook pages & groups, Instagram, and rent mobile repair tools securely.
                    </p>

                    <div class="flex flex-wrap items-center gap-4 pt-2">
                        <a href="#marketplace" id="btnPrimary" class="px-7 py-3.5 bg-amber-500 text-slate-950 font-bold rounded-xl hover:bg-amber-400 transition shadow-lg shadow-amber-500/20 flex items-center gap-2">
                            Explore Marketplace &rarr;
                        </a>
                        <a href="#toolRental" id="btnSecondary" class="px-7 py-3.5 bg-slate-900 border border-slate-800 text-slate-200 font-semibold rounded-xl hover:bg-slate-800 hover:border-slate-700 transition flex items-center gap-2">
                            ⚡ Rent Repair Tools
                        </a>
                    </div>

                    <div class="pt-6 border-t border-slate-800/80 flex items-center gap-6 text-sm text-slate-400">
                        <div class="flex items-center gap-1 text-amber-400">★★★★★</div>
                        <span id="trustText">Safe escrow transactions & Instant tool delivery guaranteed</span>
                    </div>
                </div>

                <div class="lg:col-span-5 relative">
                    <div class="relative mx-auto w-full max-w-md">
                        <div class="bg-[#1c2541] border border-slate-700/60 rounded-2xl p-6 shadow-2xl relative z-10 space-y-4">
                            <div class="flex items-center justify-between">
                                <div class="flex items-center space-x-3">
                                    <div class="w-10 h-10 rounded-lg bg-blue-600/20 text-blue-400 flex items-center justify-center font-bold text-lg">⚡</div>
                                    <div>
                                        <h4 class="font-bold text-white text-sm">Hourly Tool Rental</h4>
                                        <p class="text-xs text-slate-400">UnlockTool / DFT Pro</p>
                                    </div>
                                </div>
                                <span class="px-2.5 py-1 bg-emerald-500/10 text-emerald-400 border border-emerald-500/20 text-xs font-semibold rounded-full">$2.00 / hr</span>
                            </div>

                            <div class="space-y-2 pt-2 border-t border-slate-800 text-xs">
                                <div class="flex justify-between text-slate-400">
                                    <span>Rental Status:</span>
                                    <span class="text-amber-400 font-medium">Instant Access Ready ✓</span>
                                </div>
                                <div class="w-full bg-slate-900 rounded-full h-2 overflow-hidden">
                                    <div class="bg-amber-400 h-full w-full rounded-full animate-pulse"></div>
                                </div>
                            </div>
                        </div>

                        <div class="floating-card absolute -top-6 -right-4 bg-slate-900/90 backdrop-blur border border-amber-500/30 rounded-xl p-3 shadow-xl z-20 flex items-center gap-3">
                            <div class="w-8 h-8 rounded-full bg-amber-500/20 text-amber-400 flex items-center justify-center font-bold text-xs">🛡️</div>
                            <div>
                                <p class="text-[11px] font-semibold text-white">Escrow Protection</p>
                                <p class="text-[10px] text-slate-400">100% Funds Secured</p>
                            </div>
                        </div>

                        <div class="floating-card absolute -bottom-6 -left-4 bg-slate-900/90 backdrop-blur border border-slate-700 rounded-xl p-3 shadow-xl z-20 flex items-center gap-3" style="animation-delay: -2s;">
                            <div class="w-8 h-8 rounded-full bg-blue-500/20 text-blue-400 flex items-center justify-center font-bold text-xs">✈️</div>
                            <div>
                                <p class="text-[11px] font-semibold text-white">Telegram & Socials</p>
                                <p class="text-[10px] text-slate-400">Verified Transfer</p>
                            </div>
                        </div>
                    </div>
                </div>

            </div>
        </section>

        <!-- Marketplace Categories Section -->
        <section id="marketplace" class="max-w-7xl mx-auto px-6 py-16 border-t border-slate-800">
            <div class="mb-12">
                <h2 class="text-3xl font-extrabold text-white tracking-tight">Digital Asset Categories</h2>
                <p class="text-slate-400 mt-2">Explore verified social media channels, groups, and accounts available for secure escrow exchange.</p>
            </div>

            <div class="grid grid-cols-2 md:grid-cols-4 gap-6">
                <div class="p-6 bg-[#1c2541] border border-slate-700/60 rounded-2xl hover:border-amber-500 transition group cursor-pointer shadow-lg">
                    <div class="text-3xl mb-3">✈️</div>
                    <h3 class="font-bold text-white group-hover:text-amber-400 transition">Telegram</h3>
                    <p class="text-xs text-slate-400 mt-1">Channels, Groups & Bots</p>
                </div>
                <div class="p-6 bg-[#1c2541] border border-slate-700/60 rounded-2xl hover:border-amber-500 transition group cursor-pointer shadow-lg">
                    <div class="text-3xl mb-3">🎵</div>
                    <h3 class="font-bold text-white group-hover:text-amber-400 transition">TikTok</h3>
                    <p class="text-xs text-slate-400 mt-1">Accounts & Live Access</p>
                </div>
                <div class="p-6 bg-[#1c2541] border border-slate-700/60 rounded-2xl hover:border-amber-500 transition group cursor-pointer shadow-lg">
                    <div class="text-3xl mb-3">▶️</div>
                    <h3 class="font-bold text-white group-hover:text-amber-400 transition">YouTube</h3>
                    <p class="text-xs text-slate-400 mt-1">Monetized Channels</p>
                </div>
                <div class="p-6 bg-[#1c2541] border border-slate-700/60 rounded-2xl hover:border-amber-500 transition group cursor-pointer shadow-lg">
                    <div class="text-3xl mb-3">📘</div>
                    <h3 class="font-bold text-white group-hover:text-amber-400 transition">Facebook</h3>
                    <p class="text-xs text-slate-400 mt-1">Pages & Community Groups</p>
                </div>
                <div class="p-6 bg-[#1c2541] border border-slate-700/60 rounded-2xl hover:border-amber-500 transition group cursor-pointer shadow-lg">
                    <div class="text-3xl mb-3">📸</div>
                    <h3 class="font-bold text-white group-hover:text-amber-400 transition">Instagram</h3>
                    <p class="text-xs text-slate-400 mt-1">Active Accounts</p>
                </div>
                <div class="p-6 bg-[#1c2541] border border-slate-700/60 rounded-2xl hover:border-amber-500 transition group cursor-pointer shadow-lg">
                    <div class="text-3xl mb-3">🅧</div>
                    <h3 class="font-bold text-white group-hover:text-amber-400 transition">X (Twitter)</h3>
                    <p class="text-xs text-slate-400 mt-1">Verified & Aged Profiles</p>
                </div>
                <div class="p-6 bg-[#1c2541] border border-slate-700/60 rounded-2xl hover:border-amber-500 transition group cursor-pointer shadow-lg">
                    <div class="text-3xl mb-3">💼</div>
                    <h3 class="font-bold text-white group-hover:text-amber-400 transition">LinkedIn</h3>
                    <p class="text-xs text-slate-400 mt-1">Company & Profiles</p>
                </div>
                <div class="p-6 bg-[#1c2541] border border-slate-700/60 rounded-2xl hover:border-amber-500 transition group cursor-pointer shadow-lg">
                    <div class="text-3xl mb-3">🎮</div>
                    <h3 class="font-bold text-white group-hover:text-amber-400 transition">Gaming & Misc</h3>
                    <p class="text-xs text-slate-400 mt-1">PUBG, Discord & More</p>
                </div>
            </div>
        </section>

        <!-- Software Tool Rental Section -->
        <section id="toolRental" class="max-w-7xl mx-auto px-6 py-16 border-t border-slate-800">
            <div class="bg-gradient-to-r from-blue-950/60 to-[#1c2541] border border-amber-500/30 rounded-3xl p-8 md:p-12 shadow-2xl">
                <div class="max-w-2xl mb-10">
                    <span class="px-3 py-1 bg-amber-500/10 text-amber-400 border border-amber-500/30 rounded-full text-xs font-bold uppercase tracking-wider">Hourly & Daily Rental for Technicians</span>
                    <h2 class="text-3xl md:text-4xl font-black text-white mt-4">Professional Repair Tool Rentals</h2>
                    <p class="text-slate-300 mt-2">Rent official mobile repair software licenses by the hour. Affordable access for technicians across all cities.</p>
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

        <!-- Help Center View Section -->
        <section id="helpCenterSection" class="hidden max-w-5xl mx-auto px-6 py-16">
            <div class="text-center space-y-4 mb-12">
                <button onclick="closeHelpCenter()" class="text-xs px-4 py-2 bg-slate-800 text-slate-300 rounded-lg hover:bg-slate-700 mb-4">&larr; ወደ ዋናው ገጽ ተመለስ</button>
                <h1 class="text-4xl font-extrabold text-white">How can we help?</h1>
                <p class="text-slate-400">የሚፈልጉትን እርዳታ ወይም ጥያቄ እዚህ ይፈልጉ</p>
            </div>
        </section>

        <!-- Scripts -->
        <script>
            function toggleMenu() {
                const menu = document.getElementById('dropdownMenu');
                menu.classList.toggle('hidden');
            }

            window.addEventListener('click', function(e) {
                const menu = document.getElementById('dropdownMenu');
                const btn = e.target.closest('button');
                if (!btn && !menu.contains(e.target)) {
                    menu.classList.add('hidden');
                }
            });

            function openHelpCenter() {
                document.getElementById('mainHero').classList.add('hidden');
                document.getElementById('marketplace').classList.add('hidden');
                document.getElementById('toolRental').classList.add('hidden');
                document.getElementById('helpCenterSection').classList.remove('hidden');
                document.getElementById('dropdownMenu').classList.add('hidden');
            }

            function closeHelpCenter() {
                document.getElementById('helpCenterSection').classList.add('hidden');
                document.getElementById('mainHero').classList.remove('hidden');
                document.getElementById('marketplace').classList.remove('hidden');
                document.getElementById('toolRental').classList.remove('hidden');
            }

            let currentLang = 'en';
            const translations = {
                en: {
                    langBtn: 'አማርኛ',
                    badge: 'Trusted & Secure Escrow & Tool Rental Platform',
                    heroTitle: 'The ultimate marketplace to <span class="text-amber-400">buy, sell & rent</span> digital assets & repair tools.',
                    heroDesc: 'Seamlessly transfer Telegram channels, TikTok accounts, YouTube channels, Facebook pages & groups, Instagram, and rent mobile repair tools securely.',
                    btnPrimary: 'Explore Marketplace &rarr;',
                    btnSecondary: '⚡ Rent Repair Tools',
                    trustText: 'Safe escrow transactions & Instant tool delivery guaranteed'
                },
                am: {
                    langBtn: 'English',
                    badge: 'ደህንነቱ የተጠበቀ የእስክሮው እና የቱል አከራይ ፕላትፎርም',
                    heroTitle: 'ዲጂታል ንብረቶችዎን እና የጥገና ቱሎችዎን <span class="text-amber-400">በእስተማማኝ</span> የሚገበያዩበት እና የሚያከራዩበት ፕላትፎርም',
                    heroDesc: 'የቴሌግራም ቻናሎች፣ የቲክቶክ አካውንቶች፣ ዩቲዩብ፣ ፌስቡክ ፔጆች እና ግሩፖች፣ ኢንስታግራም እና የሞባይል ሶፍትዌር ቱሎችን በአስተማማኝ ዋስትና ይለዋወጡ።',
                    btnPrimary: 'ገበያውን ያስሱ &rarr;',
                    btnSecondary: '⚡ ቱሎችን አከራይ',
                    trustText: 'ሙሉ ዋስትና ያለው የታመነ የዲጂታል ንብረት እና የቱል ዝውውር'
                }
            };

            function toggleLanguage() {
                currentLang = currentLang === 'en' ? 'am' : 'en';
                const t = translations[currentLang];
                
                document.getElementById('langText').innerText = t.langBtn;
                document.getElementById('badgeText').innerText = t.badge;
                document.getElementById('heroTitle').innerHTML = t.heroTitle;
                document.getElementById('heroDesc').innerText = t.heroDesc;
                document.getElementById('btnPrimary').innerHTML = t.btnPrimary;
                document.getElementById('btnSecondary').innerText = t.btnSecondary;
                document.getElementById('trustText').innerText = t.trustText;
            }
        </script>
    </body>
    </html>
    """