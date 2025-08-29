import sys 
sys.dont_write_bytecode = True
from utils.db_comands import execute_command

def cadastrar_empresa(dados):
    dados_empresa = tuple(dados.values())
    # try:
    result = execute_command("INSERT INTO empresas (empresa_id, empresa_nome, empresa_cnpj) VALUES (?, ?, ?)", dados_empresa)
    contas = execute_command("SELECT conta_nome, conta_codigo FROM contas_modelos WHERE conta_tipo = 'Matriz'")
    print(contas)
    for conta in contas:
        conta["empresa_id"] = dados["empresa_id"]
        print("contaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", conta)
        conta = tuple(conta.values())
        execute_command("INSERT INTO contas (empresa_id, conta_nome, conta_codigo) VALUES (?, ?, ?)", conta)
    return None
    # except Exception:
    #     return ("Erro ao cadastrar empresa, o ID já está em uso!")
    
cadastrar_empresa({'empresa_id': '3221', 'empresa_nome': 'fadsfsdafdsfsdafsdaf', 'empresa_cnpj': '23765345646'})    