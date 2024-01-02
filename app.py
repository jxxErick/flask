from flask_ngrok import run_with_ngrok
from flask import Flask, jsonify

app = Flask(__name__)
run_with_ngrok(app)  

@app.route('/index')
def index():
    dados_planilha = [
        {"Nome": "Alice", "Idade": 25, "Cargo": "Desenvolvedor"},
        {"Nome": "Bob", "Idade": 30, "Cargo": "Analista de Dados"},
        {"Nome": "Charlie", "Idade": 28, "Cargo": "Designer"}
    ]

    return jsonify(dados_planilha)

if __name__ == '__main__':
    app.run()