from fastapi import FastAPI
from app.routes.blog import router

def create_app():
    app_ = FastAPI(title="Blog Service")
    app_.include_router(router)

    return app_

app = create_app()