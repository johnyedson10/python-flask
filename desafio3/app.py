from flask import Flask, render_template, request

# iniciando o Flask
app = Flask(__name__)

# GET e POST
# GET: recebendo os informações
#POST: inserindo dados
@app.route('/', methods=['GET e POST'])

# def é função
def cad_contas():
    if request.method == 'POST':
        data_venc      = request.form.get('data_venc')
        data_pag       = request.form.get('data_pag')
        descricao      = request.form.get('descricao')
        valor          = request.form.get('valor')
        status         = request.form,get('pago, pendente, vencido')
    render_template('cad_contas.html')                               
    # rende_template: chama o arquivo cad_contas.html

# roda o projeto
if __name__ == '__Main__':
    app.run(debug=True, port=8081)
    


  


