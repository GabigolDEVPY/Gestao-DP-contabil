from flask import Blueprint, render_template, request, redirect, url_for, flash
from utils.func_contas import Contas

contas_bp = Blueprint('contas', __name__)

@contas_bp.route("/contas", methods=["GET"])
def return_page():
    contas, contas_privadas = Contas.retornar_contas()
    return render_template("contas.html", contas=contas, contas_privadas=contas_privadas)


@contas_bp.route("/contas/criar", methods=["POST"])
def criar_conta():
    result = Contas.criar_contas(dados=request.form.to_dict())
    if result:
        flash(result)
    return redirect(url_for("contas.return_page"))

@contas_bp.route("/contas/delete", methods=["POST"])
def delete_conta():
    result = Contas.deletar_conta(dados=request.form.to_dict())
    if result:
        flash(result)
    return redirect(url_for("contas.return_page"))


@contas_bp.route("/contas/edit", methods=["POST"])
def edit_conta():
    result = Contas.editar_conta(dados=request.form.to_dict())
    if result:
        flash(result)
        return redirect(url_for("contas.return_page"))
    return redirect(url_for("contas.return_page"))
