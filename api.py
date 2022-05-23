import os
import requests
from flask import *
app = Flask(__name__)

@app.route("/primeirarota/<nome>/<senha>")
def ok(nome,senha):
    return "Nome: "+nome +' '+"Senha: "+senha

app.run(host="0.0.0.0", port=2000, debug=False)

