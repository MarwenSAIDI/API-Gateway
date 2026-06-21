import os

class Config:
    def __init__(self):
        
        self.DATABASE_URI = os.getenv("DATABASE_URI", None)
        self.USER_SERVICE_URL = os.getenv("USER_SERVICE_URL")

config = Config()