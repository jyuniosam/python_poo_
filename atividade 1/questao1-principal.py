from livro import Livro

# Criando dois objetos da classe Livro
livro1 = Livro("Crepúsculo", "Stephenie Meyer", 2005)
livro2 = Livro("Harry Potter e a Pedra Filosofal", "J.K. Rowling", 1997)

# Chamando os métodos para o primeiro livro
print("Informações do Livro 1:")
livro1.exibirinformacoes()
livro1.verificaridadeLivro()

print("\nInformações do Livro 2:")
# Chamando os métodos para o segundo livro
livro2.exibirinformacoes()
livro2.verificaridadeLivro()