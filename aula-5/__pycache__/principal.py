from biblioteca import Biblioteca, Livro, Revista

# Criando objetos
biblioteca1 = Livro("A Culpa é das Estrelas", "John Green", 2012, 255)
livro1 = Livro("É assim que acaba", " Colleen Hoover", 2016, 368)
revista1 = Revista("Revista Veja", "Diversos", 1997, 120)

biblioteca1.detalhes()
biblioteca1.calcularIdadeItem()

livro1.detalhes()
livro1.calcularIdadeItem()
livro1.verificarTamanho()

revista1.detalhes()
revista1.calcularIdadeItem()
revista1.verificarEdicao()

