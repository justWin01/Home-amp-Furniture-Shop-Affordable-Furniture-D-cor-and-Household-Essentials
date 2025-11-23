from flask import Blueprint, request, jsonify
from app.services.category_service import CategoryService

category_bp = Blueprint("category", __name__)

@category_bp.route("/categories", methods=["GET"])
def get_categories():
    categories = CategoryService.get_all()
    return jsonify([c.category_name for c in categories])

@category_bp.route("/categories", methods=["POST"])
def create_category():
    data = request.json
    category = CategoryService.create(data["name"], data["description"])
    return jsonify({"message": "Category created", "id": category.category_id})
