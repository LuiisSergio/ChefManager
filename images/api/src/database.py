import psycopg2
from psycopg2 import pool

DATABASE_NAME 	= "chefmanager"
USER_NAME		= "pguser"
PASSWORD		= "pguser"
HOST			= "LOCALHOST"

database = psycopg2.pool.SimpleConnectionPool(1, 20, user=USER_NAME, password=PASSWORD, host=HOST, port = "5432", database = DATABASE_NAME)

def dbQuery(query, params=None):
    """
    Executa uma consulta SQL com parâmetros e retorna o resultado.
    
    :param query: A consulta SQL a ser executada.
    :param params: Uma tupla de parâmetros para a consulta SQL.
    :return: O resultado da consulta.
    """
    connection = database.getconn()
    if(connection):
        try:
            cursor = connection.cursor()
            cursor.execute(query, params)
            if query.lower().startswith("select"):
                result = cursor.fetchall()
            else:
                connection.commit()
                result = None
            cursor.close()
            return result
        except Exception as e:
            print(f"An error occurred: {e}")
            connection.rollback()
            return None
        finally:
            database.putconn(connection)
    else:
        return None