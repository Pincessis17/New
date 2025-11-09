from flask import Blueprint

sales_bp = Blueprint("sales", __name__)

@sales_bp.route("/")
def sales_home():
    return "Sales Page"
