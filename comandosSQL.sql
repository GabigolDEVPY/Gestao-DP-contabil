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

CREATE TABLE IF NOT EXISTS contas (
    id INTEGER PRIMARY KEY AUTOINCREMENT ,
    empresa_id INT NOT NULL UNIQUE,
    conta_nome VARCHAR(100) NOT NULL "RANDOM"
    conta_status VARCHAR(50) DEFAULT "PENDENTE"
    conta_valor_total VARCHAR(100) DEFAULT 0
    conta_descricao VARCHAR(500) 
    conta_valor_fechado VARCHAR(100) DEFAULT 0
    conta_data TIME NOT NULL
    conta_codigo VARCHAR(100) NOT NULL UNIQUE

SELECT * FROM empresas;

INSERT INTO empresas (empresa_id, empresa_nome, empresa_cnpj) VALUES (
    433,
    'A melhor',
    '1231233773323'
)