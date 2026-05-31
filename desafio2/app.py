from flask import Flask, render_template, request

# dá inicio ao flask
app = Flask(__name__)

# GET e POST
# GET: coletar os dados
#POST: insere dados
@app.route('/', methods=['GET e POST'])
#def é função no python
def cadastro():
    if request.method == 'POST':
       nome      = request.form.get('nome')
       telefone  = request.form.get('telefone')
    return render_template('cadastro.html')

# isso faz o projeto rodar
if __name__ == '__Main__':
    app.run(debug=True, port=8081)
