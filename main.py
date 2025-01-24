from flask import *

import dao


app = Flask(__name__)

app.secret_key = 'Khggj3h424j23JSMD@'


@app.route('/', methods=['POST','GET'])
def pag_principal():
    return render_template('index.html')


@app.route('/fazerlogin', methods=['POST'])
def fazer_login():
    login_user = request.form.get('login')
    senha_user = request.form.get('senha')
    saida = dao.login(login_user, senha_user)

    if len(saida) > 0:
        session['login'] = login_user
        nome_user = saida[0][0]
        return render_template('home.html', nome=nome_user)
    else:
        return render_template('index.html')


@app.route('/logout' , methods=['POST' , 'GET'])
def sair():
    session.pop('login')
    return render_template('index.html')
    




@app.route('/cadastrarusuario', methods=['POST', 'GET'])
def cadastrar_usuario():
    nome = request.form.get('nome')
    login = request.form.get('login')
    senha = request.form.get('senha')
    

    if dao.inserir_user(nome, login, senha):
        msg= 'usuário inserido com sucesso'
        return render_template('index.html', texto=msg)
    else:
        msg = 'Erro ao inserir usuário'
        return render_template('index.html', texto=msg)

@app.route('/mostrar_cadastro')
def mostrar_pag_cadastro():
    return render_template('pagCadastro.html')


@app.route('/listarusuarios')
def listar_usuarios():

    if 'login' in session:
        dao.listar_usuarios()
        print(usuario)
        return render_template('listarusuarios.html', lista=usuario)   
    else:
        return render_template('index.html')


        

if __name__ == '__main__':
    app.run(debug=True)




