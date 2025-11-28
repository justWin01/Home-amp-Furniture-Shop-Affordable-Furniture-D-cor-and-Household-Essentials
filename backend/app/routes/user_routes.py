from flask import Blueprint, request, jsonify
from models import db, User
from app.services.auth_service import AuthService
from app.services.user_service import UserService

user_bp = Blueprint("user_bp", __name__)

# --- CRUD routes ---
@user_bp.route("/", methods=["GET"])
def get_users():
    users = User.query.all()
    return jsonify([{"user_id": u.user_id, "username": u.username, "email": u.email} for u in users])

@user_bp.route("/<int:id>", methods=["GET"])
def get_user(id):
    u = User.query.get_or_404(id)
    return jsonify({"user_id": u.user_id, "username": u.username, "email": u.email})

@user_bp.route("/", methods=["POST"])
def create_user():
    data = request.get_json()
    user = User(username=data["username"], email=data["email"], password=data["password"])
    db.session.add(user)
    db.session.commit()
    return jsonify({"message": "User created", "user_id": user.user_id})

@user_bp.route("/<int:id>", methods=["PUT"])
def update_user(id):
    data = request.get_json()
    u = User.query.get_or_404(id)
    u.username = data.get("username", u.username)
    u.email = data.get("email", u.email)
    db.session.commit()
    return jsonify({"message": "User updated"})

@user_bp.route("/<int:id>", methods=["DELETE"])
def delete_user(id):
    u = User.query.get_or_404(id)
    db.session.delete(u)
    db.session.commit()
    return jsonify({"message": "User deleted"})

# --- Auth routes ---
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
