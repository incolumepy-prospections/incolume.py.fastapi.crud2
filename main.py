# main.py
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root(msg: str = ''):
    msg = msg or "Hello world"
    return {"greeting": msg}
