from flask import Blueprint, request, jsonify
from werkzeug.utils import secure_filename
import os
from app.services.product_service import ProductService

product_bp = Blueprint("product_bp", __name__)

# Folder to save uploaded product images
UPLOAD_FOLDER = "static/uploads/products"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# ----------------------------
# GET ALL PRODUCTS
# ----------------------------
@product_bp.route("/", methods=["GET"])
def get_products():
    products = ProductService.get_all_products()
    return jsonify([p.to_dict() for p in products])

# ----------------------------
# GET PRODUCT BY ID
# ----------------------------
@product_bp.route("/<int:product_id>", methods=["GET"])
def get_product(product_id):
    p = ProductService.get_product_by_id(product_id)
    return jsonify(p.to_dict())

# ----------------------------
# CREATE PRODUCT (JSON or Form + Image)
# ----------------------------
@product_bp.route("/", methods=["POST"])
def create_product():
    # Check if request has JSON or form-data
    if request.is_json:
        data = request.get_json()
        file = None
        filename = None
    else:
        data = request.form.to_dict()
        file = request.files.get("image")
        filename = None
        if file:
            filename = secure_filename(file.filename)
            file.save(os.path.join(UPLOAD_FOLDER, filename))

    # Create product using service
    ProductService.create_product(data, image_filename=filename)
    return jsonify({"message": "Product created"}), 201

# ----------------------------
# UPDATE PRODUCT (JSON or Form + Image)
# ----------------------------
@product_bp.route("/<int:product_id>", methods=["PUT"])
def update_product(product_id):
    if request.is_json:
        data = request.get_json()
        file = None
        filename = None
    else:
        data = request.form.to_dict()
        file = request.files.get("image")
        filename = None
        if file:
            filename = secure_filename(file.filename)
            file.save(os.path.join(UPLOAD_FOLDER, filename))

    ProductService.update_product(product_id, data, image_filename=filename)
    return jsonify({"message": "Product updated"})

# ----------------------------
# DELETE PRODUCT
# ----------------------------
@product_bp.route("/<int:product_id>", methods=["DELETE"])
def delete_product(product_id):
    ProductService.delete_product(product_id)
    return jsonify({"message": "Product deleted"})
