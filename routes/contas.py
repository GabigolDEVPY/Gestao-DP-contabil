from flask import Blueprint, render_template

contas_bp = Blueprint('contas', __name__)

@contas_bp.route("/contas", methods=["GET"])
def return_page():
    print("deu certo")
    valor= {"total": 18 }
    return render_template("contas.html", valor=valor, aba="contas")