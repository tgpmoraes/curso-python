from urllib.parse import quote_plus as urlquote
import pandas
from sqlalchemy import create_engine
import pathlib
import json


def get_ssl_cert():
    current_path = pathlib.Path(__file__).parent.parent
    print(current_path)
    return str(current_path / 'banco_dados/BaltimoreCyberTrustRoot.crt.pem')


def read_params():
    with open('banco_dados/parametros.json', 'r') as openfile:
        params = json.load(openfile)
    return params


# Function to extract table to a pandas DataFrame
def extract_table_to_pandas(tablename, db_engine):
    query = "SELECT * FROM {}".format(tablename)
    return pandas.read_sql(query, db_engine)


def get_connection(database):
    ssl_args = {'ssl_ca': get_ssl_cert()}
    params = read_params()
    engineString = (f"mysql+pymysql://{params['user']}:"
                    f"%s@{params['host']}/{database}"
                    % urlquote(params['passwd']))

    engine = create_engine(engineString, pool_recycle=3600,
                           connect_args=ssl_args)
    return engine.connect()


if __name__ == '__main__':
    # Extract the film table into a pandas DataFrame
    df1 = extract_table_to_pandas("film", get_connection('sakila'))
    print(df1.head(3))

    # Extract the customer table into a pandas DataFrame
    df2 = extract_table_to_pandas("customer", get_connection('sakila'))
    print(df2.head(3))


# # Transformation step, join with recommendations data
# film_pdf_joined = film_pdf.join(recommendations)

# # Finish the .to_sql() call to write to store.film
# film_pdf_joined.to_sql("film", db_engine_dwh, schema="store",
#                        if_exists="replace")

# # Run the query to fetch the data
# pd.read_sql("SELECT film_id, recommended_film_ids FROM store.film",
#             db_engine_dwh)
