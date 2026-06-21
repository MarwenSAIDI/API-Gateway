import os

class Config:
    def __init__(self):
        
        self.DATABASE_URI = os.getenv("DATABASE_URI", None)

config = Config()