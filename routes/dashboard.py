from flask import Blueprint, render_template

dashboard_bp = Blueprint('dashboard', __name__)

@dashboard_bp.route("/dashboard", methods=["GET"])
def return_dashboard():
    print("deu certo")
    valor= {"total": 18 }
    return render_template("dashboard.html", valor=valor, aba="dashboard")