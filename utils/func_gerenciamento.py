import sys 
from flask import session
sys.dont_write_bytecode = True
from utils.db_comands import execute_command

class Gerenciamento:
    @staticmethod
    def retornar_periodo(dados):
        if "new" in dados:
            del dados["new"]
        session["dados"] = dados
        data = f"{dados['mes']}/{dados['ano']}"
        contas = execute_command("SELECT * FROM contas WHERE empresa_id = ? AND conta_data = ?", (dados["codigo"], data))
        empresa = execute_command("SELECT empresa_nome FROM empresas WHERE empresa_id = ?", (dados["codigo"],))[0]["empresa_nome"]
        return contas, empresa, data

    
    @staticmethod
    def editar_contas(dados):
        result = execute_command("UPDATE contas SET conta_valor_total = ?, conta_valor_fechado = ?, conta_status = ?, conta_descricao = ? WHERE id = ?", tuple(dados.values()))
        return 1


