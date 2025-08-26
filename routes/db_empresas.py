empresas = [
    {
        "id": 1,
        "empresa_id": "001",
        "empresa_nome": "Tech Solutions LTDA",
        "empresa_cnpj": "12.345.678/0001-90",
        "contas_pendentes": [
            {"descricao": "Imposto de Renda", "data": "10/08/2025"},
            {"descricao": "Contribuição Sindical", "data": "15/08/2025"}
        ],
        "periodos": [
            {"mes": "07", "ano": "2025", "status": "Fechado"},
            {"mes": "08", "ano": "2025", "status": "Aberto"}
        ],
        "filiais": [
            {
                "id": 11,
                "nome": "Filial São Paulo",
                "cnpj": "12.345.678/0002-70",
                "contas_pendentes": [
                    {"descricao": "IPTU", "data": "05/08/2025"}
                ]
            },
            {
                "id": 12,
                "nome": "Filial Rio de Janeiro",
                "cnpj": "12.345.678/0003-50",
                "contas_pendentes": [
                    {"descricao": "Conta de Energia", "data": "20/08/2025"}
                ]
            },
            {
                "id": 13,
                "nome": "Filial Curitiba",
                "cnpj": "12.345.678/0004-30",
                "contas_pendentes": []
            }
        ]
    }
]