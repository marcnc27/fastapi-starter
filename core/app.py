from __future__ import annotations

from fastapi_offline import FastAPIOffline
from starlette.middleware.cors import CORSMiddleware

from config import Configuration
from constants import app_title
from core.api import status_router
from utils import Logger

logger = Logger.get_logger(__name__)


def generate_app_instance(configuration: Configuration):
    fastapi_app = FastAPIOffline(title=app_title, version=Configuration.get().VERSION, licence_info={"name": "MIT"})

    if configuration.DEBUG:
        logger.debug("on startup: registering middlewares")
    fastapi_app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_credentials=True, allow_methods=["*"],
                               allow_headers=["*"])
    return fastapi_app


app = generate_app_instance(Configuration.get())


@app.on_event("startup")
def on_startup():
    configuration = Configuration.get()
    if configuration.DEBUG:
        logger.debug("on startup: registering routers")

    app.include_router(status_router)
