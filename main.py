from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
def read_root():
    return """
    <!DOCTYPE html>
    <html lang="am">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>አማላጅ ፕላስ - Amalaj Plus</title>
        <script src="https://cdn.tailwindcss.com"></script>
    </head>
    <body class="bg-[#0b132b] text-slate-100 min-h-screen font-sans">
        <!-- Navbar -->
        <header class="border-b border-amber-500/20 bg-[#1c2541]/80 backdrop-blur sticky top-0 z-50">
            <div class="max-w-7xl mx-auto px-4 py-4 flex justify-between items-center">
                <div class="flex items-center space-x-3">
                    <span class="text-2xl font-bold text-amber-400 tracking-wider">አማላጅ ፕላስ</span>
                    <span class="text-xs px-2 py-1 bg-amber-500/10 text-amber-300 border border-amber-500/30 rounded-full">ደህንነቱ የተጠበቀ የዲጂታል ንብረት ገበያ</span>
                </div>
                <div class="space-x-4">
                    <a href="/docs" target="_blank" class="text-sm px-4 py-2 bg-amber-500 text-slate-950 font-semibold rounded-lg hover:bg-amber-400 transition">API Docs</a>
                </div>
            </div>
        </header>

        <!-- Hero Section -->
        <main class="max-w-7xl mx-auto px-4 py-16 text-center">
            <div class="max-w-3xl mx-auto space-y-6">
                <h1 class="text-4xl md:text-6xl font-extrabold tracking-tight text-white">
                    ዲጂታል ንብረቶችዎን <span class="text-amber-400">በእስተማማኝ</span> ይሽጡና ይግዙ
                </h1>
                <p class="text-lg text-slate-300">
                    የቴሌግራም ቻናሎች፣ የቲክቶክ አካውንቶች፣ ዩቲዩብ ቻናሎች እና ዌብሳይቶች በአስተማማኝ የእስክሮው (Escrow) ስርዓት ይለዋወጡ።
                </p>
                <div class="flex justify-center gap-4 pt-4">
                    <a href="/docs" class="px-8 py-3 bg-amber-500 text-slate-950 font-bold rounded-xl shadow-lg hover:bg-amber-400 transition">
                        አሁን ይጀምሩ
                    </a>
                </div>
            </div>

            <!-- Features Grid -->
            <div class="grid md:grid-cols-3 gap-8 mt-20 text-left">
                <div class="p-6 rounded-2xl bg-[#1c2541] border border-amber-500/20 shadow-xl">
                    <div class="text-amber-400 text-2xl mb-3">🔒</div>
                    <h3 class="text-xl font-bold mb-2 text-white">አስተማማኝ እስክሮው</h3>
                    <p class="text-slate-400 text-sm">ገንዘቡ ደህንነቱ በተጠበቀ ሁኔታ ተይዞ ንብረቱ እስኪረከብ ድረስ ሙሉ ዋስትና ይሰጣል።</p>
                </div>
                <div class="p-6 rounded-2xl bg-[#1c2541] border border-amber-500/20 shadow-xl">
                    <div class="text-amber-400 text-2xl mb-3">⚡</div>
                    <h3 class="text-xl font-bold mb-2 text-white">ፈጣን ዝውውር</h3>
                    <p class="text-slate-400 text-sm">ያለ ምንም ወከባ እና መዘግየት ንብረቶችን በፍጥነት የማዛወር ሂደት።</p>
                </div>
                <div class="p-6 rounded-2xl bg-[#1c2541] border border-amber-500/20 shadow-xl">
                    <div class="text-amber-400 text-2xl mb-3">🛡️</div>
                    <h3 class="text-xl font-bold mb-2 text-white">የታመነ ድጋፍ</h3>
                    <p class="text-slate-400 text-sm">በማንኛውም ሰዓት ከጎንዎ ሆኖ ግብይቱን የሚያስተባብር ባለሙያ ድጋፍ።</p>
                </div>
            </div>
        </main>

        <!-- Footer -->
        <footer class="border-t border-amber-500/20 mt-20 py-8 text-center text-slate-500 text-sm">
            <p>&copy; 2026 አማላጅ ፕላስ (Amalaj Plus). መብቱ በህግ የተጠበቀ ነው።</p>
        </footer>
    </body>
    </html>
    """