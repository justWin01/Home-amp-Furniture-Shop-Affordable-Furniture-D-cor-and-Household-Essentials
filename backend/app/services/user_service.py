from app.repositories.user_repository import UserRepository

class UserService:

    @staticmethod
    def get_all():
        return UserRepository.get_all()
