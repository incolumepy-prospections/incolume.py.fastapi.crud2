"""Server module."""
from fastapi import FastAPI

from incolume.py.fastapi.crud2 import __version__
from incolume.py.fastapi.crud2.routers import user

app = FastAPI(version=__version__)


@app.get("/")
async def root(msg: str = ""):
    """Endpoint for root."""
    msg = msg or "Hello world"
    return {"greeting": msg}


app.include_router(user.router, prefix="/api/v2")
