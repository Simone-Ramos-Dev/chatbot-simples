from flask import Flask, request, jsonify
from flask_cors import CORS # Necessário para o frontend

# Configuração do Flask
app = Flask(__name__)
CORS(app) # Habilita o CORS para que o HTML possa se conectar

# Mapeia as perguntas e suas respostas
RESPOSTAS = {
    "ola": "Olá! Como posso ajudar você hoje?",
    "oi": "Oi! O que você gostaria de saber?",
    "como voce esta": "Eu sou um programa de computador, mas estou funcionando perfeitamente! E você?",
    "qual seu nome": "Eu sou um chatbot simples, criado para demonstrar a criação de APIs com Flask.",
    "obrigado": "De nada! Fico feliz em ajudar.",
    "ajuda": "Para ajuda, envie um POST para /api/chat com a chave 'pergunta'.",
}

def obter_resposta_chatbot(pergunta_usuario: str) -> str:
    """
    Processa a pergunta do usuário e retorna a resposta do chatbot.
    """
    pergunta_limpa = pergunta_usuario.lower().strip()
    
    for chave, valor in RESPOSTAS.items():
        if chave in pergunta_limpa:
            return valor
            
    # Resposta padrão
    return "Desculpe, não entendi. Você pode tentar reformular a pergunta?"

@app.route('/api/chat', methods=['POST'])
def chat():
    # 1. Garante que a requisição tem dados JSON
    if not request.is_json:
        return jsonify({"erro": "Requisição deve ser JSON"}), 400

    # 2. Extrai e define a variável 'pergunta'
    data = request.get_json()
    pergunta = data.get('pergunta')

    # 3. Verifica se o campo 'pergunta' existe
    if not pergunta:
        return jsonify({"erro": "O campo 'pergunta' é obrigatório"}), 400

    # 4. Processa a pergunta
    resposta_bot = obter_resposta_chatbot(pergunta)

    # 5. Retorna a resposta no formato JSON
    return jsonify({
        "pergunta_usuario": pergunta,
        "resposta_chatbot": resposta_bot,
    }), 200

if __name__ == '__main__':
    import os
    port = int(os.environ.get("PORT", 5000))  # Pega a porta do ambiente, ou 5000 por padrão
    app.run(host="0.0.0.0", port=port, debug=True)
