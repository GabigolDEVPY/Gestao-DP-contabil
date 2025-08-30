import sys 
sys.dont_write_bytecode = True
from utils.db_comands import execute_command

class Gerenciamento:
    @staticmethod
    def retornar_periodo(dados):
        data = f"{dados["mes"]}/{dados["ano"]}"
        print(data)
        contas = execute_command("SELECT * FROM contas WHERE empresa_id = ? AND conta_data = ?", (dados["codigo"], data))
        return contas

