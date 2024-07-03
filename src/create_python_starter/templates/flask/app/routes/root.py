from flask import Blueprint

bp = Blueprint("root", __name__)


@bp.route("/", methods=["GET"])
def hello_world() -> str:
    """A hello world example endpoint"""
    return "hello world!"
