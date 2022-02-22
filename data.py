import pandas as pd
import psycopg2
import db_credentials
import os

dbname = 'warehouse'
host = 'warehouse.vacasa.services'
#user = os.environ['user']
#password = os.environ['password']
user = db_credentials.user
password = db_credentials.password

# connect to redshift
def query_helper(sql_statement):
    """
    Executes sql query and retrieves data from Redshift db.
    :param sql_statement: str
    :return: df
    """
    con = psycopg2.connect(dbname=dbname, host=host, user=user, password=password, port=5439)
    # cursor = con.cursor()
    data = pd.read_sql(sql_statement, con)
    con.close()
    return data


