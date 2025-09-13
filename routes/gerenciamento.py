from flask import Blueprint, render_template, request, redirect, url_for, session, flash
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
                contas, empresa, data = Gerenciamento.retornar_periodo(dados)
                if not empresa:
                        session.clear()
                        flash("Empresa Inexistente")
                        return redirect(url_for("gerenciamento.return_page"))
                elif not contas:
                        session.clear()
                        flash("Periodo não cadastrado!")
                        return redirect(url_for("gerenciamento.return_page"))
                
        if "dados" in session:
                contas, empresa, data = Gerenciamento.retornar_periodo(session["dados"])
        return render_template("gerenciamento.html", contas=contas, empresa=empresa[0]["empresa_nome"], data=data)

@gerenciamento_bp.route("/gerenciamento/empresa/edit", methods=["POST"])
def edit_contas():
        result = Gerenciamento.editar_contas(request.form.to_dict())
        return redirect(url_for("gerenciamento.return_empresa"))
