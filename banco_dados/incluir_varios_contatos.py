from mysql.connector.errors import ProgrammingError
from bd import nova_conexao

sql = """
    INSERT INTO contatos (nome, tel) VALUES (%s, %s)
"""
args = [('Bia', '98765-4321'),
        ('Leo', '98765-4321')]


with nova_conexao() as conexao:
    try:
        cursor = conexao.cursor()
        cursor.executemany(sql, args)
        conexao.commit()
    except ProgrammingError as e:
        print(f'Erro: {e.msg}')
    else:
        print(f'Foram incluídos {cursor.rowcount} registros!')
