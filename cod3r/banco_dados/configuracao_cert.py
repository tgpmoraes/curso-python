import mysql.connector
from mysql.connector import errorcode
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

# Construct connection string


try:
    conn = mysql.connector.connect(**read_params())
    print("Connection established")
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Something is wrong with the user name or password")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database does not exist")
    else:
        print(err)
else:
    cursor = conn.cursor()

    # Cleanup
    conn.commit()
    cursor.close()
    conn.close()
    print("Done.")
