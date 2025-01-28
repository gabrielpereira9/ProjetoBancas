import psycopg2

def conectardb():

    con = psycopg2.connect(

        #host='localhost',
        #database = '3anoifpb',
        #user = 'postgres',
        #password = 'Per2022'

        host='dpg-cu8fupjtq21c73et27tg-a.oregon-postgres.render.com',
        database = 'projetobancas',
        user = 'projetobancas_user',
        password = 'pzKHkgaVFhmtor1cv6t8pWdVqJASUyIx'
    )
    return con



def login(user,senha):
    con = conectardb()
    cur = con.cursor()
    sq = f"SELECT login, nome from usuario where login='{user}' and senha='{senha}'  "
    cur.execute(sq)
    saida = cur.fetchall()

    cur.close()
    con.close()

    return saida


def inserir_user(nome, login, senha):

    conn = conectardb()
    cur = conn.cursor()
    try:
        sql = f"INSERT INTO usuario (nome, login, senha ) VALUES ('{nome}','{login}', '{senha}' )"
        cur.execute(sql)

    except psycopg2.IntegrityError:
        conn.rollback()
        exito = False
    else:
        conn.commit()
        exito = True

def cadastroProduto(nome_produto, preco, estoque):
    con = conectardb()
    cur = con.cursor()
    try:
        sql = f"SELECT * FROM produto WHERE nome_produto = '{nome_produto}'"
        cur.execute(sql)
        saida = cur.fetchall()
    except Exception as e:
        print(f"Erro ao consultar o produto: {e}")
        saida = None
    finally:
        cur.close()
        con.close()

    return saida


def inserirProduto(nome_produto, preco, estoque):
   
    conn = conectardb()
    cur = conn.cursor()
    try:
        sql = f"INSERT INTO produto (nome_produto, preco, estoque) VALUES ('{nome_produto}', {preco}, {estoque})"
        cur.execute(sql)
        conn.commit()
        print("Produto inserido com sucesso!")
        return True
    except Exception as e:
        print(f"Erro ao inserir o produto: {e}")
        return False
    finally:
        cur.close()
        conn.close()


        

    cur.close()
    conn.close()
    return exito