class Personagem:
    def __init__(self, nome, rank, vida):
        self._nome = nome
        self._rank = rank
        self._vida = vida

    def receberDano(self, dano):
        dano = dano
        self._vida = self._vida - dano
        print(f"O personagem {self._nome} recebeu {dano} de dano e está com {self._vida} de vida")

    def verificarVida(self):
        if self._vida == 0:
            print(f"O personagem {self._nome} faleceu.")
        else:
            print(f"O personagem {self._nome} está vivo!")

    def detalhes(self):
        print(f"O personagem {self._nome} do rank {self._rank} está hordienamente com {self._vida} de vida.")
    
class Heroi(Personagem):
    def __init__(self, nome, rank, vida, identidadeSecreta, energia):
        super().__init__(nome, rank, vida)
        self._identidadeSecreta = identidadeSecreta
        self._energia = energia

    def executarHabilidade(self, tipoHabilidade):
        self._energia = self._energia - 5
        print(f"\nO herói {self._nome} usou o poder {tipoHabilidade} o que consumiu 20 de energia e hordienamente está com {self._energia}")

    def recarregarEnergia(self):
        self._energia = self._energia + 16
        print(f"O héroi {self._nome} recuperou 16 de energia, ficando agora com {self._energia}")

    def chamarAliado(self, nomeAliado, poderAliado):
        print(f"O herói {self._nome} levou para a batalha o colega {nomeAliado} para ajudá-lo e ele utilizou o {poderAliado}")


class Vilao(Personagem):
    def __init__(self, nome, rank, vida, malicia):
        super().__init__(nome, rank, vida)
        self._malicia = malicia

    def desferirGolpe(self, tipoGolpe):
        self._malicia = self._malicia - 13
        print(f"\nO vilão {self._nome} atacou utilizando seu poder {tipoGolpe} o que usou 40 pontos de malicia então o deixando com {self._malicia} de malicia")

    def planejarArmadilha(self, tipoArmadilha):
        print(f"Silenciosamente nos becos escuros da cidade o vilão {self._nome} vem planejando sua armailha perigosa chamada {tipoArmadilha}!")

    def fugir(self, tipoFuga):
        print(f"O vilão {self._nome} conseguiu fugir usando o {tipoFuga}!\n")