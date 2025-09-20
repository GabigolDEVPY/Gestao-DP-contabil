import sys
sys.dont_write_bytecode = True
from flask import Blueprint, render_template, request, redirect, url_for, flash
from utils.func_empresas import Empresa

companies_dp = Blueprint('empresas', __name__)




@companies_dp.route("/empresas", methods=["GET"])
def return_page():
        return render_template("empresas.html", empresas=Empresa.retornar_empresas())


@companies_dp.route("/empresas/cadastrar", methods=["POST"])
def cadastrar_empresa():
        result = Empresa.cadastrar_empresa(request.form.to_dict())
        if result:
                flash(result)
                return redirect(url_for("empresas.return_page"))
        return redirect(url_for("empresas.return_page"))

@companies_dp.route("/empresa/criarperiodo", methods=["POST"])
def criar_periodo():
        result = Empresa.criar_periodo(request.form.to_dict())
        if result:
                flash(result)
                return redirect(url_for("empresas.return_page"))
        return redirect(url_for("empresas.return_page"))