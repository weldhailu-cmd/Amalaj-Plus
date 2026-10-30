from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse

app = FastAPI()

# Mount static folder so images can be served
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/", response_class=HTMLResponse)
def read_root():
    return """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Amalaj Plus - Modern & Secure Digital Asset Escrow</title>
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
                    <div class="w-10 h-10 rounded-full border-2 border-amber-500/80 overflow-hidden shadow-lg shadow-amber-500/20 bg-[#1c2541] flex items-center justify-center">
                        <img src="/static/amalaj-logo.png" alt="Amalaj Plus Logo" class="w-full h-full object-cover">
                    </div>
                    <span class="text-2xl font-extrabold text-white tracking-tight">Amalaj<span class="text-amber-400">Plus</span></span>
                </div>

                <!-- Desktop Nav Links with Acquire-style Mega Menus -->
                <div class="hidden md:flex items-center space-x-8 text-sm font-medium text-slate-300">
                    
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
                                        <h4 class="font-bold text-white group-hover/item:text-amber-400 transition">List Your Startup</h4>
                                        <p class="text-xs text-slate-400 mt-1">Create and publish your business listing to 500k+ buyers. Get expert tools & support.</p>
                                    </div>
                                </a>
                                <a href="#sellers" class="flex items-start space-x-4 p-4 rounded-xl hover:bg-slate-800/60 transition group/item">
                                    <div class="text-2xl p-3 bg-blue-500/10 text-blue-400 rounded-lg">🛡️</div>
                                    <div>
                                        <h4 class="font-bold text-white group-hover/item:text-amber-400 transition">Get help selling</h4>
                                        <p class="text-xs text-slate-400 mt-1">Acquisition advisory service tailored for founders. Get the highest price and terms.</p>
                                    </div>
                                </a>
                            </div>
                        </div>
                    </div>

                    <!-- Buyers -->
                    <a href="#buyers" class="hover:text-amber-400 transition py-2">Buyers</a>

                    <!-- Pricing Dropdown -->
                    <div class="static group">
                        <button class="flex items-center gap-1 hover:text-amber-400 transition py-2">
                            Pricing <span class="text-xs">▾</span>
                        </button>
                        <div class="absolute top-full left-0 w-full bg-[#1c2541] border-t border-b border-slate-700 shadow-2xl py-8 px-12 hidden group-hover:block z-50 transition-all">
                            <div class="max-w-7xl mx-auto grid grid-cols-2 gap-8">
                                <a href="#pricing" class="flex items-start space-x-4 p-4 rounded-xl hover:bg-slate-800/60 transition group/item">
                                    <div class="text-2xl p-3 bg-emerald-500/10 text-emerald-400 rounded-lg">💼</div>
                                    <div>
                                        <h4 class="font-bold text-white group-hover/item:text-amber-400 transition">Sellers</h4>
                                        <p class="text-xs text-slate-400 mt-1">Get acquired with an acquisition plan tailored to your exit goals. List and sell securely.</p>
                                    </div>
                                </a>
                                <a href="#pricing" class="flex items-start space-x-4 p-4 rounded-xl hover:bg-slate-800/60 transition group/item">
                                    <div class="text-2xl p-3 bg-purple-500/10 text-purple-400 rounded-lg">⭐</div>
                                    <div>
                                        <h4 class="font-bold text-white group-hover/item:text-amber-400 transition">Buyers</h4>
                                        <p class="text-xs text-slate-400 mt-1">View buyer plans that connect you with founders and startups. Connect to pursue acquisitions.</p>
                                    </div>
                                </a>
                            </div>
                        </div>
                    </div>

                    <!-- Resources Dropdown -->
                    <div class="static group">
                        <button class="flex items-center gap-1 hover:text-amber-400 transition py-2">
                            Resources <span class="text-xs">▾</span>
                        </button>
                        <div class="absolute top-full left-0 w-full bg-[#1c2541] border-t border-b border-slate-700 shadow-2xl py-8 px-12 hidden group-hover:block z-50 transition-all">
                            <div class="max-w-7xl mx-auto grid grid-cols-2 gap-8">
                                <a href="#help" onclick="openHelpCenter()" class="flex items-start space-x-4 p-4 rounded-xl hover:bg-slate-800/60 transition group/item">
                                    <div class="text-2xl p-3 bg-amber-500/10 text-amber-400 rounded-lg">❓</div>
                                    <div>
                                        <h4 class="font-bold text-white group-hover/item:text-amber-400 transition">Help center</h4>
                                        <p class="text-xs text-slate-400 mt-1">How to use Amalaj Plus and other questions answered. Get the most out of the marketplace.</p>
                                    </div>
                                </a>
                                <a href="#blog" class="flex items-start space-x-4 p-4 rounded-xl hover:bg-slate-800/60 transition group/item">
                                    <div class="text-2xl p-3 bg-blue-500/10 text-blue-400 rounded-lg">📰</div>
                                    <div>
                                        <h4 class="font-bold text-white group-hover/item:text-amber-400 transition">Blog</h4>
                                        <p class="text-xs text-slate-400 mt-1">Learn how to buy, grow, and sell businesses. Become an acquisition expert in no time.</p>
                                    </div>
                                </a>
                            </div>
                        </div>
                    </div>

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
                            <a href="#blog" class="block px-4 py-2.5 text-sm text-slate-700 hover:bg-slate-100 transition">Blog</a>
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
                        <span id="badgeText">Trusted & Secure Escrow Platform</span>
                    </div>

                    <h1 id="heroTitle" class="text-4xl md:text-6xl font-black tracking-tight text-white leading-tight">
                        The modern & trusted marketplace to <span class="text-amber-400">buy and sell</span> digital assets.
                    </h1>

                    <p id="heroDesc" class="text-lg text-slate-300 max-w-xl leading-relaxed">
                        Seamlessly transfer Telegram channels, TikTok accounts, YouTube channels, and websites with 100% verified escrow protection.
                    </p>

                    <div class="flex flex-wrap items-center gap-4 pt-2">
                        <a href="/docs" id="btnPrimary" class="px-7 py-3.5 bg-amber-500 text-slate-950 font-bold rounded-xl hover:bg-amber-400 transition shadow-lg shadow-amber-500/20 flex items-center gap-2">
                            View Listings &rarr;
                        </a>
                        <a href="#how-it-works" id="btnSecondary" class="px-7 py-3.5 bg-slate-900 border border-slate-800 text-slate-200 font-semibold rounded-xl hover:bg-slate-800 hover:border-slate-700 transition flex items-center gap-2">
                            ▶ How Escrow Works
                        </a>
                    </div>

                    <div class="pt-6 border-t border-slate-800/80 flex items-center gap-6 text-sm text-slate-400">
                        <div class="flex items-center gap-1 text-amber-400">★★★★★</div>
                        <span id="trustText">Safe transactions & Instant asset delivery guaranteed</span>
                    </div>
                </div>

                <div class="lg:col-span-5 relative">
                    <div class="relative mx-auto w-full max-w-md">
                        <div class="bg-[#1c2541] border border-slate-700/60 rounded-2xl p-6 shadow-2xl relative z-10 space-y-4">
                            <div class="flex items-center justify-between">
                                <div class="flex items-center space-x-3">
                                    <div class="w-10 h-10 rounded-lg bg-blue-600/20 text-blue-400 flex items-center justify-center font-bold text-lg">✈</div>
                                    <div>
                                        <h4 class="font-bold text-white text-sm">Telegram Channel</h4>
                                        <p class="text-xs text-slate-400">45.2K Subscribers</p>
                                    </div>
                                </div>
                                <span class="px-2.5 py-1 bg-emerald-500/10 text-emerald-400 border border-emerald-500/20 text-xs font-semibold rounded-full">$1,500 USD</span>
                            </div>

                            <div class="space-y-2 pt-2 border-t border-slate-800 text-xs">
                                <div class="flex justify-between text-slate-400">
                                    <span>Escrow Status:</span>
                                    <span class="text-amber-400 font-medium">Payment Secured ✓</span>
                                </div>
                                <div class="w-full bg-slate-900 rounded-full h-2 overflow-hidden">
                                    <div class="bg-amber-400 h-full w-3/4 rounded-full"></div>
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
                            <div class="w-8 h-8 rounded-full bg-purple-500/20 text-purple-400 flex items-center justify-center font-bold text-xs">🎵</div>
                            <div>
                                <p class="text-[11px] font-semibold text-white">TikTok Account</p>
                                <p class="text-[10px] text-slate-400">Verified Transfer</p>
                            </div>
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
                
                <div class="max-w-2xl mx-auto mt-6">
                    <div class="relative">
                        <input type="text" placeholder="Search for answers (e.g., buying escrow, account transfer)..." class="w-full px-5 py-4 bg-[#1c2541] border border-slate-700 rounded-2xl text-white placeholder-slate-400 focus:outline-none focus:border-amber-500 shadow-xl">
                        <span class="absolute right-4 top-4 text-slate-400 text-xl">🔍</span>
                    </div>
                </div>
            </div>

            <div class="grid md:grid-cols-2 gap-6 mt-12">
                <div class="p-6 bg-[#1c2541] border border-slate-700/60 rounded-2xl hover:border-amber-500/50 transition shadow-lg space-y-2">
                    <div class="text-amber-400 text-2xl mb-2">💰</div>
                    <h3 class="text-xl font-bold text-white">Buying</h3>
                    <p class="text-slate-400 text-sm">ንብረት ሲገዙ የሚደረግ እርዳታ እና የእስክሮው አጠቃቀም ስርዓት።</p>
                </div>
                <div class="p-6 bg-[#1c2541] border border-slate-700/60 rounded-2xl hover:border-amber-500/50 transition shadow-lg space-y-2">
                    <div class="text-amber-400 text-2xl mb-2">🏷️</div>
                    <h3 class="text-xl font-bold text-white">Selling</h3>
                    <p class="text-slate-400 text-sm">ንብረት ሲሸጡ እና ቻናሎችን/አካውንቶችን በሰላም ሲያዛውሩ የሚደረግ እርዳታ።</p>
                </div>
                <div class="p-6 bg-[#1c2541] border border-slate-700/60 rounded-2xl hover:border-amber-500/50 transition shadow-lg space-y-2">
                    <div class="text-amber-400 text-2xl mb-2">⚙️</div>
                    <h3 class="text-xl font-bold text-white">Account</h3>
                    <p class="text-slate-400 text-sm">አካውንት አስተዳደር፣ የደህንነት ቅንብሮች እና የመግቢያ መረጃዎች።</p>
                </div>
                <div class="p-6 bg-[#1c2541] border border-slate-700/60 rounded-2xl hover:border-amber-500/50 transition shadow-lg space-y-2">
                    <div class="text-amber-400 text-2xl mb-2">📊</div>
                    <h3 class="text-xl font-bold text-white">Resources</h3>
                    <p class="text-slate-400 text-sm">ነፃ አጋዥ ዳታዎች፣ ቼክሊስቶች እና የግብይት መመሪያዎች።</p>
                </div>
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
                document.getElementById('helpCenterSection').classList.remove('hidden');
                document.getElementById('dropdownMenu').classList.add('hidden');
            }

            function closeHelpCenter() {
                document.getElementById('helpCenterSection').classList.add('hidden');
                document.getElementById('mainHero').classList.remove('hidden');
            }

            let currentLang = 'en';
            const translations = {
                en: {
                    langBtn: 'አማርኛ',
                    badge: 'Trusted & Secure Escrow Platform',
                    heroTitle: 'The modern & trusted marketplace to <span class="text-amber-400">buy and sell</span> digital assets.',
                    heroDesc: 'Seamlessly transfer Telegram channels, TikTok accounts, YouTube channels, and websites with 100% verified escrow protection.',
                    btnPrimary: 'View Listings &rarr;',
                    btnSecondary: '▶ How Escrow Works',
                    trustText: 'Safe transactions & Instant asset delivery guaranteed'
                },
                am: {
                    langBtn: 'English',
                    badge: 'ደህንነቱ የተጠበቀ የእስክሮው ገበያ',
                    heroTitle: 'ዲጂታል ንብረቶችዎን <span class="text-amber-400">በእስተማማኝ</span> የሚገበያዩበት ዘመናዊ ፕላትፎርም',
                    heroDesc: 'የቴሌግራም ቻናሎች፣ የቲክቶክ አካውንቶች፣ ዩቲዩብ ቻናሎች እና ዌብሳይቶችን በአስተማማኝ የእስክሮው (Escrow) ዋስትና ይለዋወጡ።',
                    btnPrimary: 'ዝርዝሩን ይመልከቱ &rarr;',
                    btnSecondary: '▶ እስክሮው እንዴት ይሰራል?',
                    trustText: 'ሙሉ ዋስትና ያለው የታመነ የዲጂታል ንብረት ዝውውር'
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