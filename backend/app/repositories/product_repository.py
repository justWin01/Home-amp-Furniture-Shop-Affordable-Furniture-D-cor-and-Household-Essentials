from extensions import db
from app.models.product import Product

class ProductRepository:

    @staticmethod
    def get_all():
        return Product.query.all()

    @staticmethod
    def create(product):
        db.session.add(product)
        db.session.commit()
        return product
