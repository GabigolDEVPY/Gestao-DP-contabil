from flask import Blueprint, render_template, request, redirect, url_for

empresas_bp = Blueprint('empresas', __name__)

@empresas_bp.route("/empresas", methods=["GET"])
def return_page():
        empresas = [{"id": 1,"nome": "TechMaster LTDA","cnpj": "12.345.678/0001-90"}]
        return render_template("index.html", aba="empresas", empresas=empresas)


@empresas_bp.route("/empresas/empresa", methods=["POST"])
def return_empresa():
    dados = request.form.to_dict()
    print(dados)
    print("deu certo")
    return render_template("index.html", aba="empresas", empresas="12")