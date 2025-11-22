from flask import Flask
from flask_cors import CORS
from config import Config, db
from models import *
from routes.user_routes import user_bp
from routes.category_routes import category_bp
from routes.product_routes import product_bp
from routes.orders_routes import orders_bp
from routes.order_details_routes import order_details_bp

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)

# Enable CORS for all /api routes
CORS(app, resources={r"/api/*": {"origins": "*"}})

# Root route for testing
@app.route('/')
def home():
    return "Flask backend is running!"

# Register all blueprints with /api prefix
app.register_blueprint(user_bp, url_prefix='/api')
app.register_blueprint(category_bp, url_prefix='/api')
app.register_blueprint(product_bp, url_prefix='/api')
app.register_blueprint(orders_bp, url_prefix='/api')
app.register_blueprint(order_details_bp, url_prefix='/api')

if __name__ == "__main__":
    with app.app_context():
        db.create_all()  # Create tables if they don't exist
    app.run(debug=True)
