from flask import Flask, render_template
from .config import Config

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # import and register blueprints
    from .routes.auth_routes import auth_bp
    from .routes.sales_routes import sales_bp
    from .routes.inventory_routes import inventory_bp
    from .routes.reports_routes import reports_bp

    app.register_blueprint(auth_bp)
    app.register_blueprint(sales_bp, url_prefix="/sales")
    app.register_blueprint(inventory_bp, url_prefix="/inventory")
    app.register_blueprint(reports_bp, url_prefix="/reports")

    @app.route("/")
    def home():
        return render_template("dashboard.html")

    return app
