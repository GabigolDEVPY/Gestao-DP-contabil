from flask import Blueprint, render_template, request, redirect, url_for, session
from utils.func_gerenciamento import Gerenciamento
import ast
import json

gerenciamento_bp = Blueprint('gerenciamento', __name__)

@gerenciamento_bp.route("/gerenciamento", methods=["GET"])
def return_page():
        if "dados" in session:
                return redirect(url_for("gerenciamento.return_empresa"))
        return render_template("gerenciamento.html")



@gerenciamento_bp.route("/gerenciamento/empresa", methods=["POST", "GET"])
def return_empresa():
        dados = request.form.to_dict()
        if "new" in dados:
                contas = Gerenciamento.retornar_periodo(dados)
        if "dados" in session:
                contas, empresa, data = Gerenciamento.retornar_periodo(session["dados"])
        return render_template("gerenciamento.html", contas=contas, empresa=empresa, data=data)

@gerenciamento_bp.route("/gerenciamento/empresa/edit", methods=["POST"])
def edit_contas():
        dados = request.form.to_dict()
        result = Gerenciamento.editar_contas(dados)
        return redirect(url_for("gerenciamento.return_empresa"))
