from flask import Blueprint, request, jsonify
from app.services.orders_service import OrdersService

orders_bp = Blueprint("orders", __name__)

@orders_bp.route("/orders", methods=["GET"])
def get_orders():
    orders = OrdersService.get_all()
    return jsonify([o.order_id for o in orders])

@orders_bp.route("/orders", methods=["POST"])
def create_order():
    data = request.json
    order = OrdersService.create(data)
    return jsonify({"message": "Order created", "id": order.order_id})
