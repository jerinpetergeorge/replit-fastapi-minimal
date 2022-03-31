from fastapi import FastAPI

from app.apis.users import router

app = FastAPI()
app.include_router(router)


@app.get("/")
async def read_root():
    return {"Hello": "World"}
