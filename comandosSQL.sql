-- Active: 1757614231733@@127.0.0.1@3306

CREATE TABLE IF NOT EXISTS empresas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    empresa_id INT NOT NULL UNIQUE,
    empresa_nome VARCHAR(60) NOT NULL UNIQUE,
    empresa_cnpj VARCHAR(18) NOT NULL 
) ;




CREATE TABLE IF NOT EXISTS empresas_filiais (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    empresa_id INTEGER NOT NULL,
    id_filial INT NOT NULL UNIQUE,
    empresa_nome VARCHAR(60) NOT NULL UNIQUE,
    empresa_cnpj VARCHAR(18) NOT NULL,
    FOREIGN KEY (empresa_id) REFERENCES empresa(empresa_id)
) ;




-- contas de cada empresa, individual
CREATE TABLE IF NOT EXISTS contas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    empresa_id INT NOT NULL,
    conta_nome VARCHAR(50) DEFAULT "Random",
    conta_status VARCHAR(15) DEFAULT "Pendente",
    conta_valor_total DECIMAL DEFAULT 0,
    conta_descricao VARCHAR(800) ,
    conta_valor_fechado DECIMAL DEFAULT 0,
    conta_data VARCHAR(15),
    conta_codigo VARCHAR(10) NOT NULL
    )



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




ALTER Table contas_modelos 
RENAME COLUMN tipo TO conta_tipo;

CREATE TABLE periodos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    empresa_id INTEGER NOT NULL,
    empresa_data VARCHAR(15) NOT NULL,
    periodo_id VARCHAR(10) UNIQUE NOT NULL
)




SELECT * FROM empresas;




INSERT INTO empresas (empresa_id, empresa_nome, empresa_cnpj) VALUES (
    433,
    'A melhor',
    '1231233773323'
)

INSERT INTO empresas_filiais (empresa_id, id_filial, empresa_nome, empresa_cnpj) VALUES (
    433,
    34,
    'Mahair',
    '433243654354'
)

INSERT INTO contas (empresa_id, conta_nome, conta_status, conta_valor_total, conta_descricao, conta_valor_fechado, conta_data, conta_codigo)
VALUES 
(
    "34",
    "Talvez uma conta",
    "Pendente",
    "0",
    "Nada",
    "0",
    "01/2025",
    "21410"
)

INSERT INTO periodos 
(empresa_id, data, status) 
VALUES (
    433,
    "01/2025",
    "Pendente"
)

INSERT INTO contas_modelos (conta_codigo, conta_nome, conta_tipo)
VALUES
(21403, 'FGTS a Recolher', 'Matriz'),
(21431, 'Recisão', 'Matriz'),
(21401, 'Salarios a Pagar', 'Matriz'),
(21416, 'Salarios a Pagar', 'Filial'),
(12204, 'Adiantamento Salarial', 'Matriz');