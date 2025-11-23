from app.repositories.order_details_repository import OrderDetailsRepository
from app.models.order_details import OrderDetails

class OrderDetailsService:

    @staticmethod
    def create(data):
        detail = OrderDetails(**data)
        return OrderDetailsRepository.create(detail)
