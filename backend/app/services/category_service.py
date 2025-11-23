from app.repositories.category_repository import CategoryRepository
from app.models.category import Category

class CategoryService:

    @staticmethod
    def get_all():
        return CategoryRepository.get_all()

    @staticmethod
    def create(name, description):
        category = Category(category_name=name, description=description)
        return CategoryRepository.create(category)
