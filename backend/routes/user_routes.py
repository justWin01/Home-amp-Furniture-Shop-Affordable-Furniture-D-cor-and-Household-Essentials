from flask import Blueprint, request, jsonify
from models import db, User

user_bp = Blueprint('user_bp', __name__)

# CREATE
@user_bp.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    user = User(username=data['username'], email=data['email'], password=data['password'])
    db.session.add(user)
    db.session.commit()
    return jsonify({'message': 'User created', 'user_id': user.user_id})

# READ ALL
@user_bp.route('/users', methods=['GET'])
def get_users():
    users = User.query.all()
    return jsonify([{'user_id': u.user_id, 'username': u.username, 'email': u.email} for u in users])

# READ ONE
@user_bp.route('/users/<int:id>', methods=['GET'])
def get_user(id):
    u = User.query.get_or_404(id)
    return jsonify({'user_id': u.user_id, 'username': u.username, 'email': u.email})

# UPDATE
@user_bp.route('/users/<int:id>', methods=['PUT'])
def update_user(id):
    data = request.get_json()
    u = User.query.get_or_404(id)
    u.username = data.get('username', u.username)
    u.email = data.get('email', u.email)
    db.session.commit()
    return jsonify({'message': 'User updated'})

# DELETE
@user_bp.route('/users/<int:id>', methods=['DELETE'])
def delete_user(id):
    u = User.query.get_or_404(id)
    db.session.delete(u)
    db.session.commit()
    return jsonify({'message': 'User deleted'})
