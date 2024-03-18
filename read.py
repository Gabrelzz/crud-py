import mysql.connector
import config

conexao = config.conectar(config.host, config.user, config.password, config.dbname)
cursor = conexao.cursor()

comando = 'SELECT * FROM estoque'
cursor.execute(comando)

#COMANDO PARA EXIBIR TODOS OS CONTEÚDOS DA TABELA DO BANCO DE DADOS.
print (resultado)

cursor.close()
conexao.close()