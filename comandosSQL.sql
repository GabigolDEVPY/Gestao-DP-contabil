-- Active: 1756167730368@@127.0.0.1@3306

CREATE TABLE IF NOT EXISTS empresas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    empresa_id INT NOT NULL UNIQUE,
    empresa_nome VARCHAR(100) NOT NULL UNIQUE,
    empresa_cnpj VARCHAR(100) NOT NULL 
) ;
CREATE TABLE IF NOT EXISTS empresas_filiais (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    empresa_id INT NOT NULL,
    empresa_nome VARCHAR(100) NOT NULL,
    empresa_cnpj VARCHAR(100) NOT NULL,
    FOREIGN KEY (empresa_id) REFERENCES empresas(empresa_id)
) ;


-- contas de cada empresa, individual
CREATE TABLE IF NOT EXISTS contas (
    id INTEGER PRIMARY KEY AUTOINCREMENT ,
    empresa_id INT NOT NULL,
    conta_nome VARCHAR(100) DEFAULT "RANDOM",
    conta_status VARCHAR(50) DEFAULT "PENDENTE",
    conta_valor_total VARCHAR(100) DEFAULT 0,
    conta_descricao VARCHAR(500) ,
    conta_valor_fechado VARCHAR(100) DEFAULT 0,
    conta_data VARCHAR(15),
    conta_codigo VARCHAR(100) NOT NULL
    )

CREATE TABLE periodos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    empresa_id INTEGER,
    data VARCHAR(15),
    status VARCHAR(20) DEFAULT "Pendente"
)

SELECT * FROM empresas;

INSERT INTO empresas (empresa_id, empresa_nome, empresa_cnpj) VALUES (
    433,
    'A melhor',
    '1231233773323'
)

INSERT INTO contas (empresa_id, conta_nome, conta_status, conta_valor_total, conta_descricao, conta_valor_fechado, conta_data, conta_codigo)
VALUES 
(
    "433",
    "Salarios a pagar",
    "Pendente",
    "0",
    "Nada",
    "0",
    "01/2025",
    "21410"
)