from flask import Flask
from flask_talisman import Talisman # type: ignore
from flask_utils import init_app


def create_app() -> Flask:
    """Create the Flask application factory"""
    app = Flask(__name__)
    
    # important security headers
    Talisman(app)
    
    # register common functionality (error handling, etc)
    init_app(app)

    from .routes.root import bp as root_bp

    app.register_blueprint(root_bp)

    return app
