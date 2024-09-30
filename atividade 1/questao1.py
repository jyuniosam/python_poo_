class Livro:
    def __init__(self, titulo, autor, ano_publicacao):
        self.titulo = titulo
        self.autor = autor
        self.ano_publicacao = ano_publicacao

    def exibirinformacoes(self):
        print(f"Título: {self.titulo}")
        print(f"Autor: {self.autor}")
        print(f"Ano de Publicação: {self.ano_publicacao}")

    def verificaridadeLivro(self):
        ano_atual = 2024
        idade_livro = ano_atual - self.ano_publicacao
        
        if idade_livro > 50:
            print("Este livro é um clássico.")
        else:
            print("Ainda não é considerado um clássico.")


