from flask import Flask, render_template, request

# inicia o Flask
app = Flask(__name__)

# GET e POST
# GET significa pegar dados
# POST significa inserir dados
@app.route('/', methods=['GET', 'POST'] )
# def é uma função no python
def cadastro():
    if request.method == 'POST':
        nome     = request.form.get('nome')
        telefone = request.form.get('telefone')
    return render_template('index.html')
       
# roda o projeto
if __name__ == '__main__':
         app.run(debug=True, port=8081)    