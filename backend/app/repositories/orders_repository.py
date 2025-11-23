from extensions import db
from app.models.orders import Orders

class OrdersRepository:

    @staticmethod
    def get_all():
        return Orders.query.all()

    @staticmethod
    def create(order):
        db.session.add(order)
        db.session.commit()
        return order
