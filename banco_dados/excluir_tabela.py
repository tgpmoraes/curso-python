from mysql.connector.errors import ProgrammingError
from bd import nova_conexao


excluir_tabela = """
    DROP TABLE IF EXISTS emails
"""


try:
    with nova_conexao() as conexao:
        try:
            cursor = conexao.cursor()
            cursor.execute(excluir_tabela)
        except ProgrammingError as e:
            print(f'Erro: {e.msg}')
except ProgrammingError as e:
    print(f'Erro CONEXÃO: {e.msg}')
