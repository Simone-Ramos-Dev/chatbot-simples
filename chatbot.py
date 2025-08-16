# Mapeia as perguntas e suas respostas correspondentes
# O ideal é usar frases curtas e diretas como chaves para facilitar a correspondência
respostas = {
    "ola": "Olá! Como posso ajudar você hoje?",
    "oi": "Oi! O que você gostaria de saber?",
    "como voce esta": "Eu sou um programa de computador, mas estou funcionando perfeitamente! E você?",
    "qual seu nome": "Eu sou um chatbot simples, criado para demonstrar programação em Python.",
    "obrigado": "De nada! Fico feliz em ajudar.",
    "ajuda": "Posso responder a perguntas sobre Python. Tente perguntar 'o que e python?' ou 'como voce esta?'."
}

def iniciar_chatbot():
    print("Bem-vindo ao Chatbot Simples!")
    print("Você pode conversar comigo. Digite 'sair' para encerrar.")
    
    while True:
        # Pega a entrada do usuário e converte para minúsculas
        pergunta_usuario = input("Você: ").lower()
        
        # Condição de saída do loop
        if pergunta_usuario == "sair":
            print("Chatbot: Até logo! Foi um prazer conversar com você.")
            break
        
        # Verifica se a pergunta do usuário está no dicionário de respostas
        # Usamos `in` para verificar se a entrada do usuário está contida em alguma chave
        encontrou_resposta = False
        for chave, valor in respostas.items():
            if chave in pergunta_usuario:
                print(f"Chatbot: {valor}")
                encontrou_resposta = True
                break
        
        # Se nenhuma resposta for encontrada, dá uma resposta genérica
        if not encontrou_resposta:
            print("Chatbot: Desculpe, não entendi. Você pode tentar reformular a pergunta?")

# Inicia o chatbot
iniciar_chatbot()