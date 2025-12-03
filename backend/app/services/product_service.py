from extensions import db
from app.models.product import Product

class ProductService:

    # ======================
    # GET ALL PRODUCTS
    # ======================
    @staticmethod
    def get_all_products():
        return Product.query.all()

    # ======================
    # GET PRODUCT BY ID
    # ======================
    @staticmethod
    def get_product_by_id(product_id):
        return Product.query.get_or_404(product_id)

    # ======================
    # CREATE PRODUCT
    # ======================
    @staticmethod
    def create_product(data, image_filename=None):
        # Safely convert fields to proper types
        try:
            price = float(data.get("price", 0)) if data.get("price") is not None else 0.0
        except ValueError:
            price = 0.0

        try:
            stock_quantity = int(data.get("stock_quantity", 0)) if data.get("stock_quantity") is not None else 0
        except ValueError:
            stock_quantity = 0

        try:
            category_id = int(data.get("category_id")) if data.get("category_id") is not None else None
        except ValueError:
            category_id = None

        product = Product(
            product_name=data.get("product_name"),
            price=price,
            stock_quantity=stock_quantity,
            description=data.get("description"),
            category_id=category_id,
            image=image_filename
        )
        db.session.add(product)
        db.session.commit()
        return product

    # ======================
    # UPDATE PRODUCT
    # ======================
    @staticmethod
    def update_product(product_id, data, image_filename=None):
        product = Product.query.get_or_404(product_id)

        if data.get("product_name"):
            product.product_name = data["product_name"]

        if data.get("price") is not None:
            try:
                product.price = float(data["price"])
            except ValueError:
                pass  # keep old price if conversion fails

        if data.get("stock_quantity") is not None:
            try:
                product.stock_quantity = int(data["stock_quantity"])
            except ValueError:
                pass  # keep old stock_quantity if conversion fails

        if data.get("description"):
            product.description = data["description"]

        if data.get("category_id") is not None:
            try:
                product.category_id = int(data["category_id"])
            except ValueError:
                pass

        if image_filename:
            product.image = image_filename

        db.session.commit()
        return product

    # ======================
    # DELETE PRODUCT
    # ======================
    @staticmethod
    def delete_product(product_id):
        product = Product.query.get_or_404(product_id)
        db.session.delete(product)
        db.session.commit()
        return True
