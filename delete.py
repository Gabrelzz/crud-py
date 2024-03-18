import mysql.connector
import config

conexao = config.conectar(config.host, config.user, config.password, config.dbname)
cursor = conexao.cursor()

#EDITAR ID PARA PODER DELETAR O PRODUTO DA SUA TABELA
id_produto = 3
#EDITAR NOME PARA DELETAR UM PRODUTO NA TABELA!
produto = ""
#EDITAR VALOR PARA DELETAR O VALOR DO PRODUTO NA TABELA!
valor = ""

comando = f'DELETE FROM estoque WHERE id = {id_produto}'

cursor.execute(comando)
conexao.commit()


cursor.close()
conexao.close()