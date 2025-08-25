from db_comands import execute_command

class Empresa:
    @staticmethod
    def retornar_empresas():
        dados_empresas = execute_command("SELECT * FROM empresas")
        empresas = []
        for empresa in dados_empresas:
            empresa = {}
            id = empresa["empresa_id"]
            
        print(empresas)
        
        
Empresa = Empresa
Empresa.retornar_empresas()        
        