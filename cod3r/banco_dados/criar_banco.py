from mysql.connector import connect
from configuracao import get_ssl_cert
import json


def read_params():
    with open('parametros.json', 'r') as openfile:
        params = json.load(openfile)
    params['ssl_ca'] = get_ssl_cert()
    return params


conexao = connect(**read_params())

cursor = conexao.cursor()
cursor.execute('CREATE DATABASE IF NOT EXISTS agenda')
