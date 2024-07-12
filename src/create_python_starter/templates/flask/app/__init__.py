from flask import Flask
from flask_talisman import Talisman  # type: ignore
from dotenv import dotenv_values
from .config import ConfigSchema
from typing import Any
import os
from flask_cors import CORS
from flask_utils import init_app


def create_app() -> Flask:
    """Create the Flask application factory"""
    app = Flask(__name__)

    # validate and load configs
    env_file = f".{os.environ.get("FLASK_ENV")}.env"
    env: dict[str, Any] = dotenv_values(env_file)

    config = ConfigSchema(**env)

    app.config.update(config.model_dump())

    # allow CORS
    CORS(app, methods=["GET", "POST", "PUT", "PATCH", "DELETE", "OPTIONS", "HEAD"])

    # important security headers
    Talisman(app)

    # register common functionality (error handling, etc)
    init_app(app)

    from .routes.root import bp as root_bp

    app.register_blueprint(root_bp)

    return app
