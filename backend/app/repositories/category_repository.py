from extensions import db
from app.models.category import Category

class CategoryRepository:

    @staticmethod
    def get_all():
        return Category.query.all()

    @staticmethod
    def create(category):
        db.session.add(category)
        db.session.commit()
        return category
