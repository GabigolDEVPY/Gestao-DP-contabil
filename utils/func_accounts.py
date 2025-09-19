import sys 
sys.dont_write_bytecode = True
from utils.db_comands import execute_command
import sqlite3

class Accounts:
    @staticmethod
    def return_accounts():
        accounts = execute_command("SELECT * FROM accounts_models")
        private_accounts = execute_command("SELECT * FROM private_accounts")
        return accounts, private_accounts
    
    @staticmethod
    def create_accounts(dados):
        del dados["tipo_conta"]
        try:
            if "id_empresa" in dados:
                execute_command("INSERT INTO private_accounts (empresa_id, conta_nome, conta_codigo, conta_tipo) VALUES (?, ?, ?, ?)", tuple(dados.values()))
                return
            else:
                execute_command("INSERT INTO accounts_models (conta_nome, conta_codigo, conta_tipo) VALUES (?, ?, ?)", tuple(dados.values()))
        except sqlite3.IntegrityError as e: 
            if "UNIQUE constraint failed" in str(e):
                return "Já existe uma conta cadastrada com esse códgo ou nome!"
        return
    
    @staticmethod
    def delete_account(dados):
        try:
            if "empresa_id" in dados:
                execute_command("DELETE FROM private_accounts WHERE conta_codigo = ?", (dados["id"],))
            execute_command("DELETE FROM accounts_models WHERE conta_codigo = ?", (dados["id"],))
        except sqlite3.Error as e: 
            return "Erro ao excluir conta"            

    @staticmethod
    def edit_account(dados):
        try:
            if dados["tipo_conta"] == "publica":
                dados.pop("tipo_conta")
                execute_command("UPDATE accounts_models SET conta_codigo = ?, conta_nome = ?, conta_tipo = ? WHERE conta_codigo = ?", tuple(dados.values()))
            execute_command("UPDATE private_accounts SET conta_codigo = ?, conta_nome = ?, conta_tipo = ? WHERE conta_codigo = ?", tuple(dados.values()))    
        except sqlite3.IntegrityError as e: 
            if "UNIQUE constraint failed" in str(e):
                return "Já existe uma conta cadastrada com esse códgo ou nome!"
            
        
