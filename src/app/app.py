# api em python com servidor em flask
# consultar cep em https://viacep.com.br/

import requests

from flask import Flask, jsonify, json, render_template, request # importa o Flask (servidor), importa o jsonify (formato de JSON) e o request (acessar os dados - requisições)

app = Flask (__name__) # criando uma aplicação com o nome de Flask

@app.route("/",methods = ["GET"])
def index():
    return render_template("index.html")

@app.route("/buscar",methods = ["POST","GET"])
def buscar():
    numerocep = request.form["numerocep"]
    print(f'Printando: {numerocep}')
    try:
        res = json.loads(requests.get(f"https://viacep.com.br/ws/{numerocep}/json/").text) # chama a API externa passando o número do CEP solicitado
        return(jsonify(res)) # retorna na tela um JSON com os dados do CEP solicitado
    except (Exception) as error:
        print("Erro ao buscar CEP!\n", error) # printa erro caso o CEP não exista
        return 1

@app.route("/cep/<int:id>",methods=["GET"]) # aqui é definido qual URL que vai chamar esse médodo
def obter_cep(id): # método para buscar o CEP
    try:
        res = json.loads(requests.get(f"https://viacep.com.br/ws/{id}/json/").text) # chama a API externa passando o número do CEP solicitado
        return(jsonify(res)) # retorna na tela um JSON com os dados do CEP solicitado
    except (Exception) as error:
        print("Erro ao buscar CEP!\n", error) # printa erro caso o CEP não exista
        return 1

if __name__ == "__main__": # vai rodar tudo isso apenas se o arquivo principal for acionado
    app.run(port=5000,host="localhost",debug=True) # define em qual porta ele vai rodar e em qual host (localhost)