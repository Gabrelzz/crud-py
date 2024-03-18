import mysql.connector

host = 'localhost'
dbname = 'banco_crudpy'
user = 'root'
password = 'root'

connect = mysql.connector.connect(host= host, user= user, password= password, database= dbname)
cursor = connect.cursor()
print ("conectado com sucesso ao banco de dados.")

cursor.close()
connect.close()