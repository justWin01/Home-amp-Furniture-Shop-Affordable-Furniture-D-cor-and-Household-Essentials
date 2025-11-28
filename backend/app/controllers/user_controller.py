from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from extensions import db, bcrypt
from ..models.user import User
from app.services.user_service import UserService

auth_bp = Blueprint("auth_bp", __name__)
user_bp = Blueprint("user_bp", __name__)

# GET ALL USERS
@user_bp.get("/")
def get_users():
    users = UserService.get_all_users()
    return jsonify([u.to_dict() for u in users]), 200

# GET USER BY ID
@user_bp.get("/<int:user_id>")
def get_user(user_id):
    user = UserService.get_user_by_id(user_id)
    return jsonify(user.to_dict()), 200
# --------------------------
# REGISTER
# --------------------------
@auth_bp.post("/register")
def register():
    data = request.get_json()
    full_name = data.get("full_name")
    email = data.get("email")
    password = data.get("password")
    contact_number = data.get("contact_number")
    address = data.get("address")
    role = data.get("role", "Customer")

    if not all([full_name, email, password]):
        return jsonify({"error": "Missing required fields"}), 400

    if User.query.filter_by(email=email).first():
        return jsonify({"error": "User already exists"}), 400

    # Hash password using Bcrypt
    hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')

    user = User(
        full_name=full_name,
        email=email,
        password=hashed_password,
        contact_number=contact_number,
        address=address,
        role=role
    )
    db.session.add(user)
    db.session.commit()

    return jsonify({"message": "User registered successfully"}), 201

# --------------------------
# LOGIN
# --------------------------
@auth_bp.post("/login")
def login():
    data = request.get_json()
    email = data.get("email")
    password = data.get("password")

    user = User.query.filter_by(email=email).first()
    if not user or not bcrypt.check_password_hash(user.password, password):
        return jsonify({"error": "Invalid credentials"}), 401

    access_token = create_access_token(
        identity=user.user_id,
        additional_claims={"role": user.role}
    )

    return jsonify({"access_token": access_token, "user": user.to_dict()}), 200

# --------------------------
# GET CURRENT USER (/me)
# --------------------------
@auth_bp.get("/me")
@jwt_required()
def get_me():
    user_id = get_jwt_identity()
    user = User.query.get(user_id)
    if not user:
        return jsonify({"error": "User not found"}), 404
    return jsonify(user.to_dict()), 200
