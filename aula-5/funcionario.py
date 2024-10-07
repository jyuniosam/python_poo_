class Funcionario:
    def __init__(self,nome,salario):
        #estamos mudando a visibilidade dos atributos de privado para protegido, dessa forma, as classes filhas poderão acessar os atributos da classe  
        self._nome = nome
        self._salario = salario

    def informacoes(self):
        print(f"Olá {self._nome} seu sálario atual é {self._salario} ")

#CRIANDO CLASSES FILHAS 
class Engenheiro(Funcionario):# A classe Engenheiro está herdado as características da classe Funciónario,que será sua classe mãe 
    def bonusEngenheiro(self):
        self._salario = self._salario * 1.1 #Estamos aumentando o salário em 10%

class Supervisor(Funcionario):
    def relatorio(self):
        print(f"Relatorio do supervisor: O nome do funcionário é {self._nome}")