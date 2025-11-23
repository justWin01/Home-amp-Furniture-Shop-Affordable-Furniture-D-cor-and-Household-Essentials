from app.repositories.orders_repository import OrdersRepository
from app.models.orders import Orders

class OrdersService:

    @staticmethod
    def get_all():
        return OrdersRepository.get_all()

    @staticmethod
    def create(data):
        order = Orders(**data)
        return OrdersRepository.create(order)
