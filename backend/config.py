import os

class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "supersecretkey")
    SQLALCHEMY_DATABASE_URI =  "mysql://root:@localhost/home_furniture_db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False


