import sys 
sys.dont_write_bytecode = True
from utils.db_comands import execute_command

class Gerenciamento:
    @staticmethod
    def retornar_periodo(dados):
        print("dados no back", dados)
        data = f"{dados["mes"]}/{dados["ano"]}"
        print(data)
        contas = execute_command("SELECT * FROM contas WHERE empresa_id = ? AND conta_data = ?", (dados["codigo"], data))
        print(contas)
        return contas
    
    @staticmethod
    def editar_contas(dados):
        print("dadosssssssssssssssss", dados)
        # result = execute_command("UPDATE contas SET conta_status = ?, conta_valor_total = ?, conta_descricao = ?, conta_valor_fechado = ? WHERE conta_id = ?", (dados["id_conta"]))
        return 1


