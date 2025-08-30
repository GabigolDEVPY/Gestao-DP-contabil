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
            empresa["periodos"] = execute_command("SELECT empresa_id, mes, ano, status FROM periodos WHERE empresa_id = ?", (empresa["empresa_id"],))
            filiais = execute_command("SELECT * FROM empresas_filiais WHERE empresa_id = ?", (empresa["empresa_id"],))
            for filial in filiais:
                filial["contas_pendentes"] = execute_command('SELECT conta_nome, conta_data FROM contas WHERE empresa_id = ? AND conta_status = "Pendente" ', (filial["id_filial"],))
            empresa["filiais"] = filiais    
            empresas.append(empresa) 
        return empresas 
    
    def cadastrar_empresa(dados):
        dados_empresa = tuple(dados.values())
        try:
            result = execute_command("INSERT INTO empresas (empresa_id, empresa_nome, empresa_cnpj) VALUES (?, ?, ?)", dados_empresa)
            contas = execute_command("SELECT conta_nome, conta_codigo FROM contas_modelos WHERE conta_tipo = 'Matriz'")
            for conta in contas:
                conta["empresa_id"] = dados["empresa_id"]
                conta = tuple(conta.values())
                execute_command("INSERT INTO contas (empresa_id, conta_nome, conta_codigo) VALUES (?, ?, ?)", conta)
            return None
        except Exception:
            return ("Erro ao cadastrar empresa, o ID já está em uso!")


