from fastapi import APIRouter

dormitories_router = APIRouter()


@dormitories_router.get("/")
async def index():
    return {"status": "OK"}
