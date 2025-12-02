from flask import Blueprint, request, jsonify
from app.services.product_service import ProductService

product_bp = Blueprint("product_bp", __name__)

# GET ALL PRODUCTS
@product_bp.route("/", methods=["GET"])
def get_products():
    products = ProductService.get_all_products()
    return jsonify([{
        "product_id": p.product_id,
        "product_name": p.product_name,
        "price": p.price,
        "stock": p.stock_quantity,
        "category_id": p.category_id
    } for p in products])

# GET PRODUCT BY ID
@product_bp.route("/<int:product_id>", methods=["GET"])
def get_product(product_id):
    p = ProductService.get_product_by_id(product_id)
    return jsonify({
        "product_id": p.product_id,
        "product_name": p.product_name,
        "price": p.price,
        "stock": p.stock_quantity,
        "category_id": p.category_id
    })

# CREATE PRODUCT
@product_bp.route("/", methods=["POST"])
def create_product():
    data = request.get_json()
    ProductService.create_product(data)
    return jsonify({"message": "Product created"}), 201

# UPDATE PRODUCT
@product_bp.route("/<int:product_id>", methods=["PUT"])
def update_product(product_id):
    data = request.get_json()
    ProductService.update_product(product_id, data)
    return jsonify({"message": "Product updated"})

# DELETE PRODUCT
@product_bp.route("/<int:product_id>", methods=["DELETE"])
def delete_product(product_id):
    ProductService.delete_product(product_id)
    return jsonify({"message": "Product deleted"})
