import sys
sys.dont_write_bytecode = True
from waitress import serve
from app import app
import logging
from werkzeug.middleware.proxy_fix import ProxyFix
from flask import request
from utils.db_comands import create_database


@app.before_request
def log_request_info():
    app.logger.info(f"Request: {request.method} {request.url}")
    
@app.after_request
def log_response_info(response):
        app.logger.info(f"{request.method} {request.url} -> {response.status_code}")
        return response
    

if __name__ == "__main__":
    port = 5600
    logging.basicConfig(level=logging.INFO)
    app.wsgi_app = ProxyFix(app.wsgi_app)
    create_database()
    print(f"Server rodando na porta 5600")
    serve(app, host="0.0.0.0", port=port)