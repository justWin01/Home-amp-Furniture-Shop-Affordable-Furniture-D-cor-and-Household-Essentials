from extensions import db
from .user import User
from .category import Category
from .product import Product
from .orders import Orders
from .order_details import OrderDetails


# optional helper to create tables
def create_all(app):
    with app.app_context():
        db.create_all()
