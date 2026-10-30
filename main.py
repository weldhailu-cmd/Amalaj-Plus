from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/auth/google")
def google_auth_placeholder():
    return {"message": "Google Authentication integration will be connected here."}

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

                <!-- Right Actions: Dynamic User Profile or Sign In/Sign Up -->
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

        <!-- Hero Section -->
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
                <!-- Hero Card -->
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
                            <button onclick="openAuthModal('signin')" class="w-full py-2.5 bg-amber-500 text-slate-950 font-bold rounded-xl text-xs hover:bg-amber-400 transition cursor-pointer">Approve Escrow Request</button>
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
                <div class="p-6 bg-[#16203a] border border-slate-700/60 rounded-2xl hover:border-[#229ED9] transition-all group shadow-xl">
                    <div class="w-12 h-12 rounded-xl bg-[#229ED9]/20 text-[#229ED9] flex items-center justify-center text-2xl mb-4"><i class="fa-brands fa-telegram"></i></div>
                    <h3 class="font-bold text-white text-lg">Telegram</h3>
                    <p class="text-xs text-slate-400 mt-1">Channels, Groups & Bots</p>
                </div>
                <div class="p-6 bg-[#16203a] border border-slate-700/60 rounded-2xl hover:border-[#EE1D52] transition-all group shadow-xl">
                    <div class="w-12 h-12 rounded-xl bg-[#EE1D52]/20 text-[#EE1D52] flex items-center justify-center text-2xl mb-4"><i class="fa-brands fa-tiktok"></i></div>
                    <h3 class="font-bold text-white text-lg">TikTok</h3>
                    <p class="text-xs text-slate-400 mt-1">Accounts & Live Access</p>
                </div>
                <div class="p-6 bg-[#16203a] border border-slate-700/60 rounded-2xl hover:border-[#FF0000] transition-all group shadow-xl">
                    <div class="w-12 h-12 rounded-xl bg-[#FF0000]/20 text-[#FF0000] flex items-center justify-center text-2xl mb-4"><i class="fa-brands fa-youtube"></i></div>
                    <h3 class="font-bold text-white text-lg">YouTube</h3>
                    <p class="text-xs text-slate-400 mt-1">Monetized Channels</p>
                </div>
                <div class="p-6 bg-[#16203a] border border-slate-700/60 rounded-2xl hover:border-[#1877F2] transition-all group shadow-xl">
                    <div class="w-12 h-12 rounded-xl bg-[#1877F2]/20 text-[#1877F2] flex items-center justify-center text-2xl mb-4"><i class="fa-brands fa-facebook"></i></div>
                    <h3 class="font-bold text-white text-lg">Facebook</h3>
                    <p class="text-xs text-slate-400 mt-1">Pages & Community Groups</p>
                </div>
            </div>
        </section>

        <!-- Authentication Modal -->
        <div id="authModal" class="fixed inset-0 bg-black/80 backdrop-blur-sm z-50 hidden flex items-center justify-center p-4">
            <div class="bg-[#1c2541] border border-slate-700 rounded-3xl max-w-md w-full p-8 relative shadow-2xl space-y-6">
                <!-- Close Button -->
                <button onclick="closeAuthModal()" class="absolute top-5 right-5 text-slate-400 hover:text-white text-xl cursor-pointer">
                    <i class="fa-solid fa-xmark"></i>
                </button>

                <!-- Header -->
                <div class="text-center space-y-2">
                    <h3 id="modalTitle" class="text-2xl font-black text-white">Create Account</h3>
                    <p id="modalSubtitle" class="text-xs text-slate-400">Join Amalaj Plus Ethiopian Marketplace</p>
                </div>

                <!-- Google Sign-In Button -->
                <button onclick="handleGoogleAuth()" class="w-full bg-white hover:bg-slate-100 text-slate-900 font-bold py-3 px-4 rounded-xl flex items-center justify-center space-x-3 transition shadow-lg text-sm cursor-pointer">
                    <i class="fa-brands fa-google text-red-500 text-lg"></i>
                    <span>Sign in with Google</span>
                </button>

                <!-- Divider -->
                <div class="relative flex py-1 items-center">
                    <div class="flex-grow border-t border-slate-700"></div>
                    <span class="flex-shrink mx-4 text-xs text-slate-500 uppercase">Or</span>
                    <div class="flex-grow border-t border-slate-700"></div>
                </div>

                <!-- Error Message Alert Box -->
                <div id="formErrorBox" class="hidden bg-red-500/10 border border-red-500/50 text-red-400 text-xs p-3 rounded-xl text-center"></div>

                <!-- Form Fields -->
                <form id="authForm" onsubmit="handleFormSubmit(event)" class="space-y-4">
                    <div id="fullNameGroup">
                        <label class="block text-xs font-semibold text-slate-300 mb-1">Full Name</label>
                        <input type="text" id="fullNameInput" placeholder="Hailewelde Kidan" class="w-full bg-slate-900 border border-slate-700 rounded-xl px-4 py-2.5 text-sm text-white focus:outline-none focus:border-amber-500">
                    </div>

                    <div>
                        <label class="block text-xs font-semibold text-slate-300 mb-1">Email address</label>
                        <input type="email" id="emailInput" required placeholder="you@example.com" class="w-full bg-slate-900 border border-slate-700 rounded-xl px-4 py-2.5 text-sm text-white focus:outline-none focus:border-amber-500">
                    </div>

                    <!-- Password Field with Show/Hide Eye Icon -->
                    <div>
                        <label class="block text-xs font-semibold text-slate-300 mb-1">Password</label>
                        <div class="relative">
                            <input type="password" id="passwordInput" required placeholder="••••••••" class="w-full bg-slate-900 border border-slate-700 rounded-xl px-4 py-2.5 text-sm text-white focus:outline-none focus:border-amber-500 pr-10">
                            <button type="button" onclick="togglePassword('passwordInput', 'eyeIcon1')" class="absolute right-3 top-3 text-slate-400 hover:text-white text-xs cursor-pointer">
                                <i id="eyeIcon1" class="fa-solid fa-eye"></i>
                            </button>
                        </div>
                    </div>

                    <!-- Confirm Password Field (Only for Sign Up) -->
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

                <!-- Switch Mode Link -->
                <div class="text-center text-xs text-slate-400">
                    <span id="switchText">Already have an account?</span>
                    <button onclick="toggleAuthMode()" id="switchBtn" class="text-amber-400 font-bold hover:underline ml-1 cursor-pointer">Sign In</button>
                </div>
            </div>
        </div>

        <!-- JavaScript Logic with Strict Validation -->
        <script>
            let currentMode = 'signup';

            function openAuthModal(mode) {
                currentMode = mode;
                const modal = document.getElementById('authModal');
                modal.classList.remove('hidden');
                document.getElementById('formErrorBox').classList.add('hidden');
                updateModalUI();
            }

            function closeAuthModal() {
                document.getElementById('authModal').classList.add('hidden');
            }

            function toggleAuthMode() {
                currentMode = currentMode === 'signin' ? 'signup' : 'signin';
                document.getElementById('formErrorBox').classList.add('hidden');
                updateModalUI();
            }

            function updateModalUI() {
                const title = document.getElementById('modalTitle');
                const subtitle = document.getElementById('modalSubtitle');
                const submitBtn = document.getElementById('submitBtn');
                const switchText = document.getElementById('switchText');
                const switchBtn = document.getElementById('switchBtn');
                const fullNameGroup = document.getElementById('fullNameGroup');
                const confirmPasswordGroup = document.getElementById('confirmPasswordGroup');

                if (currentMode === 'signup') {
                    title.innerText = 'Create Account';
                    subtitle.innerText = 'Join Amalaj Plus Ethiopian Marketplace';
                    submitBtn.innerText = 'Create Account';
                    switchText.innerText = 'Already have an account?';
                    switchBtn.innerText = 'Sign In';
                    fullNameGroup.classList.remove('hidden');
                    confirmPasswordGroup.classList.remove('hidden');
                } else {
                    title.innerText = 'Welcome back';
                    subtitle.innerText = 'Sign in to your Amalaj Plus account';
                    submitBtn.innerText = 'Sign In';
                    switchText.innerText = "Don't have an account?";
                    switchBtn.innerText = 'Sign Up';
                    fullNameGroup.classList.add('hidden');
                    confirmPasswordGroup.classList.add('hidden');
                }
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

            function showError(msg) {
                const errBox = document.getElementById('formErrorBox');
                errBox.innerText = msg;
                errBox.classList.remove('hidden');
            }

            function handleGoogleAuth() {
                window.location.href = "/auth/google";
            }

            function handleFormSubmit(e) {
                e.preventDefault();
                const email = document.getElementById('emailInput').value.trim();
                const pass = document.getElementById('passwordInput').value;
                const errorBox = document.getElementById('formErrorBox');
                errorBox.classList.add('hidden');

                // Strict Validation Checks
                if (!email || !email.includes('@') || !email.includes('.')) {
                    showError("እባክዎ ትክክለኛ የኢሜይል አድራሻ ያስገቡ (Please enter a valid email address)");
                    return;
                }

                if (pass.length < 6) {
                    showError("የሚስጥር ቃል (Password) ቢያንስ 6 ፊደላት/ቁጥሮች መሆን አለበት");
                    return;
                }

                if (currentMode === 'signup') {
                    const fullName = document.getElementById('fullNameInput').value.trim();
                    const confirmPass = document.getElementById('confirmPasswordInput').value;

                    if (!fullName) {
                        showError("እባክዎ ሙሉ ስምዎን ያስገቡ (Full name is required)");
                        return;
                    }

                    if (pass !== confirmPass) {
                        showError("የሚስጥር ቃል ማረጋገጫው አልተመሳሰለም (Passwords do not match)");
                        return;
                    }

                    // Success for Signup
                    alert("አካውንትዎ በተሳካ ሁኔታ ተፈጥሯል! (Account created successfully)");
                    closeAuthModal();
                    updateNavbarUser(fullName);
                } else {
                    // Success for Signin
                    alert("እንኳን ደህና መጡ! በሰአቱ ገብተዋል (Logged in successfully)");
                    closeAuthModal();
                    updateNavbarUser("Hailewelde Kidan");
                }
            }

            function updateNavbarUser(name) {
                const navActions = document.getElementById('navUserActions');
                navActions.innerHTML = `
                    <div class="flex items-center space-x-3 bg-slate-800/80 border border-slate-700 px-3 py-1.5 rounded-xl">
                        <div class="w-8 h-8 rounded-full bg-amber-500 text-slate-950 font-bold flex items-center justify-center text-xs">
                            ${name.charAt(0).toUpperCase()}
                        </div>
                        <span class="text-xs font-semibold text-white">${name}</span>
                    </div>
                `;
            }
        </script>
    </body>
    </html>
    """