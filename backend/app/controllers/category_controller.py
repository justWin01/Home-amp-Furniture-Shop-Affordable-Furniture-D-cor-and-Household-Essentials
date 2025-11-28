from flask import Blueprint, request, jsonify
from app.services.category_service import CategoryService

category_bp = Blueprint('category', __name__)

@category_bp.route('/', methods=['GET'])
def get_categories():
    categories = CategoryService.get_all()
    return jsonify([c.serialize() for c in categories])

@category_bp.route('/', methods=['POST'])
def create_category():
    data = request.json
    category = CategoryService.create(data)
    return jsonify(category.serialize()), 201
