from flask import Blueprint, request, jsonify
from app.services.order_details_service import OrderDetailsService

order_details_bp = Blueprint('order_details', __name__)

@order_details_bp.route('/<int:order_id>', methods=['GET'])
def get_order_details(order_id):
    details = OrderDetailsService.get_by_order(order_id)
    return jsonify([d.serialize() for d in details])
