from fastapi import FastAPI
from app.routes import user_gateway, blog_gateway

def create_app():
    app_ = FastAPI(title="API Gateway")
    app_.include_router(user_gateway.router, prefix='/api')
    app_.include_router(blog_gateway.router, prefix='/api')
    return app_

app = create_app()