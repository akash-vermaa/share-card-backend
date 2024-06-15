import os

class Config:
    PORT = os.getenv("PORT")
    SECRET_KEY = os.getenv("SECRET_KEY")

class DevConfig(Config):
    DEBUG = True

class ProdConfig(Config):
    DEBUG = False

# config = {
#     "dev": DevConfig,
#     "prod": ProdConfig,
#     "default": Config
# }

# def getConfig ():
#     return config.get(os.getenv('FLASK_ENV', 'default'))