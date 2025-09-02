import sys 
sys.dont_write_bytecode = True
from utils.db_comands import execute_command

class Empresa:
    @staticmethod
    def retornar_empresas():
        dados_empresas = execute_command("SELECT * FROM empresas")
        empresas = []
        for empresa in dados_empresas:
            empresa["contas_pendentes"] = execute_command('SELECT conta_nome, conta_data FROM contas WHERE empresa_id = ? AND conta_status = "Pendente" ', (empresa["empresa_id"],))
            empresa["periodos"] = execute_command("SELECT empresa_id, empresa_data, status FROM periodos WHERE empresa_id = ?", (empresa["empresa_id"],))
            empresa["filiais"] = execute_command("SELECT * FROM empresas_filiais WHERE empresa_id = ?", (empresa["empresa_id"],))
            filiais = execute_command("SELECT * FROM empresas_filiais WHERE empresa_id = ?", (empresa["empresa_id"],))
            print(filiais)
            for filial in filiais:
                filial["contas_pendentes"] = execute_command('SELECT conta_nome, conta_data FROM contas WHERE empresa_id = ? AND conta_status = "Pendente" ', (filial["id_filial"],)) 
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
        try:
            execute_command("INSERT INTO periodos (empresa_id, empresa_data) VALUES (?, ?)", (dados['empresa_id'], f"{dados['mes']}/{dados['ano']}"))
        except Exception as e:
            return "Periodo já cadastrado!"
        contas = execute_command("SELECT conta_nome, conta_codigo FROM contas_modelos WHERE conta_tipo = 'Matriz'")
        if contas is None:
            return "Sem contas para criar período"
        for conta in contas:
            conta["empresa_id"] = dados["empresa_id"]
            conta["conta_data"] = f"{dados["mes"]}/{dados["ano"]}"
            conta = tuple(conta.values())
            execute_command("INSERT INTO contas (conta_nome, conta_codigo, empresa_id, conta_data) VALUES (?, ?, ?, ?)", conta)


