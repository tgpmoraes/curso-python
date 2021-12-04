from mysql.connector.errors import ProgrammingError
from bd import nova_conexao

sql = """
    INSERT INTO contatos (nome, tel) VALUES (%s, %s)
"""
args = [('Teo', '98765-4321'),
        ('Dig', '98765-4321'),
        ('Pet', '98765-4321'),
        ('Mike', '98765-4321'),
        ('Cleo', '98765-4321')]


with nova_conexao() as conexao:
    try:
        cursor = conexao.cursor()
        cursor.executemany(sql, args)
        conexao.commit()
    except ProgrammingError as e:
        print(f'Erro: {e.msg}')
    else:
        print(f'Foram incluídos {cursor.rowcount} registros!')
