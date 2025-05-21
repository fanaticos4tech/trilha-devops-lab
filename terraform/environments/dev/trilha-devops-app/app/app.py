# app/app.py
# - Esta é uma aplicação Flask mínima que exibe "Hello DevOps World!" (ou o valor da variável de ambiente NAME), 
# - o hostname do container e permite mudar a cor de fundo via variável de ambiente BACKGROUND_COLOR.
# - Ela escuta na porta 8080 e em 0.0.0.0 para ser acessível de fora do container.

from flask import Flask

import os

import socket

app = Flask(__name__)

@app.route('/')

def hello():

    html = "<h3>Hello {name}!</h3>"

    html += "<b>Hostname:</b> {hostname}<br/>"

    # Tenta obter uma variável de ambiente 'BACKGROUND_COLOR', default para 'white'

    bgcolor = os.environ.get('BACKGROUND_COLOR', 'white')

    html = f"<body style='background-color:{bgcolor};'>{html}</body>"

    return html.format(name=os.getenv("NAME", "DevOps World"), hostname=socket.gethostname())

if __name__ == '__main__':

    # Roda na porta 8080, acessível de qualquer IP

    app.run(host='0.0.0.0', port=8080)
