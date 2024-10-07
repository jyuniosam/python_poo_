# arquivo: celular.py
class Celular:
    def __init__(self, numero, plano="pré-pago", saldo=0):
        self.__numero = numero
        self.__plano = plano
        self.__saldo = saldo
        self.__valorMinuto = 1.50

    @property
    def plano(self):
        return self.__plano

    @plano.setter
    def plano(self, novo_plano):
        self.__plano = novo_plano

    def recarregar(self, valor):
        if self.__plano == "pré-pago":
            self.__saldo += valor

    def fazerChamada(self, duracao_minutos):
        custo = duracao_minutos * self.__valorMinuto
        if self.__plano == "pré-pago":
            if self.__saldo >= custo:
                self.__saldo -= custo
            else:
                print("Saldo insuficiente para realizar a chamada.")
        else:
            print(f"Chamada realizada. O valor de R${custo:.2f} será cobrado no final do mês.")

    def exibir_dados(self):
        print(f"Número: {self.__numero}, Plano: {self.__plano}, Saldo: R${self.__saldo:.2f}")

# arquivo: principalCelular.py
from celular import Celular

cliente1 = Celular("1234-5678", "pré-pago")
cliente2 = Celular("8765-4321", "pós-pago")

cliente1.recarregar(50)
cliente2.recarregar(30)

cliente1.fazerChamada(10)
cliente2.fazerChamada(5)

cliente1.exibir_dados()
cliente2.exibir_dados()
