import sys
sys.dont_write_bytecode = True
from flask import Flask, render_template
from routes.dashboard import dashboard_bp
from routes.gerenciamento import gerenciamento_bp

def create_app():
    app = Flask(__name__)
    app.register_blueprint(dashboard_bp)
    app.register_blueprint(gerenciamento_bp)
    return app

app = create_app()

@app.route("/", methods=["GET"])
def return_home():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True, host="localhost", port=5500)