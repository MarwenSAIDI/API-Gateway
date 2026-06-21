import os

class Config:
    def __init__(self):
        
        self.DATABASE_URI = os.getenv("DATABASE_URI", None)
        self.CONFIG_URI = os.getenv("CONFIG_URI", os.path.join(
            os.getcwd(),
            "gateway.config.yml"
        ))

config = Config()