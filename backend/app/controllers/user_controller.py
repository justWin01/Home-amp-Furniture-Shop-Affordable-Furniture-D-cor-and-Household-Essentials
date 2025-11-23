from flask import Blueprint, request, jsonify
from app.services.auth_service import AuthService
from app.services.user_service import UserService

user_bp = Blueprint("users", __name__)

@user_bp.route("/users", methods=["GET"])
def get_users():
    users = UserService.get_all()
    return jsonify([u.email for u in users])

@user_bp.route("/register", methods=["POST"])
def register():
    data = request.json
    user = AuthService.register(data["fullname"], data["email"], data["password"])
    return jsonify({"message": "User registered", "id": user.user_id})

@user_bp.route("/login", methods=["POST"])
def login():
    data = request.json
    user = AuthService.login(data["email"], data["password"])
    if not user:
        return jsonify({"message": "Invalid credentials"}), 401
    return jsonify({"message": "Login successful", "email": user.email})
