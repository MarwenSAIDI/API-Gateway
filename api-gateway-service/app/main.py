from fastapi import FastAPI

def create_app():
    app_ = FastAPI(title="API Gateway")

    return app_

app = create_app()