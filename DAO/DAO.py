import psycopg2

def conectardb():

    con = psycopg2.connect(

        host='localhost',
        database = '3anoifpb',
        user = 'postgres',
        password = 'Per2022'
    )
    return con

conectardb

def login(user,senha):
    con = conectardb()
    cur = con.cursor()
    sq = f"SELECT nome, estado, profissao, email from usuario where email='{user}' and senha='{senha}'  "
    cur.execute(sq)
    saida = cur.fetchall()

    cur.close()
    con.close()

    return saida

def inserir_user(nome, email, estado, profissao, senha):

    conn = conectardb()
    cur = conn.cursor()
    try:
        sql = f"INSERT INTO usuario (email, senha, nome, estado, profissao) VALUES ('{email}','{senha}','{nome}', '{estado}', '{profissao}' )"
        cur.execute(sql)

        sql2 = f"INSERT INTO carteira (email_usuario) VALUES('{email}')"
        cur.execute(sql2)


    except psycopg2.IntegrityError:
        conn.rollback()
        exito = False
    else:
        conn.commit()
        exito = True

    cur.close()
    conn.close()
    return exito