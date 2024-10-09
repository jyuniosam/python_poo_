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

#passo3 - Acessar 