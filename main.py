from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles

app = FastAPI()

# staticfiles ን ማገናኘት (የ jsx ፋይሎች የሚገኙበትን ፎልደር ለማሳየት)
# ፋይሎቹ ያሉት በሩት directory ውስጥ ከሆነ ወይም static የሚባል ፎልደር ካለ
app.mount("/static", StaticFiles(directory="."), name="static")

@app.get("/", response_class=HTMLResponse)
def read_root():
    return """
    <!DOCTYPE html>
    <html lang="am">
      <head>
        <meta charset="UTF-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1.0" />
        <title>አማላጅ ፕላስ - Amalaj Plus</title>
        <script src="https://cdn.tailwindcss.com"></script>
        <script src="https://unpkg.com/react@18/umd/react.production.min.js"></script>
        <script src="https://unpkg.com/react-dom@18/umd/react-dom.production.min.js"></script>
        <script src="https://unpkg.com/@babel/standalone/babel.min.js"></script>
      </head>
      <body class="bg-slate-950 text-slate-100">
        <div id="root"></div>
        <!-- እዚህ ጋር ስሙን ከፋይሉ ጋር ማመሳሰል -->
        <script type="text/babel" src="/static/AmalajPlus.jsx"></script>
      </body>
    </html>
    """