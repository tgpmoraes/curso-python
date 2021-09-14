from mysql.connector import connect
from configuracao import get_ssl_cert
import json


def read_params():
    with open('parametros.json', 'r') as openfile:
        params = json.load(openfile)
    params['ssl_ca'] = get_ssl_cert()
    return params


conexao = connect(connect(**read_params()))

cursor = conexao.cursor()
cursor.execute('SHOW DATABASES')

for i, database in enumerate(cursor, start=1):
    print(f'Banco de Dados {i}: {database[0]}')
