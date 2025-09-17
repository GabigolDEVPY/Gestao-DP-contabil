import sys
sys.dont_write_bytecode = True
import sqlite3
from pathlib import Path

CAMINHO_DB = Path(__file__).parent.parent / "data_base.db"

def execute_command(command, value=None):
    conn = sqlite3.connect(CAMINHO_DB, timeout=30, check_same_thread=False)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA journal_mode=WAL;")
    conn.execute("PRAGMA busy_timeout = 5000;")

    cursor = conn.cursor()
    try:
        if value is None:
            cursor.execute(command)
        else:
            cursor.execute(command, value)
        
        if command.strip().upper().startswith("SELECT"):
            rows = cursor.fetchall()
            return [dict(row) for row in rows]  
        else:
            conn.commit()
            return cursor.lastrowid
    finally:
        cursor.close()
        conn.close()
