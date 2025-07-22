from flask import Blueprint, render_template, request, redirect, url_for

gerenciamento_bp = Blueprint('gerenciamento', __name__)

@gerenciamento_bp.route("/gerenciamento", methods=["GET"])
def return_page():
        contas = [
        {
                "codigo": 1,
                "descricao": "Conta de Luz",
                "valor_total": 150.75,
                "valor_fechado": 140.50,
                "descricao_detalhada": "afasdfsdafjsadfsadfsdfasdfsdf"
        },
        {
                "codigo": "002",
                "descricao": "Conta de Água",
                "valor_total": 80.20,
                "valor_fechado": 80.20,
                "descricao_detalhada": "fadsfasdfasdfsdafsdfsdfsdfsadf"
        }
        ]
        return render_template("index.html", aba="gerenciamento", contas=contas)


@gerenciamento_bp.route("/gerenciamento/empresa", methods=["POST"])
def return_empresa():
    dados = request.form.to_dict()
    return render_template("index.html", aba="gerenciamento")

