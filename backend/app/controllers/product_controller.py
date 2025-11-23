from flask import Blueprint, request, jsonify
from app.services.product_service import ProductService

product_bp = Blueprint("product", __name__)

@product_bp.route("/products", methods=["GET"])
def get_products():
    return jsonify([p.product_name for p in ProductService.get_all()])

@product_bp.route("/products", methods=["POST"])
def create_product():
    data = request.json
    product = ProductService.create(data)
    return jsonify({"message": "Product created", "id": product.product_id})
