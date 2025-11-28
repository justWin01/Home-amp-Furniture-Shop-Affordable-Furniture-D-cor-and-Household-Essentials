from extensions import bcrypt
from app.repositories.user_repository import UserRepository
from app.models.user import User
from flask_jwt_extended import create_access_token

class AuthService:
    @staticmethod
    def register(full_name, email, plain_password, contact_number=None, address=None):
        # Check if the user already exists
        existing = UserRepository.get_by_email(email)
        if existing:
            raise ValueError('Email already registered')
        
        # Hash the password
        hashed_password = bcrypt.generate_password_hash(plain_password).decode('utf-8')
        
        # Create a new user instance
        new_user = User(
            full_name=full_name,
            email=email,
            password=hashed_password,
            contact_number=contact_number,
            address=address,
            role='Customer'  # default role
        )
        
        # Save the user to the database
        UserRepository.add(new_user)
        return new_user

    @staticmethod
    def login(email, plain_password):
        user = UserRepository.get_by_email(email)
        if not user:
            raise ValueError('Invalid email or password')
        
        if not bcrypt.check_password_hash(user.password, plain_password):
            raise ValueError('Invalid email or password')
        
        # Create a JWT access token
        access_token = create_access_token(identity=user.user_id)
        return access_token
