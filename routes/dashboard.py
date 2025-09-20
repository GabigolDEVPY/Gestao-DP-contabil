from flask import Blueprint, render_template, redirect, url_for
from utils.func_dashboard import Dashboard

dashboard_bp = Blueprint('dashboard', __name__)


@dashboard_bp.route("/", methods=["GET"])
def return_home():
    return redirect(url_for("dashboard.return_dashboard"))

@dashboard_bp.route("/dashboard", methods=["GET"])
def return_dashboard():
    return render_template("dashboard.html", contas=Dashboard.return_dashboard())