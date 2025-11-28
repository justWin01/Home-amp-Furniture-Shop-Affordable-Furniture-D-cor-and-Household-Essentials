from flask import Blueprint, request, jsonify
from app.services.user_service import UserService
from app.services.auth_service import AuthService

user_bp = Blueprint('user', __name__)

# Get all users (Admin only)
@user_bp.route('/', methods=['GET'])
def get_users():
    users = UserService.get_all()
    return jsonify([{
        "user_id": u.user_id,
        "full_name": u.full_name,
        "email": u.email,
        "contact_number": u.contact_number,
        "address": u.address,
        "role": u.role
    } for u in users])

# Get user by ID
@user_bp.route('/<int:id>', methods=['GET'])
def get_user(id):
    user = UserService.get_by_id(id)
    if not user:
        return jsonify({'message': 'User not found'}), 404
    return jsonify({
        "user_id": user.user_id,
        "full_name": user.full_name,
        "email": user.email,
        "contact_number": user.contact_number,
        "address": user.address,
        "role": user.role
    })

# Register
@user_bp.route('/register', methods=['POST'])
def register():
    data = request.json
    user = AuthService.register(
        full_name=data.get('full_name'),
        email=data.get('email'),
        password=data.get('password'),
        contact_number=data.get('contact_number'),
        address=data.get('address')
    )
    return jsonify({"message": "User registered", "user_id": user.user_id})

# Login
@user_bp.route('/login', methods=['POST'])
def login():
    data = request.json
    user, token = AuthService.login(data.get('email'), data.get('password'))
    if not user:
        return jsonify({"message": "Invalid credentials"}), 401
    return jsonify({"message": "Login successful", "token": token})
