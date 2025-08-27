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
            empresa = empresa
            empresa["contas_pendentes"] = execute_command('SELECT conta_nome, conta_data FROM contas WHERE empresa_id = ? AND conta_status = "Pendente" ', (empresa["empresa_id"],))
            empresa["periodos"] = execute_command("SELECT empresa_id, mes, ano, status FROM periodos WHERE empresa_id = ?", (empresa["empresa_id"],))
            empresa["filiais"] = execute_command("SELECT * FROM empresas_filiais WHERE empresa_id = ?", (empresa["empresa_id"],))
            empresas.append(empresa)
        print(empresas)    
        return empresas    

            
        
        
Empresa = Empresa
Empresa.retornar_empresas()        
        