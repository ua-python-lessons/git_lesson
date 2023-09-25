from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()


@app.get("/", response_class=HTMLResponse)
async def root():
    html = f"""
    <!DOCTYPE html>
    <html>
        <head>
            <title>Image Page</title>
        </head>
        <body>
            <h1>Ви великий молодець!</h1>
            <p>Перший крок у вас вдався, рухаємся далі!</p>
            <img src="https://media4.giphy.com/media/4QFd9B1jMRZDVbMYAg/giphy.gif" alt="Example Image">
        </body>
    </html>
    """
    return html
