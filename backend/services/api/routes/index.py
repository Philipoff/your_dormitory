from fastapi import APIRouter

index_router = APIRouter()


@index_router.get("/")
async def index():
    return {"status": "OK"}
