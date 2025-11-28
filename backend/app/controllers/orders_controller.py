from flask import Blueprint, request, jsonify
from app.services.orders_service import OrdersService

orders_bp = Blueprint('orders', __name__)

@orders_bp.route('/', methods=['POST'])
def create_order():
    data = request.json
    order = OrdersService.create(data)
    return jsonify(order.serialize()), 201
