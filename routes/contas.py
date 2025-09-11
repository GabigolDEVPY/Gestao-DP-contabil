from flask import Blueprint, render_template, request, redirect, url_for
from utils.func_contas import Contas

contas_bp = Blueprint('contas', __name__)

@contas_bp.route("/contas", methods=["GET"])
def return_page():
    contas, contas_privadas = Contas.retornar_contas()
    return render_template("contas.html", contas=contas, contas_privadas=contas_privadas)


@contas_bp.route("/contas/criar", methods=["POST"])
def criar_conta():
    dados = request.form.to_dict()
    print(dados)
    Contas.criar_contas(dados)
    return redirect(url_for("contas.return_page"))