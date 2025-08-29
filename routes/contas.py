from flask import Blueprint, render_template
from utils.func_contas import Contas

contas_bp = Blueprint('contas', __name__)

@contas_bp.route("/contas", methods=["GET"])
def return_page():
    contas = Contas.retornar_contas()
    return render_template("contas.html", aba="contas", contas=contas)