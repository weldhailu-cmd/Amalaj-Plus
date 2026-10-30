def get_login_page():
    return """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Login - Amalaj Plus</title>
        <script src="https://cdn.tailwindcss.com"></script>
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    </head>
    <body class="bg-[#0b132b] text-slate-100 min-h-screen font-sans flex items-center justify-center selection:bg-amber-500 selection:text-slate-950">

        <div class="max-w-md w-full mx-4 bg-[#16203a] border border-slate-700/60 rounded-3xl p-8 shadow-2xl space-y-8">
            <!-- Brand Logo & Header -->
            <div class="text-center space-y-3">
                <div class="w-14 h-14 rounded-full border-2 border-amber-500 mx-auto overflow-hidden shadow-lg shadow-amber-500/20 bg-white flex items-center justify-center p-1">
                    <img src="/static/logo.png" alt="Amalaj Plus Logo" class="w-full h-full object-cover rounded-full">
                </div>
                <h1 class="text-2xl font-black text-white tracking-tight">Welcome to Amalaj<span class="text-amber-400">Plus</span></h1>
                <p class="text-xs text-slate-400">Secure Digital Asset & Repair Tool Rental Escrow</p>
            </div>

            <!-- Login Options -->
            <div class="space-y-4 pt-4">
                <a href="/auth/google" class="w-full flex items-center justify-center gap-3 px-6 py-3.5 bg-white text-slate-900 font-bold rounded-xl hover:bg-slate-100 transition shadow-lg text-sm">
                    <i class="fa-brands fa-google text-red-500 text-lg"></i>
                    <span>Continue with Google</span>
                </a>
            </div>

            <!-- Terms & Info -->
            <div class="text-center pt-4 border-t border-slate-800 text-xs text-slate-500">
                By continuing, you agree to Amalaj Plus <a href="#" class="text-amber-400 hover:underline">Terms of Service</a> and <a href="#" class="text-amber-400 hover:underline">Privacy Policy</a>.
            </div>
        </div>

    </body>
    </html>
    """