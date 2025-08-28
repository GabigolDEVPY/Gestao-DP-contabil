import sys 
sys.dont_write_bytecode = True
from utils.db_comands import execute_command

class Gerenciamento:
    @staticmethod
    def retornar_periodo():
        meses = [
            {"Janeiro": 1},{"Fevereiro": 2},{"Março": 3},{"Abril": 4},{"Maio": 5},{"Junho": 6},{"Julho": 7},{"Agosto": 8},{"Setembro": 9},{"Outubro": 10},{"Novembro": 11},{"Dezembro": 12}]
        contas = execute_command("SELECT * FROM contas WHERE empresa_id = ? AND conta_data = ?")
        