import sys
sys.dont_write_bytecode = True
from flask import Flask, render_template
from routes.dashboard import dashboard_bp
from routes.gerenciamento import gerenciamento_bp
from routes.empresas import empresas_bp
from routes.contas import contas_bp
from routes.relatorios import relatorios_bp

def create_app():
    app = Flask(__name__)
    app.register_blueprint(dashboard_bp)
    app.register_blueprint(gerenciamento_bp)
    app.register_blueprint(empresas_bp)
    app.register_blueprint(contas_bp)
    app.register_blueprint(relatorios_bp)
    return app

app = create_app()

@app.route("/", methods=["GET"])
def return_home():
    return render_template("base.html", aba="dashboard")

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5500)