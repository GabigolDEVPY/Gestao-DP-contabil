from flask import Blueprint, render_template, request, redirect, url_for

gerenciamento_bp = Blueprint('gerenciamento', __name__)

@gerenciamento_bp.route("/gerenciamento", methods=["GET"])
def return_page():
    return render_template("index.html", aba="gerenciamento")

# @gerenciamento_bp.route("/gerenciamento", methods=["POST"])
# def return_empresa():
#     dados = request.form.to_dict()
#     print(dados)
#     print("deu certo")
#     return redirect(url_for("gerenciamento.return_page"))