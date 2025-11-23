from app.repositories.product_repository import ProductRepository
from app.models.product import Product

class ProductService:

    @staticmethod
    def get_all():
        return ProductRepository.get_all()

    @staticmethod
    def create(data):
        product = Product(**data)
        return ProductRepository.create(product)
