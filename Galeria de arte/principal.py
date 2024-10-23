from galeriaArte import ObraDeArte #importando a classe

# Nessa parte, estamos criando os objetos a serem utilizados na tabela
cadastrar = ObraDeArte()
consultar = ObraDeArte()
consultarInd = ObraDeArte()
deletar = ObraDeArte()
atualizar = ObraDeArte()


print('GALERIA DE ARTES')
# Colocando a programação para rodar em repetição, até que o usuário deseja sair do gerenciamento 
while True: # O comando while True indica que o código continuará se repetindo até que o sistema peça pra parar, com o 'break'
    print('.' * 50 )
    option = int(input('Opções:\n1. Cadastrar Obra\n2. Consultar todas as obras\n3. Consultar apenas uma obra\n4. Atualizar obra\n5. Apagar Obra\n6.Sair\n'))

    if option == 1: # Chamando a função de cadastro
        print('Informações da Obra', '-' * 30)
        
        titulo = input('Título da obra: ')
        artista = input('Nome do artista: ')
        preco = float(input('Preço: R$'))
        descricao = input('Descrição da obra: ')

        cadastrar.cadastrarObra(titulo, artista, preco, descricao) # Utilizando o objeto para chamar o método, os parâmetros que estão dentro são os solicitados pelo método, que precisam ser preenchidos obrigatoriamente

    elif option == 2: # Chamando a função que irá mostrar todas as obras
        print('------------------- Obras --------------------')
        consultar.consultarObras()

    elif option == 3: # Consultar apenas uma obra
        id = int(input('Informe o id da Obra: '))
        print('-' * 20)
        print('DADOS DA OBRA:')
        consultarInd.consultarObraIndividual(id)

    elif option == 4: # Atualizar algum dado da obra, no caso seu preço
        id = int(input('Informe o ID da obra: '))
        preco = input('Informe o novo preço da obra: ')

        atualizar.atualizarObra(preco, id) # Utilizando o objeto para chamar o método, os parâmetros que estão dentro são os solicitados pelo método, que precisam ser preenchidos obrigatoriamente
    
    elif option == 5:
        id = int(input('Informe a sessão: '))
        print('-' * 20)
        print('DADOS DA SESSÃO')
        deletar.deletarObra(id) # Utilizando o objeto para chamar o método, os parâmetros que estão dentro são os solicitados pelo método, que precisam ser preenchidos obrigatoriamente


    elif option == 6:
        print('Obrigado por utilizar o gerenciamento')
        break # indica que o sistema irá parar de repetir
