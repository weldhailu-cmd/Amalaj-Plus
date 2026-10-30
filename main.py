from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

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
        <header class="border-b border-slate-800 bg-[#0b132b]/90 backdrop-blur sticky top-0 z-50">
            <div class="max-w-7xl mx-auto px-6 py-4 flex justify-between items-center">
                <div class="flex items-center space-x-3">
                    <div class="w-9 h-9 bg-amber-500 rounded-xl flex items-center justify-center font-black text-slate-950 text-xl shadow-lg shadow-amber-500/20">A</div>
                    <span class="text-2xl font-extrabold text-white tracking-tight">Amalaj<span class="text-amber-400">Plus</span></span>
                </div>

                <div class="flex items-center space-x-6">
                    <nav class="hidden md:flex space-x-6 text-sm font-medium text-slate-300">
                        <a href="#features" class="hover:text-amber-400 transition">Features</a>
                        <a href="#how-it-works" class="hover:text-amber-400 transition">How it Works</a>
                        <a href="/docs" target="_blank" class="hover:text-amber-400 transition">API Docs</a>
                    </nav>

                    <!-- Language Switcher & Actions -->
                    <div class="flex items-center space-x-3">
                        <button onclick="toggleLanguage()" id="langBtn" class="text-xs px-3 py-1.5 border border-slate-700 bg-slate-900 rounded-lg text-slate-300 hover:border-amber-500/50 transition flex items-center gap-1.5">
                            🌐 <span id="langText">አማርኛ</span>
                        </button>
                        <a href="/docs" class="text-xs font-semibold px-4 py-2 bg-amber-500 text-slate-950 rounded-lg hover:bg-amber-400 transition shadow-md shadow-amber-500/10">Get Started</a>
                    </div>
                </div>
            </div>
        </header>

        <!-- Hero Section -->
        <section class="max-w-7xl mx-auto px-6 py-16 md:py-24">
            <div class="grid lg:grid-cols-12 gap-12 items-center">
                
                <!-- Left Column: Text & CTA -->
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

                    <!-- CTA Buttons -->
                    <div class="flex flex-wrap items-center gap-4 pt-2">
                        <a href="/docs" id="btnPrimary" class="px-7 py-3.5 bg-amber-500 text-slate-950 font-bold rounded-xl hover:bg-amber-400 transition shadow-lg shadow-amber-500/20 flex items-center gap-2">
                            View Listings &rarr;
                        </a>
                        <a href="#how-it-works" id="btnSecondary" class="px-7 py-3.5 bg-slate-900 border border-slate-800 text-slate-200 font-semibold rounded-xl hover:bg-slate-800 hover:border-slate-700 transition flex items-center gap-2">
                            ▶ How Escrow Works
                        </a>
                    </div>

                    <!-- Trust Stats -->
                    <div class="pt-6 border-t border-slate-800/80 flex items-center gap-6 text-sm text-slate-400">
                        <div class="flex items-center gap-1 text-amber-400">
                            ★★★★★
                        </div>
                        <span id="trustText">Safe transactions & Instant asset delivery guaranteed</span>
                    </div>
                </div>

                <!-- Right Column: Interactive Visual / Mockup (acquire.com style) -->
                <div class="lg:col-span-5 relative">
                    <div class="relative mx-auto w-full max-w-md">
                        <!-- Main Card -->
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

                        <!-- Floating Badge 1 (Top Right) -->
                        <div class="floating-card absolute -top-6 -right-4 bg-slate-900/90 backdrop-blur border border-amber-500/30 rounded-xl p-3 shadow-xl z-20 flex items-center gap-3">
                            <div class="w-8 h-8 rounded-full bg-amber-500/20 text-amber-400 flex items-center justify-center font-bold text-xs">🛡️</div>
                            <div>
                                <p class="text-[11px] font-semibold text-white">Escrow Protection</p>
                                <p class="text-[10px] text-slate-400">100% Funds Secured</p>
                            </div>
                        </div>

                        <!-- Floating Badge 2 (Bottom Left) -->
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

        <!-- Script for Language Toggle -->
        <script>
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