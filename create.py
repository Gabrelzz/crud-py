import mysql.connector
import config

conexao = config.conectar(config.host, config.user, config.password, config.dbname)
cursor = conexao.cursor()

#EDITAR NOME PARA ADICIONAR UM PRODUTO NA TABELA!
produto = "Toddy"

#EDITAR VALOR PARA ADICIONAR O VALOR DO PRODUTO NA TABELA!
valor = 13

comando = f'INSERT INTO estoque (produto, valor) VALUES ("{produto}", {valor})'

cursor.execute(comando)

#Usar sempre que for executar um comando que edite o banco de dados.
conexao.commit()

cursor.close()
conexao.close()