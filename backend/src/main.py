from starlette.middleware.cors import CORSMiddleware
from .services.service import APIService
from .data.service import DatabaseService

import uvicorn

api = APIService(DatabaseService("postgresql+asyncpg://postgres:password@localhost:5432/your_dormitory"))

api.app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@api.app.get("/")
async def root():
    return {"message": "Hello Bigger Applications!"}


if __name__ == "__main__":
    # init_db()
    uvicorn.run("main:api.app", port=3000, reload=True, workers=1)
