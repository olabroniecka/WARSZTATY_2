from mysql.connector import connect

def connect_to_bd():  # cnx, cursor
    cnx = connect(
        user='root',
        password='coderslab',
        database='communicator_db'
    )
    cursor = cnx.cursor()

    return cnx.cursor

def close_connetcion(cnx, cursor):
    cursor.close()
    cnx.close()