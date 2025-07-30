from flask import Blueprint, render_template, request, redirect, url_for

relatorios_bp = Blueprint('relatorios', __name__)

@relatorios_bp.route("/relatorios", methods=["GET"])
def return_page():
    return render_template("relatorios.html")