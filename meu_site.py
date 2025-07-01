from flask import Flask, render_template

app = Flask(__name__)
 

@app.route('/')
def inicio():
    return render_template ('inicio.html')

@app.route('/contatos')
def conntatos():
    return render_template('contatos.html')

@app.route('/localizacao')
def localizacao():
    return render_template('localizacao.html')

@app.route('/usuarios/<nome_usuario>')
def usuarios(nome_usuario):
    return render_template ('usuarios.html',nome_usuario=nome_usuario)


#colocar o site pra rodar
if __name__ == '__main__':
    app.run(debug=True)


#servidor do heroku