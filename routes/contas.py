from flask import Blueprint, render_template

contas_bp = Blueprint('contas', __name__)

@contas_bp.route("/contas", methods=["GET"])
def return_page():
    contas_data = [
        {"descricao": "INSS", "valor": 500.00, "data_vencimento": "2025-07-25"},
        {"descricao": "FGTS", "valor": 300.00, "data_vencimento": "2025-07-30"},
    ]
    return render_template("contas.html", aba="contas", contas=contas_data)