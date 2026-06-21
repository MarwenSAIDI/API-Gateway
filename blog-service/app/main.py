from fastapi import FastAPI

def create_app():
    app_ = FastAPI(title="Blog Service")

    return app_

app = create_app()