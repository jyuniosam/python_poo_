from conta import 
minhaConta = Conta(321, "Epamenondas Soares", 2000)
minhaConta.relatorio()

minhaConta.setlimite(8000)
minhaConta.relatorio()

print(f"o seu limite atual é {minhaConta.getLimite()}")



minhaConta.depositar(200)
minhaConta.relatorio()

minhaConta.sacar(150)
minhaConta.relatorio()