from extensions import db, bcrypt
from app.models.user import User

class UserService:

    @staticmethod
    def get_all_users():
        return User.query.all()

    @staticmethod
    def get_user_by_id(user_id):
        return User.query.get_or_404(user_id)

    @staticmethod
    def create_user(data):
        hashed_password = bcrypt.generate_password_hash(
            data["password"]
        ).decode("utf-8")

        user = User(
            full_name=data["full_name"],
            email=data["email"],
            password=hashed_password,
            contact_number=data.get("contact_number"),
            address=data.get("address"),
            role=data.get("role", "Customer")
        )
        db.session.add(user)
        db.session.commit()
        return user

    @staticmethod
    def update_user(user_id, data):
        user = User.query.get_or_404(user_id)

        user.full_name = data.get("full_name", user.full_name)
        user.email = data.get("email", user.email)

        # hash password only if user wants to change it
        if "password" in data and data["password"]:
            user.password = bcrypt.generate_password_hash(
                data["password"]
            ).decode("utf-8")

        user.contact_number = data.get("contact_number", user.contact_number)
        user.address = data.get("address", user.address)
        user.role = data.get("role", user.role)

        db.session.commit()
        return user

    @staticmethod
    def delete_user(user_id):
        user = User.query.get_or_404(user_id)
        db.session.delete(user)
        db.session.commit()
        return True
