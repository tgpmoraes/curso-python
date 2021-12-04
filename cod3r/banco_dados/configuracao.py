from mysql.connector import connect
import pathlib
import json


def get_ssl_cert():
    current_path = pathlib.Path(__file__).parent.parent
    print(current_path)
    return str(current_path / 'banco_dados/BaltimoreCyberTrustRoot.crt.pem')


def read_params():
    with open('parametros.json', 'r') as openfile:
        params = json.load(openfile)
    params['ssl_ca'] = get_ssl_cert()
    return params


print(connect(**read_params()))
