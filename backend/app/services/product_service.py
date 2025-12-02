from extensions import db
from app.models.product import Product

class ProductService:

    # GET ALL PRODUCTS
    @staticmethod
    def get_all_products():
        return Product.query.all()

    # GET PRODUCTS BY ID
    @staticmethod
    def get_product_by_id(product_id):
        return Product.query.get_or_404(product_id)

    # ADD PRODUCTS
    @staticmethod
    def create_product(data):
        product = Product(
            product_name=data["product_name"],
            price=data["price"],
            stock=data.get("stock", 0),
            description=data.get("description"),
            category_id=data.get("category_id")
        )
        db.session.add(product)
        db.session.commit()
        return product

    # UPDATE PRODUCTS
    @staticmethod
    def update_product(product_id, data):
        product = Product.query.get_or_404(product_id)
        product.product_name = data.get("product_name", product.product_name)
        product.price = data.get("price", product.price)
        product.stock = data.get("stock", product.stock)
        product.description = data.get("description", product.description)
        product.category_id = data.get("category_id", product.category_id)
        db.session.commit()
        return product

    # DELETE PRODUCTS
    @staticmethod
    def delete_product(product_id):
        product = Product.query.get_or_404(product_id)
        db.session.delete(product)
        db.session.commit()
        return True
