from flask import Flask, request, jsonify, render_template
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Permite requisições do frontend

# --- Lógica simples do chatbot ---
RESPOSTAS = {
    "ola": "Olá! Como posso ajudar você hoje?",
    "oi": "Oi! O que você gostaria de saber?",
    "como voce esta": "Eu sou um programa de computador, mas estou funcionando perfeitamente! E você?",
    "qual seu nome": "Eu sou um chatbot simples, criado para demonstrar a criação de APIs com Flask.",
    "obrigado": "De nada! Fico feliz em ajudar.",
    "ajuda": "Para ajuda, envie um POST para /api/chat com a chave 'pergunta'.",
}

def obter_resposta_chatbot(pergunta_usuario: str) -> str:
    pergunta_limpa = pergunta_usuario.lower().strip()
    for chave, valor in RESPOSTAS.items():
        if chave in pergunta_limpa:
            return valor
    return "Desculpe, não entendi. Você pode tentar reformular a pergunta?"

# --- Rota da API ---
@app.route('/api/chat', methods=['POST'])
def chat():
    if not request.is_json:
        return jsonify({"erro": "Requisição deve ser JSON"}), 400
    data = request.get_json()
    pergunta = data.get('pergunta')
    if not pergunta:
        return jsonify({"erro": "O campo 'pergunta' é obrigatório"}), 400
    resposta_bot = obter_resposta_chatbot(pergunta)
    return jsonify({
        "pergunta_usuario": pergunta,
        "resposta_chatbot": resposta_bot,
    }), 200

# --- Rota do frontend ---
@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')

# --- Inicialização ---
if __name__ == '__main__':
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
