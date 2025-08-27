import sys 
sys.dont_write_bytecode = True
from utils.db_comands import execute_command

class Contas:
    @staticmethod
    def retornar_contas():
        contas = execute_command("SELECT * FROM contas_modelos")
        return contas