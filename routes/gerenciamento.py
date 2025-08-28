from flask import Blueprint, render_template, request, redirect, url_for
from utils.func_gerenciamento import Gerenciamento

gerenciamento_bp = Blueprint('gerenciamento', __name__)

@gerenciamento_bp.route("/gerenciamento", methods=["GET"])
def return_page():
        return render_template("gerenciamento.html")



@gerenciamento_bp.route("/gerenciamento/empresa", methods=["POST"])
def return_empresa():
        dados = request.form.to_dict()
        print(dados)
        contas = Gerenciamento.retornar_periodo(dados)
        return render_template("gerenciamento.html", contas=contas)


