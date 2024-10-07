class Biblioteca:
    def __init__(self, titulo, autor, anoPublicacao, numeroPagina):
        self._titulo = titulo
        self._autor = autor
        self._anoPublicacao = anoPublicacao
        self._numeroPagina = numeroPagina

    def detalhes(self):
        print(f"Título: {self._titulo}, Autor: {self._autor}, Ano de Publicação: {self._anoPublicacao}")
        
    def calcularIdadeItem(self):
        idade = (2024 - self._anoPublicacao)
        if idade > 70:
            print(f"O livro {self._titulo} de {self._anoPublicacao} com {idade} anos é um livro antigo\n")
        elif idade >= 30 and idade <= 70:
            print(f"O livro {self._titulo} de {self._anoPublicacao} com {idade} anos é um livro recente\n")
        elif idade < 30:
            print(f"O livro {self._titulo} de {self._anoPublicacao} com {idade} anos é um livro contemporâneo\n")


class Livro(Biblioteca):
    def verificarTamanho(self):
        tipo = "longo" if self._numeroPagina > 300 else "curto"
        print(f"{self._titulo} tem {self._numeroPagina} páginas e é um livro {tipo}.\n")

class Revista(Biblioteca):
    def verificarEdicao(self):
        edicao_especial = "edição especial" if self._anoPublicacao < 1998 else "não é uma edição especial"
        print(f"{self._titulo}, {self._anoPublicacao}: {edicao_especial}.")
