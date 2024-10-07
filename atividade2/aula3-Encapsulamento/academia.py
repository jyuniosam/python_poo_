class Conta:
    def __init__(self, numero, titular, saldo,limite):
       #Quando colocamos 2 underlines antes do atributo, indicamos que esse atributo está com a visibilidade "privado", o ocntrário significa que está público
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

        def relatorio(self):
            print(f"Olá (self.titular) seu saldo é {self.__saldo} e o seu limite atual é {self.__limite}")
        def getLimite(self):
            return self.__limite 

        def depositar(self, valor):
            if valor < 0:
                print("Informe um valor válido")
            else:
                     self.__saldo = self_saldo + valor 

        def sacar(self, valor):
            if valor <= 0 or valor > self.__saldo:
                print("Saldo insuficiente ou valor negativo solicitando")
            else:
                    self.__saldo -= valor
                    