import os
from webbrowser import get
import requests
from flask import *
app = Flask(__name__)

@app.route("/primeirarota/", methods=['post', 'get'])
def ok(nome, senha):
    if request.form == 'post':
        return str(request.form)
    elif request.form == 'get':
        return 'Nome: '+nome+' '+'Senha: '+senha
app.run(host="0.0.0.0", port=2000, debug=False)
