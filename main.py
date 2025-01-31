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
    tipo_user = request.form.get('tipo')
    saida = dao.login(login_user, senha_user, tipo_user)

    if len(saida) > 0:
        session['login'] = login_user
        nome_user = saida[0][0]

        if tipo_user == 'vendedor':
            return render_template('pagPrincipalVendedores.html', nome=nome_user)
        else:
            return render_template('pagPrincipalClientes.html', nome=nome_user)
        
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
    tipo = request.form.get('tipo')
    
    print(nome, login, senha, tipo)

    if dao.inserir_user(nome, login, senha, tipo):
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

@app.route('/cadastrar_produto', methods=['POST', 'GET'])
def cadastrar_produto():
    nome_produto = request.form.get('nome_produto')
    estoque = int(request.form.get('estoque'))
    preco = float(request.form.get('preco'))
    if dao.inserirProduto(nome_produto, preco, estoque):
        msg = 'Produto inserido com sucesso'
        return render_template('index.html', texto=msg)
    else:
        msg = 'Erro ao inserir produto'
        return render_template('index.html', texto=msg)


@app.route ('/listar_produto',  methods = ['GET'])
def listar_produto():
    if 'login' in session:
        produtos = dao.listar_produto()
        print(produtos)
        return render_template('listarproduto.html', lista=produtos)   
    else:
        return render_template('index.html')



if __name__ == '__main__':
    app.run(debug=True)




