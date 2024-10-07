class Aluno:
    def __init__(self, nome, idade, peso, altura):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura

    def exibirDados(self):
        print(f"Nome: {self.nome}")
        print(f"Idade: {self.idade}")
        print(f"Peso: {self.peso} kg")
        print(f"Altura: {self.altura} m")

    def calcularIMC(self):
        if self.altura > 0:
            imc = self.peso / (self.altura ** 2)
            return imc
        else:
            return "Altura inválida."
