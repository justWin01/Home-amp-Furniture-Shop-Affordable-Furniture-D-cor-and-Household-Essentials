from flask import Blueprint, request, jsonify
from models import db, Category

category_bp = Blueprint('category_bp', __name__)

@category_bp.route('/categories', methods=['POST'])
def create_category():
    data = request.get_json()
    category = Category(category_name=data['category_name'], description=data.get('description'))
    db.session.add(category)
    db.session.commit()
    return jsonify({'message': 'Category created', 'category_id': category.category_id})

@category_bp.route('/categories', methods=['GET'])
def get_categories():
    categories = Category.query.all()
    return jsonify([{'category_id': c.category_id, 'category_name': c.category_name, 'description': c.description} for c in categories])

@category_bp.route('/categories/<int:id>', methods=['GET'])
def get_category(id):
    c = Category.query.get_or_404(id)
    return jsonify({'category_id': c.category_id, 'category_name': c.category_name, 'description': c.description})

@category_bp.route('/categories/<int:id>', methods=['PUT'])
def update_category(id):
    data = request.get_json()
    c = Category.query.get_or_404(id)
    c.category_name = data.get('category_name', c.category_name)
    c.description = data.get('description', c.description)
    db.session.commit()
    return jsonify({'message': 'Category updated'})

@category_bp.route('/categories/<int:id>', methods=['DELETE'])
def delete_category(id):
    c = Category.query.get_or_404(id)
    db.session.delete(c)
    db.session.commit()
    return jsonify({'message': 'Category deleted'})
