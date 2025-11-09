from flask import Blueprint

reports_bp = Blueprint("reports", __name__)

@reports_bp.route("/")
def reports_home():
    return "Reports Page"
