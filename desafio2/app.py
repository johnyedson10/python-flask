from flask import Flask, render_template, request

# dá inicio ao flask
app = Flask(__name__)

# GET e POST
# GET: coletar os dados
#POST: insere dados
@app.route('/', methods=['GET e POST'])  
# @app.route('/'): Define que este código deve ser executado quando alguém acessar a página inicial do seu site (a raiz, representada pela barra /).
# methods=['GET', 'POST']: Define quais tipos de "conversas" o servidor aceita nesse endereço.
#def é função no python
def cadastro():
    if request.method == 'POST':
       nome      = request.form.get('nome')
       telefone  = request.form.get('telefone')
    return render_template('cadastro.html') # exibe um arquivo html em resposta a uma requisição do usuário

# isso faz o projeto rodar
if __name__ == '__Main__':
    app.run(debug=True, port=8081)
