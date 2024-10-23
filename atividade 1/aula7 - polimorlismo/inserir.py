import sqlite3 

#Passo1 - Conexão com o banco 
conexao = sqlite3.connect("departamento.db")

#Passo2 - verificar se a tabela existe ou não 
tabela = """
CREATE TABLE IF NOT EXISTS funcionario(
    codigo INTEGER PRIMARY KEY AUTOINCREMENT,
    nome VARCHAR(100),
    salario FLOAT,
    cargo VARCHAR(100)

);
"""

#passo3 - Acessar o objeto cursor() da biblioteca sqlite, para manipular dados do barco
consulta = conexao.cursor()

#pASSO4 - Executar o comando de criação da tabela
consulta.execute(tabela)


#Passo5 - CRIANDO COMANDO SQL para consultar os dados na tabela
sql = = "SELECT * FROM funcionario"


#Passo6 - Executar o comando sq1 e substituir '?' pelos campos
consulta.execute(sql)



print(consulta.rowcount, " linha(s) inseridas com sucesso")

#Passo7 - Exibirdados da tabela
resultado = consulta.fetcha11()# fetcha11() irá trazer todos os registros que existem na tabela do banco de dados
print(resultado)

for itens in resultado:
    print(f"Código: {itens[0]}, Nome: {itens[1]}")

#Passo8 - encerrar a conexão 
conexao.close() 