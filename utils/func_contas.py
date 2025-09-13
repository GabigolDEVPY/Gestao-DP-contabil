import sys 
sys.dont_write_bytecode = True
from utils.db_comands import execute_command
import sqlite3

class Contas:
    @staticmethod
    def retornar_contas():
        contas = execute_command("SELECT * FROM contas_modelos")
        contas_privadas = execute_command("SELECT * FROM contas_privadas")
        return contas, contas_privadas
    
    @staticmethod
    def criar_contas(dados):
        del dados["tipo_conta"]
        try:
            if "id_empresa" in dados:
                execute_command("INSERT INTO contas_privadas (empresa_id, conta_nome, conta_codigo, conta_tipo) VALUES (?, ?, ?, ?)", tuple(dados.values()))
                return
            else:
                execute_command("INSERT INTO contas_modelos (conta_nome, conta_codigo, conta_tipo) VALUES (?, ?, ?)", tuple(dados.values()))
        except sqlite3.IntegrityError as e: 
            if "UNIQUE constraint failed" in str(e):
                return "Já existe uma conta cadastrada com esse códgo ou nome!"
        return