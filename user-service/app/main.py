from fastapi import FastAPI
from app.routes.user import router

def create_app():
    app_ = FastAPI(title="User Service")
    app_.include_router(router, prefix='/api')

    return app_

app = create_app()