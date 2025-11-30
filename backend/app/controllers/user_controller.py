from flask import Blueprint, request, jsonify
from app.services.user_service import UserService

user_bp = Blueprint("user_bp", __name__)

@user_bp.route("/", methods=["GET"])
def get_users():
    users = UserService.get_all_users()
    return jsonify([{
        "user_id": u.user_id,
        "full_name": u.full_name,
        "email": u.email,
        "role": u.role
    } for u in users])

@user_bp.route("/<int:user_id>", methods=["GET"])
def get_user(user_id):
    u = UserService.get_user_by_id(user_id)
    return jsonify({
        "user_id": u.user_id,
        "full_name": u.full_name,
        "email": u.email,
        "role": u.role
    })

@user_bp.route("/register", methods=["POST"])
def create_user():
    data = request.get_json()

    try:
        new_user = UserService.create_user(data)
        return jsonify({"message": "User created successfully"}), 201

    except ValueError as e:
        return jsonify({"error": str(e)}), 400

    except Exception as e:
        return jsonify({"error": "Server error", "details": str(e)}), 500


@user_bp.route("/login", methods=["POST"])
def login_user():
    data = request.get_json()
    result, status = UserService.login_user(data)
    return jsonify(result), status


@user_bp.route("/<int:user_id>", methods=["PUT"])
def update_user(user_id):
    data = request.get_json()
    UserService.update_user(user_id, data)
    return jsonify({"message": "User updated successfully"})

@user_bp.route("/<int:user_id>", methods=["DELETE"])
def delete_user(user_id):
    UserService.delete_user(user_id)
    return jsonify({"message": "User deleted successfully"})
