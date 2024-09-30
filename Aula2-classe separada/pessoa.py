class Pessoa
    #Método Construtor 
    def __init__(self,nome, hobby, endereco):
        self.nome = nome
        self.hobby = hobby 
        self.endereco = endereco 


        #Criando Métodos 
        daf exibirHobby(self): 
        print(f"Olá, meu hobby atual é {self.hobby}")

        def mudarhobby(self, novoHobby):
            self.hobby = novoHobby 
            print(f"Meu hobby foi mudado para {novoHobby}")
