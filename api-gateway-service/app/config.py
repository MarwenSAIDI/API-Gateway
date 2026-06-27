import os

class Config:
    def __init__(self):
        
        self.USER_SERVICE_URL = os.getenv('USER_SERVICE_URL')
        self.BLOG_SERVICE_URL = os.getenv('BLOG_SERVICE_URL')
        self.HOST_URL = os.getenv('GATEWAY_URL')+'/api'

config = Config()