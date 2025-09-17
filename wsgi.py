import sys
sys.dont_write_bytecode = True
from waitress import serve
from app import app

if __name__ == "__main__":
    print("Server ativo em 5600")
    serve(app, host="0.0.0.0", port=5600)