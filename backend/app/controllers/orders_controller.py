from flask import Blueprint, request, jsonify
from app.services.orders_service import OrdersService

orders_bp = Blueprint("orders_bp", __name__)

@orders_bp.route("/", methods=["GET"])
def get_orders():
    orders = OrdersService.get_all_orders()
    return jsonify([{
        "order_id": o.order_id,
        "user_id": o.user_id,
        "status": o.status
    } for o in orders])

@orders_bp.route("/<int:order_id>", methods=["GET"])
def get_order(order_id):
    o = OrdersService.get_order_by_id(order_id)
    return jsonify({
        "order_id": o.order_id,
        "user_id": o.user_id,
        "status": o.status
    })

@orders_bp.route("/", methods=["POST"])
def create_order():
    data = request.get_json()
    OrdersService.create_order(data)
    return jsonify({"message": "Order created"}), 201

@orders_bp.route("/<int:order_id>", methods=["PUT"])
def update_order(order_id):
    data = request.get_json()
    OrdersService.update_order(order_id, data)
    return jsonify({"message": "Order updated"})

@orders_bp.route("/<int:order_id>", methods=["DELETE"])
def delete_order(order_id):
    OrdersService.delete_order(order_id)
    return jsonify({"message": "Order deleted"})
