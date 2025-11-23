from extensions import bcrypt
from app.repositories.user_repository import UserRepository
from app.models.user import User

class AuthService:

    @staticmethod
    def register(fullname, email, password):
        hashed = bcrypt.generate_password_hash(password).decode("utf-8")
        user = User(fullname=fullname, email=email, password=hashed)
        return UserRepository.create(user)

    @staticmethod
    def login(email, password):
        user = UserRepository.find_by_email(email)
        if user and bcrypt.check_password_hash(user.password, password):
            return user
        return None
