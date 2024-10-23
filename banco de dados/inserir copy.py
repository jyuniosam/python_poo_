import sqlite3

#Estabelecendo a conexão
conexao = sqlite3.connect("departamento.db")

tabela = """
CREATE TABLE IF NOT EXISTS funcionario(
    codigo INTEGER PRIMARY KEY AUTOINCREMENT,
    nome VARCHAR(100),
    salario FLOAT,
    cargo VARCHAR(100)    
);
"""
consulta.execute(tabela)




nome = input("Informe o novo nome do funcionário ")
codigo = int(input("Informe o código do fucnoirário: "))

sq1 = "DELETE FROM funcionario WHERE codigo = ?"

campos = (codigo,)# é preciso colocar uma virgula depois do item pára configurar que temos uma tupla, caso contrário não será aceito como uma tupla válida.

campos = (nome, codigo)

consulta.executte(sq1, campos)

conexao.commit()

print(consulta.rowcount, "linha(s) atualizada(s) com sucesso")

conexão.close() 