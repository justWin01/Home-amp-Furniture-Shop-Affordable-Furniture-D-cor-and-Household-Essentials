from flask import Blueprint, jsonify
from models.product import Product

product_bp = Blueprint('product_bp', __name__)

@product_bp.route('/products', methods=['GET'])
def get_products():
    products = Product.query.all()
    return jsonify([
        {
            "id": p.product_id,
            "name": p.product_name,
            "price": p.price,
            "stock": p.stock_quantity
        } for p in products
    ])
