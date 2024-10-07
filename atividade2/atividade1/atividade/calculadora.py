from calculadora import Calculadora

def main():
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))

    calc = Calculadora(num1, num2)

    calc.somar()
    calc.subtrair()
    calc.multiplicar()
    calc.dividir()
    calc.potencia()

    # Verificando se num1 é par ou ímpar
    print(calc.verificaParImpar(num1))
    # Verificando se num2 é par ou ímpar
    print(calc.verificaParImpar(num2))
    
