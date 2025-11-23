from flask import Blueprint, request, jsonify
from app.services.order_details_service import OrderDetailsService

order_details_bp = Blueprint("order_details", __name__)

@order_details_bp.route("/order-details", methods=["POST"])
def create_detail():
    data = request.json
    detail = OrderDetailsService.create(data)
    return jsonify({"message": "Order detail created", "id": detail.detail_id})
