import sys 
sys.dont_write_bytecode = True
from utils.db_comands import execute_command
import copy

class Empresa:
    @staticmethod
    def retornar_empresas():
        dados_empresas = execute_command("SELECT * FROM empresas")
        empresas = []
        for empresa in dados_empresas:
            empresa["contas_pendentes"] = execute_command('SELECT conta_nome, conta_data FROM contas WHERE empresa_id = ? AND conta_status = "Pendente" ', (empresa["empresa_id"],))
            empresa["periodos"] = execute_command("SELECT empresa_id, empresa_data, status FROM periodos WHERE empresa_id = ?", (empresa["empresa_id"],))
            filiais = execute_command("SELECT * FROM empresas_filiais WHERE empresa_id = ?", (empresa["empresa_id"],))
            def status_periodo(empresa_id=empresa['empresa_id']):        
                for periodo in empresa["periodos"]:
                    contas = execute_command("SELECT empresa_id, conta_status, conta_data FROM contas WHERE empresa_id = ?", (empresa_id,))
                    for conta in contas:
                        if conta["conta_status"] != "Feito":
                            periodo["status"] = "Pendente"
                            break
                        periodo["status"] = "Concluido"  
                    
            empresa["filiais"] = execute_command("SELECT * FROM empresas_filiais WHERE empresa_id = ?", (empresa["empresa_id"],))
            for filial in empresa["filiais"]:
                status_periodo(empresa_id=filial["id_filial"])
                filial["contas_pendentes"] = execute_command('SELECT conta_nome, conta_data FROM contas WHERE empresa_id = ? AND conta_status = "Pendente" ', (filial["id_filial"],)) 
                print(filial["contas_pendentes"])
            empresas.append(empresa) 
        return empresas 
    
    @staticmethod
    def cadastrar_empresa(dados):
        dados_empresa = tuple(dados.values())
        try:
            if len(dados) < 4:
                result = execute_command("INSERT INTO empresas (empresa_id, empresa_nome, empresa_cnpj) VALUES (?, ?, ?)", dados_empresa)
                return None
            execute_command("INSERT INTO empresas_filiais (empresa_id, id_filial, empresa_nome, empresa_cnpj) VALUES (?, ?, ?, ?)", dados_empresa)
            return None
        except Exception:
            return ("Erro ao cadastrar empresa, o ID já está em uso!")
        
    @staticmethod
    def criar_periodo(dados):
        filiais = execute_command("SELECT id_filial FROM empresas_filiais WHERE empresa_id = ?", (dados["empresa_id"],))
        contas = execute_command("SELECT conta_nome, conta_codigo, conta_tipo FROM contas_modelos")
        if contas is None:
            return "Sem contas para criar período"
        def criando_periodo(conta_id=dados["empresa_id"], tipo="Matriz"):
            for conta_original in contas:
                conta = copy.deepcopy(conta_original)
                if conta["conta_tipo"] == tipo:
                    conta["empresa_id"] = conta_id
                    conta["conta_data"] = f"{dados['mes']}/{dados['ano']}"
                    conta.pop("conta_tipo")
                    conta = tuple(conta.values())
                    execute_command("INSERT INTO contas (conta_nome, conta_codigo, empresa_id, conta_data) VALUES (?, ?, ?, ?)", conta)
        criando_periodo()        
        if filiais:
            for filial in filiais:
                criando_periodo(filial["id_filial"], tipo="Filial")
        try:
            execute_command("INSERT INTO periodos (empresa_id, empresa_data) VALUES (?, ?)", (dados['empresa_id'], f"{dados['mes']}/{dados['ano']}"))
        except Exception as e:
            return "Periodo já cadastrado!"
                


