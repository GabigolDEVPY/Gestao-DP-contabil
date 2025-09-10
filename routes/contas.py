from flask import Blueprint, render_template, request, redirect, url_for
from utils.func_contas import Contas

contas_bp = Blueprint('contas', __name__)

@contas_bp.route("/contas", methods=["GET"])
def return_page():
    contas = Contas.retornar_contas()
    return render_template("contas.html", contas=contas)


@contas_bp.route("/contas/criar", methods=["POST"])
def criar_conta():
    dados = request.form.to_dict()
    print(dados)
    redirect(url_for("contas.return_page"))