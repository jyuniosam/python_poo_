class Calculadora:
    def __init__(self, num1, num2):
        self.__num1 = num1
        self.__num2 = num2

    def somar(self):
        resultado = self.__num1 + self.__num2
        print(f"A soma de {self.__num1} e {self.__num2} é: {resultado}")

    def subtrair(self):
        resultado = self.__num1 - self.__num2
        print(f"A subtração de {self.__num1} por {self.__num2} é: {resultado}")

    def multiplicar(self):
        resultado = self.__num1 * self.__num2
        print(f"A multiplicação de {self.__num1} e {self.__num2} é: {resultado}")

    def dividir(self):
        if self.__num2 == 0:
            print("Erro: Divisão por zero não é permitida.")
        else:
            resultado = self.__num1 / self.__num2
            print(f"A divisão de {self.__num1} por {self.__num2} é: {resultado}")

    def potencia(self):
        if self.__num1 <= 0 or self.__num2 < 0:
            print("Erro: O primeiro número deve ser maior que zero e o segundo não pode ser negativo.")
        else:
            resultado = self.__num1 ** self.__num2
            print(f"{self.__num1} elevado à {self.__num2} é: {resultado}")

    def verificaParImpar(self, valor):
        if valor % 2 == 0:
            return f"{valor} é par."
        else:
            return f"{valor} é ímpar."
