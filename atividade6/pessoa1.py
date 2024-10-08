class Pessoa: # superclasse ou classe mãe
    def __init__(self, nome, idade):
        self._nome = idade
        self._idade = idade


        def info(self):
            print(f"Nome: {self._nome} Idade: {self._idade}")

#classe filha 1 - Aluno
class Aluno(Pessoa):
    def __init__(self, nome,idade, matrícula):
        super().__init__(nome, idade)# utlizando um construtor da classe mãe
        self._matrícula = matrícula# estamos utilizando um atributo exclusivo da classe filha

        def estudar(self):
            print(f"{self._nome}, está matrícula com o código: {self._matricula} e continua estudando normalmente")

#classe filha 2 - professor
class professor(pessoa):
    def __init__(self, nome,idade, disciplina):
        super().__init__(nome, idade)
        self._disciplina = disciplina   

    def ensinar(self):
           class Professor(Pessoa):
            def __init__(self._nome, idade, disciplina):
        super().__init__(nome,idade)
        self._disciplina = disciplina 

        def ensinar(self):
print(f"{self._nome} professor(a) da disciplina {self._disciplina}, está ensinando")