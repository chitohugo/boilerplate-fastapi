from app.api.routes import routers as v1_routers
from fastapi import FastAPI
from config import configs
from container import Container
from starlette.middleware.cors import CORSMiddleware


class AppCreator:
    _instance = None

    def __init__(self):
        # set app default
        self.app = FastAPI(
            title=configs.project_name,
            openapi_url=f"{configs.api}/openapi.json",
            version="0.0.1",
        )

        # set db and container
        self.container = Container()
        self.db = self.container.db()
        # self.db.create_database()

        # set cors
        if configs.backend_cors_origins:
            self.app.add_middleware(
                CORSMiddleware,
                allow_origins=[str(origin) for origin in configs.backend_cors_origins],
                allow_credentials=True,
                allow_methods=["*"],
                allow_headers=["*"],
            )

        # set routes
        @self.app.get("/")
        def status():
            return f"API: {configs.project_name} is working"

        self.app.include_router(v1_routers, prefix=configs.prefix)

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(AppCreator, cls).__new__(cls)
        return cls._instance


app_creator = AppCreator()
app = app_creator.app
db = app_creator.db
container = app_creator.container
