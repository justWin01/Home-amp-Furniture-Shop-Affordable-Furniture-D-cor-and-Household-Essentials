from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Config:
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:@localhost/home_furniture_db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
