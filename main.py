import os
import uvicorn
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi_sso.sso.github import GithubSSO
from dotenv import load_dotenv

load_dotenv()

CLIENT_ID = os.getenv('CLIENT_ID_GH')
CLIENT_SECRET = os.getenv('CLIENT_SECRET_GH')


app = FastAPI()

sso = GithubSSO(
    client_id=CLIENT_ID,
    client_secret=CLIENT_SECRET,
    redirect_uri="http://127.0.0.1:5000/auth/callback",
    allow_insecure_http=True,
)


@app.get("/auth/login")
async def auth_init():
    """Initialize auth and redirect"""
    async with sso:
        return await sso.get_login_redirect()


@app.get("/auth/callback")
async def auth_callback(request: Request):
    """Verify login"""
    async with sso:
        user = await sso.verify_and_process(request)
        return user


@app.get("/", response_class=HTMLResponse)  # Specify HTMLResponse as response_class
async def read_root():
    """Return HTML page with login form"""
    html = """
    <form class="col-lg-2" method="get" action="/auth/login" style="text-align: center;">
        <button class="login-btn" type="submit">
            Login with GitHub
        </button>
    </form>
    """
    return html


if __name__ == "__main__":
    uvicorn.run(app="main:app", host="127.0.0.1", port=5000)