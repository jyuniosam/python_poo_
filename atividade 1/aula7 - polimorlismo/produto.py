class Produto:
    def __init__(self, nome, preco):
        self._nome = nome
        self._preco = preco

    def descrever(self):
        print(f"o produto {self._nome} custa R${self._preco}")

    def calcularDesconto(self, valor):
            print(f"o desconto não será fornecido por aqui") 

# Classe filha 1 - Eletronico
class Eletronico(Produto):
        def __init__(self, nome, preco, voltagem ):
            super().__init__(nome, preco)
            self._voltagem = voltagem 

        def descrever(self):
            print(f"o Eletrônico {self._nome} custa r${self._preco} e possuia voltagem {self._voltagem}")

        def calcularDesconto(self, valor):
            desconto = valor/100
            print(f"o produto eletrônico {self._nome} terá um desconto de {desconto}%")
            