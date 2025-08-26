import sys
sys.dont_write_bytecode = True
from flask import Blueprint, render_template, request, redirect, url_for
from routes.db_empresas import empresas
from utils.func_empresas import Empresa

empresas_bp = Blueprint('empresas', __name__)




@empresas_bp.route("/empresas", methods=["GET"])
def return_page():
        empresas = Empresa.retornar_empresas()
        return render_template("empresas.html", aba="empresas", empresas=empresas)


@empresas_bp.route("/empresas/empresa", methods=["POST"])
def return_empresa():
        dados = request.form.to_dict()
        print(dados)
        print("deu certo")
        return render_template("empresas.html", aba="empresas", empresas="12")