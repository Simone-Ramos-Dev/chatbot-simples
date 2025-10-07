# 🤖 Chatbot API com Flask

Este projeto é uma demonstração de uma **API RESTful** simples construída com **Flask**, capaz de receber requisições de chat e retornar respostas predefinidas. Ele é emparelhado com um frontend em HTML/JavaScript que interage consumindo esta API.

## ✨ Destaques do Projeto

* **Python/Flask:** Implementação de um *backend* robusto para a lógica de chat.
* **API RESTful:** Exposição de um *endpoint* único (`/api/chat`) via método **POST**.
* **CORS (Cross-Origin Resource Sharing):** Configuração correta para permitir a comunicação entre o frontend (navegador) e o backend (Flask).
* **Frontend Integrado:** Uso de JavaScript (`fetch` API) para consumir o serviço Flask de forma assíncrona.

## ⚙️ Configuração e Execução

### Pré-requisitos

* Python 3.x
* `pip` (Gerenciador de pacotes Python)

### 1. Configuração do Ambiente

Crie e ative um ambiente virtual e instale as dependências necessárias, incluindo o `flask` e o `flask-cors`:

```bash
# Crie o ambiente virtual
python -m venv venv

# Ative o ambiente virtual (Linux/macOS)
source venv/bin/activate
# Ative o ambiente virtual (Windows)
# .\venv\Scripts\activate

# Instale as dependências
pip install Flask Flask-CORS