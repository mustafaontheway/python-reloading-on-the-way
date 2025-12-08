from fastapi import FastAPI

app = FastAPI()

@app.get("/first-endpoint")
async def first_func():
    return {"First Message": "Hello AI World!"}

# fastapi dev
