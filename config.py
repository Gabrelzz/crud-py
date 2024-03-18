import mysql.connector

host = 'localhost'
user = 'root'
password = 'root'
dbname = 'banco_crudpy'

def conectar (host, user, password, dbname):

    try:
        connect = mysql.connector.connect(host= host, user= user, password= password, database= dbname)
    
        print ("Conectado com sucesso ao banco de dados.")
        return connect

    except mysql.connector.Error as err:

        print ("Erro ao conectar ao banco de dados:", {err})
        return connect.close
