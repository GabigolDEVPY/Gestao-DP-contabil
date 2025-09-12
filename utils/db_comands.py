import sys
sys.dont_write_bytecode = True
import sqlite3

from pathlib import Path

CAMINHO_DB = Path(__file__).parent.parent / "data_base.db"

def execute_command(command, value=None):
    conn = sqlite3.connect(CAMINHO_DB)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    
    if value is None:
        cursor.execute(command)
    else:
        cursor.execute(command, value)
    
    conn.commit() 
    
    if command.strip().upper().startswith("SELECT"):
        rows = cursor.fetchall()
        return [dict(row) for row in rows]  
    else:
        return cursor.lastrowid  