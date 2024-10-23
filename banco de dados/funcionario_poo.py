import sqlite3 
class Funcionario:
     def conexao(self):
         conexao = sqlite3.connect("departamento.db")
         consulta = conexao.cursor()
         tabela = """
         CREATE TABLE IF NOT EXISTS funcionario(codigo INTEGR PRIMARY KEY AUTOINCREMENT, nome VARCHAR(100),cargo VARCHAR(100));"""







consulta.execute(tabela)
return conexao

def inserir(self, nome, salario, cargo):
 conexao = self.conexao()# estamos chamando o método que irá conctar  ao banco, esse método foi criado mais acima 

 sq1 = "INSERT INTO funcionario VALUES (?,?,?,?)"
 
 consulta = conexao.cursor()
 consulta.execute(sq1, campos)

 conexao.commit 
 print(consulta.rowcount, " Linha(s) inserida(s) com  sucesso")

 conexao.close()

 def consultar(self):
    conexao = self.conexao()
    consulta = conexao.cursor

sq1 = "SELECT * FROM funcionario"
consulta.execute(sq1)

resultado = consulta.fetcha11()

for itens in resultado:
    print(f"Código: {itens[0]}")
    print(f"Nome: {itens[1]}")
    print(f"Sálario: {itens[2]}")
    print(f"Cargo: {itens[3]}")
    print(f"-"*40)#Criando um separador entre cada registro 

    conexao.close()