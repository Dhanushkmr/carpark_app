from typing import Optional, List
from fastapi import FastAPI, Request

app = FastAPI()


sk_carpark = None

@app.get("/")
async def get_default_carpark():
    return sk_carpark


@app.post("/update")
def default_carpark(location):
    global sk_carpark
    sk_carpark = location
    return sk_carpark
