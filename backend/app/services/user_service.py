from werkzeug.security import generate_password_hash, check_password_hash
from extensions import db
from app.models.user import User

class UserService:

    # ======================
    # GET ALL USERS
    # ======================
    @staticmethod
    def get_all_users():
        return User.query.all()

    # ======================
    # GET USER BY ID
    # ======================
    @staticmethod
    def get_user_by_id(user_id):
        return User.query.get_or_404(user_id)

    # ======================
    # GET USER BY EMAIL
    # ======================
    @staticmethod
    def get_user_by_email(email):
        return User.query.filter_by(email=email).first()

    # ======================
    # CREATE USER (SIGN UP)
    # ======================
    @staticmethod
    def create_user(data):
        # Check if email already exists
        if User.query.filter_by(email=data["email"]).first():
            raise ValueError("Email already registered")

        hashed_password = generate_password_hash(data["password"])

        new_user = User(
            full_name=data["full_name"],
            email=data["email"],
            password=hashed_password,
            contact_number=data.get("contact_number"),
            address=data.get("address"),
            role=data.get("role", "Customer")
        )

        db.session.add(new_user)
        db.session.commit()

        return new_user

    # ======================
    # LOGIN USER
    # ======================
    @staticmethod
    def login_user(data):
        email = data.get("email")
        password = data.get("password")

        user = User.query.filter_by(email=email).first()

        if not user:
            return {"error": "Invalid email or password"}, 401

        if not check_password_hash(user.password, password):
            return {"error": "Invalid email or password"}, 401

        return {
            "message": "Login successful",
            "user": user.to_dict()
        }, 200

    # ======================
    # UPDATE USER
    # ======================
    @staticmethod
    def update_user(user_id, data):
        user = User.query.get_or_404(user_id)

        user.full_name = data.get("full_name", user.full_name)
        user.email = data.get("email", user.email)
        user.contact_number = data.get("contact_number", user.contact_number)
        user.address = data.get("address", user.address)

        # Update password if provided
        if "password" in data and data["password"]:
            user.password = generate_password_hash(data["password"])

        db.session.commit()
        return user

    # ======================
    # DELETE USER
    # ======================
    @staticmethod
    def delete_user(user_id):
        user = User.query.get_or_404(user_id)
        db.session.delete(user)
        db.session.commit()
