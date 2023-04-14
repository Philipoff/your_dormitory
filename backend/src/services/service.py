from fastapi import APIRouter, FastAPI
from fastapi.middleware.cors import CORSMiddleware

from ..services.dormitories.routes import dormitories_router
from ..services.auth.routes import auth_router
from ..data.service import DatabaseService


class APIService:
    def __init__(self, database: DatabaseService):
        self.debug = True
        self.app = FastAPI(
            title="API",
        )
        self.database = database

        #  TODO: remove *
        origins = ["*"]
        self.app.add_middleware(
            CORSMiddleware,
            allow_origins=origins,
            allow_credentials=True,
            allow_methods=[""],
            allow_headers=[""],
        )
        self.app.state.database = database

        self.attach_routes()

    def attach_routes(self):
        api_router = APIRouter()
        api_router.prefix = "/api"

        api_router.include_router(router=dormitories_router, prefix="/index", tags=["Index"])
        api_router.include_router(router=auth_router, prefix="/auth", tags=["Auth"])
        self.app.include_router(router=api_router)
