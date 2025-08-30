import sys
sys.dont_write_bytecode = True
from flask import Blueprint, render_template, request, redirect, url_for, flash
from utils.func_empresas import Empresa

empresas_bp = Blueprint('empresas', __name__)




@empresas_bp.route("/empresas", methods=["GET"])
def return_page():
        empresas = Empresa.retornar_empresas()
        return render_template("empresas.html", empresas=empresas)


@empresas_bp.route("/empresas/cadastrar", methods=["POST"])
def cadastrar_empresa():
        dados = request.form.to_dict()
        print(dados)
        result = Empresa.cadastrar_empresa(dados)
        return redirect(url_for("empresas.return_page"))
        if result:
                flash(result)
                return redirect(url_for("empresas.return_page"))
        return redirect(url_for("empresas.return_page"))

@empresas_bp.route("/empresa/criarperiodo", methods=["POST"])
def criar_periodo():
        dados = request.form.to_dict()
        print("Dados front", dados)
        result = Empresa.criar_periodo(dados)
        if result:
                flash(result)
                return redirect(url_for("empresas.return_page"))
        return redirect(url_for("empresas.return_page"))