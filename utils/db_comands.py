import sqlite3
from pathlib import Path

CAMINHO_DB = Path(__file__).parent.parent / "data_base.db"
print(CAMINHO_DB)

def execute_command(command, value=None):
    conn = sqlite3.connect(CAMINHO_DB)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    
    if value is None:
        cursor.execute(command)
    else:
        cursor.execute(command, value)
    
    conn.commit()  # garante que INSERT/UPDATE/DELETE sejam salvos
    
    if command.strip().upper().startswith("SELECT"):
        rows = cursor.fetchall()
        return rows
        return [dict(row) for row in rows]  # retorna lista de dicionários
    else:
        return cursor.lastrowid  # retorna o id gerado ou 0 se não tiver