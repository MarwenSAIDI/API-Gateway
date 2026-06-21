import os

class Config:
    def __init__(self):
        
        self.PORT = os.getenv("PORT", 8080)
        self.DATABASE_URI = os.getenv("DATABASE_URI", None)

config = Config()