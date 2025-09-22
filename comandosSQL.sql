-- Active: 1757614231733@@127.0.0.1@3306

CREATE TABLE IF NOT EXISTS empresas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    empresa_id INT NOT NULL UNIQUE,
    empresa_nome VARCHAR(60) NOT NULL UNIQUE,
    empresa_cnpj VARCHAR(18) NOT NULL 
);

CREATE TABLE IF NOT EXISTS empresas_filiais (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    empresa_id INTEGER NOT NULL,
    id_filial INT NOT NULL UNIQUE,
    empresa_nome VARCHAR(60) NOT NULL UNIQUE,
    empresa_cnpj VARCHAR(18) NOT NULL,
    FOREIGN KEY (empresa_id) REFERENCES empresas(empresa_id)
);

CREATE TABLE IF NOT EXISTS contas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    empresa_id INT NOT NULL,
    conta_nome VARCHAR(50) DEFAULT "Random",
    conta_status VARCHAR(15) DEFAULT "Pendente",
    conta_valor_total DECIMAL DEFAULT 0,
    conta_descricao VARCHAR(800),
    conta_valor_fechado DECIMAL DEFAULT 0,
    conta_data VARCHAR(15),
    conta_codigo VARCHAR(10) NOT NULL
);

CREATE TABLE IF NOT EXISTS contas_modelos (
    id INTEGER PRIMARY KEY AUTOINCREMENT ,
    conta_nome VARCHAR(60) DEFAULT "RANDOM" UNIQUE,
    conta_codigo VARCHAR(10) NOT NULL UNIQUE,
    conta_tipo VARCHAR(15) DEFAULT "MATRIZ"
);

CREATE TABLE IF NOT EXISTS contas_privadas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    empresa_id INT NOT NULL,
    conta_nome VARCHAR(60) DEFAULT "RANDOM",
    conta_codigo VARCHAR(10) NOT NULL UNIQUE,
    conta_tipo VARCHAR(15) DEFAULT "MATRIZ",
    FOREIGN KEY (empresa_id) REFERENCES empresas(empresa_id)
);

CREATE TABLE IF NOT EXISTS periodos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    empresa_id INTEGER NOT NULL,
    empresa_data VARCHAR(15) NOT NULL,
    periodo_id VARCHAR(10) UNIQUE NOT NULL
);



