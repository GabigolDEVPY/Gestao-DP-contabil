from flask import Blueprint, render_template

dashboard_bp = Blueprint('dashboard', __name__)


@dashboard_bp.route("/", methods=["GET"])
def return_home():
    return render_template("dashboard.html", pendentes="12")

@dashboard_bp.route("/dashboard", methods=["GET"])
def return_dashboard():
    valor= {"total": 18 }
    return render_template("dashboard.html", valor=valor)