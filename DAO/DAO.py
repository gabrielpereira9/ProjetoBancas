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
    sq = f"SELECT nome, estado, profissao, email from usuario where email='{user}' and senha='{senha}'  "
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

    cur.close()
    conn.close()
    return exito