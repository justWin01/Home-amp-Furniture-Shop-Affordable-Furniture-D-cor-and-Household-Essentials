from flask import Blueprint, request, jsonify
from app.services.product_service import ProductService

product_bp = Blueprint('product', __name__)

@product_bp.route('/', methods=['GET'])
def get_products():
    products = ProductService.get_all()
    return jsonify([p.serialize() for p in products])
