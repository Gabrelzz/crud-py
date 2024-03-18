import mysql.connector
import config

conexao = config.conectar(config.host, config.user, config.password, config.dbname)
cursor = conexao.cursor()

#EDITAR ID PARA PODER ATUALIZAR A SUA TABELA
id_produto = ""
#EDITAR NOME PARA ATUALIZAR UM PRODUTO NA TABELA!
produto = ""
#EDITAR VALOR PARA ATUALIZAR O VALOR DO PRODUTO NA TABELA!
valor = ""

comando = f'UPDATE estoque SET valor = {valor} WHERE id = {id_produto}'
cursor.execute(comando)
conexao.commit()


cursor.close()
conexao.close()