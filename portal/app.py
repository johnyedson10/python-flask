from flask import Flask, render_template

# inicia o Flask
app = Flask(__name__)

# primeira rota usando Flask
@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

# Segunda rota usando Flask
@app.route('/contato', methods=['GET'])
def contato():
    return render_template('contato.html')


# Terceira rota usando Flask
@app.route('/sobre', methods=['GET'])
def sobre():
    return '<h1>Sobre a Empresa</h1>'

# Quarta rota usando Flask Página de vendas GET, POST, PUT, DELETE
@app.route('/cadastro', methods=['GET'])
def cadastro():    
    return render_template('cadastro.html')
       


# roda o projeto
if __name__ == '__main__':
         app.run(debug=True, port=8081)    
