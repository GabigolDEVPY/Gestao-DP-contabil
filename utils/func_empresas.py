import sys 
sys.dont_write_bytecode = True
from utils.db_comands import execute_command
# from db_comands import execute_command

class Empresa:
    @staticmethod
    def retornar_empresas():
        dados_empresas = execute_command("SELECT * FROM empresas")
        empresas = []
        for empresa in dados_empresas:
            # {'id': 1, 'empresa_id': 433, 'empresa_nome': 'A melhor', 'empresa_cnpj': '1231233773323'}
            empresa = empresa
            empresa["contas_pendentes"] = execute_command('SELECT conta_nome, conta_data FROM contas WHERE empresa_id = ? AND conta_status = "Pendente" ', (empresa["empresa_id"],))
            empresas.append(empresa)
            print(empresa)
        print(empresas)    
        return empresas    

            
        
        
Empresa = Empresa
Empresa.retornar_empresas()        
        