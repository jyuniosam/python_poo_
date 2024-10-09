from heroievilao import Personagem, Heroi, Vilao

p1 = Personagem("ahri", "Lendário", 100)
h1 = Heroi("Wanda", "Avançado", 95, "Feiticeira escarlate", 33)
v1 = Vilao("Hella", "Lendária", 100, 80)

p1.receberDano(20)
p1.verificarVida()
p1.detalhes()

h1.executarHabilidade("Charme")
h1.recarregarEnergia()
h1.detalhes()
h1.chamarAliado("Magia don caos", "Manto das Sombras")

v1.desferirGolpe("Charme")
v1.detalhes()
v1.fugir("Camuflagem Sombria")
v1.planejarArmadilha("Charminho rosa") 