import sys
sys.dont_write_bytecode = True
from flask import Flask, render_template, session
from routes.dashboard import dashboard_bp
from routes.gerenciamento import gerenciamento_bp
from routes.empresas import companies_bp
from routes.accounts import accounts_bp
from routes.relatorios import relatorios_bp

def create_app():
    app = Flask(__name__)
    app.secret_key = "fjasdjfksdf908432rnf4hn29f3"
    app.register_blueprint(dashboard_bp)
    app.register_blueprint(gerenciamento_bp)
    app.register_blueprint(companies_bp)
    app.register_blueprint(accounts_bp)
    app.register_blueprint(relatorios_bp)
    return app

app = create_app()

# app.run(debug=True, port=5600, host="0.0.0.0")
