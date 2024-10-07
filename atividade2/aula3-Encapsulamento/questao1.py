from academia import Aluno

def main():
    # Criando dois objetos da classe Aluno
    aluno1 = Aluno("Samuell Junior", 18, 79, 1.94)
    aluno2 = Aluno("Thavyla Sãmily", 17, 63, 1.55)

    # Chamando os métodos para o primeiro aluno
    print("Dados do Aluno 1:")
    aluno1.exibirDados()
    print(f"IMC: {aluno1.calcularIMC():.2f}\n")

    # Chamando os métodos para o segundo aluno
    print("Dados do Aluno 2:")
    aluno2.exibirDados()
    print(f"IMC: {aluno2.calcularIMC():.2f}")

{}