from flask import Blueprint, render_template, request, redirect, url_for
from utils.func_gerenciamento import Gerenciamento
import ast
import json

gerenciamento_bp = Blueprint('gerenciamento', __name__)

@gerenciamento_bp.route("/gerenciamento", methods=["GET"])
def return_page():
        return render_template("gerenciamento.html")



@gerenciamento_bp.route("/gerenciamento/empresa", methods=["POST", "GET"])
def return_empresa():
        dados = request.form.to_dict()
        contas = Gerenciamento.retornar_periodo(dados)
        return render_template("gerenciamento.html", contas=contas, periodo=dados)

@gerenciamento_bp.route("/gerenciamento/empresa/edit", methods=["POST"])
def edit_contas():
        dados = request.form.to_dict()
        print(dados["periodo_conta"])
        periodo = dados.get("periodo_conta", "")
        # dados_back = json.loads(periodo)
        # contas = Gerenciamento.retornar_periodo(dados_back)
        # result = Gerenciamento.editar_contas(dados)
        return render_template("gerenciamento.html")
