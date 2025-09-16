import sys 
sys.dont_write_bytecode = True
from utils.db_comands import execute_command
import sqlite3

class Dashboard:
    @staticmethod
    def return_dashboard():
        dados = execute_command("SELECT * FROM contas")
        contas = {
        "empresas": len(execute_command("SELECT * FROM empresas")),
        "fazendo":  sum(1 for dado in dados if dado.get("conta_status") =="Fazendo"),
        "pendente":  sum(1 for dado in dados if dado.get("conta_status") =="Pendente"),
        "feito": sum(1 for dado in dados if dado.get("conta_status") =="Feito")
        }
        print(contas)
        return contas