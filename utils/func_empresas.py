import sys 
sys.dont_write_bytecode = True
from db_comands import execute_command

class Empresa:
    @staticmethod
    def retornar_empresas():
        dados_empresas = execute_command("SELECT * FROM empresas")
        empresas = []
        for empresa in dados_empresas:
            # {'id': 1, 'empresa_id': 433, 'empresa_nome': 'A melhor', 'empresa_cnpj': '1231233773323'}
            empresa = empresa
            contas_pendentes = execute_command("SELECT * FROM contas WHERE id = ?", (empresa["id"],))
            print(contas_pendentes)

            
        
        
Empresa = Empresa
Empresa.retornar_empresas()        
        