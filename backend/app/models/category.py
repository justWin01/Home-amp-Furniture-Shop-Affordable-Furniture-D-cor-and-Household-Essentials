from flask_sqlalchemy import SQLAlchemy
from .product import Product  # Optional: only if needed
from extensions import db

db = SQLAlchemy()

class Category(db.Model):
    __tablename__ = 'category'
    category_id = db.Column(db.Integer, primary_key=True)
    category_name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=True)

    products = db.relationship('Product', backref='category', lazy=True)
