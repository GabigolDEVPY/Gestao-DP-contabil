from flask import Blueprint, render_template, request, redirect, url_for

empresas_bp = Blueprint('empresas', __name__)

@empresas_bp.route("/empresas", methods=["GET"])
def return_page():
        empresas = [
                {
                        "id": 1,
                        "nome": "Empresa A",
                        "cnpj": "00.000.000/0001-00",
                        "contas_pendentes": [
                        {"descricao": "Conta de Luz", "data": "2025-07-20"},
                        {"descricao": "Conta de Água", "data": "2025-07-22"}
                        ],
                        "filiais": [
                        {
                        "id": 11,
                        "nome": "Filial 1",
                        "cnpj": "00.000.000/0002-00"
                        },
                        {
                        "id": 12,
                        "nome": "Filial 2",
                        "cnpj": "00.000.000/0003-00"
                        }
                        ]
                        }
                ]
        return render_template("empresas.html", aba="empresas", empresas=empresas)


@empresas_bp.route("/empresas/empresa", methods=["POST"])
def return_empresa():
    dados = request.form.to_dict()
    print(dados)
    print("deu certo")
    return render_template("empresas.html", aba="empresas", empresas="12")