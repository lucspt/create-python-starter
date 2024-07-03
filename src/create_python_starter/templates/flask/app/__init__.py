from flask import Flask


def create_app() -> Flask:
    """Create the Flask application factory"""
    app = Flask(__name__)

    from .routes.root import bp as root_bp

    app.register_blueprint(root_bp)

    return app
