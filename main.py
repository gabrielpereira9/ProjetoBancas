from flask import *




app = Flask(__name__)


@app.route('/', methods=['POST','GET'])
def pag_principal():
    return render_template('index.html')


@app.route('/fazerlogin', methods=['POST'])
def fazerlogin():
    login_user = request.form.get('usuario')
    senha_user = request.form.get('senha')
    tipo = request.form.get('tipo')

    if len(login_user) == 0 or len(senha_user) == 0:
        return render_template('index.html', error="Usuário e senha são obrigatórios.")

    if tipo == 'cliente':

        logado = False
        for usuario in clientes:
            if usuario[0] == login_user and usuario[1] == senha_user:
                nome_logado = usuario[2]
                logado = True
                
                break

        if logado == True:

            return render_template('pagPrincipalClientes.html', nome=nome_logado)
        else:
            return render_template('index.html', error="Usuário ou senha incorretos.")
    
    else:

        logado = False

        for usuario in vendedores:
            if usuario[0] == login_user and usuario[1] == senha_user:
                nome_logado = usuario[2]
                logado = True
                break

        if logado == True:
            
            return render_template('pagPrincipalVendedores.html', nome=nome_logado)
        else:
            return render_template('index.html', error="Usuário ou senha incorretos.")    

    
@app.route('/mostrar_loja/<nome_loja>', methods=['GET'])
def mostrar_pagina_loja(nome_loja):

    if nome_loja == 'burguesa':
        return render_template('pagina_burguesa.html')
    elif nome_loja == 'martins':
        return render_template('pagina_martins.html')
    elif nome_loja == 'martins':
        return render_template('pagina_assis.html')
    elif nome_loja == 'hello':
        return render_template('pagina_hello.html')       
    else:
        return 'falta fazer'
    
        

        

if __name__ == '__main__':
    app.run(debug=True)




