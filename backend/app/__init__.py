from flask import Flask, jsonify
from config import Config
from extensions import db, bcrypt, jwt
from flask_cors import CORS
from app.routes import register_routes




def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # init extensions
    db.init_app(app)
    bcrypt.init_app(app)
    jwt.init_app(app)

    # enable CORS for API routes
    CORS(app, resources={r"/api/*": {"origins": "*"}})

    # simple health-check
    @app.route('/')
    def index():
        return jsonify({'message': 'Flask backend is running'})

    # register blueprints
    register_routes(app)

    return app
