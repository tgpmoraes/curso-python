from mysql.connector.errors import ProgrammingError
from bd import nova_conexao


try:
    with nova_conexao() as conexao:
        try:
            cursor = conexao.cursor()
            cursor.execute('SHOW TABLES')

            for i, tabela in enumerate(cursor, start=1):
                print(f'Tabela {i}: {tabela[0]}')
        except ProgrammingError as e:
            print(f'Erro: {e.msg}')
except ProgrammingError as e:
    print(f'Erro CONEXÃO: {e.msg}')
