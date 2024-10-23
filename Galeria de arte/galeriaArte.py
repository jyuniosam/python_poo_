import sqlite3

# Aqui estamos criando a classe que será utilizada no gerenciamento da galeria
class ObraDeArte:
    def conexao(self): # Essa função inicia a conexão com o Banco de Dados
        conexao = sqlite3.connect('galeria.db')
        consulta = conexao.cursor() # Com esses comandos, estamos iniciando o Banco de Dados
        tabela = '''
        CREATE TABLE IF NOT EXISTS obras(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        titulo VARCHAR(100),
        artista VARCHAR(100),
        preco FLOAT,
        descricao VARCHAR(100)
        );
        ''' # Aqui estamos criando a tabela e informando seus atributos
        consulta.execute(tabela) # O sistema está executando os comandos informados pelo código
        return conexao

    def cadastrarObra(self, titulo, artista, preco, descricao):
        conexao = self.conexao() # Esse comando indica que o Banco vai ser usado, portanto é obrigatório em todos os métodos (Def)

        sql = 'INSERT INTO obras VALUES (?,?,?,?,?)' # Indica o comando que vamos executar na tabela (Obras)

        campos = (None, titulo, artista, preco, descricao) # Indica os atributos de cadastro da obra 

        consulta = conexao.cursor() 
        consulta.execute(sql, campos) # O sistema está executando os comandos informados pelo código

        conexao.commit()
        print("-"  * 50)
        print('Cadastro realizado com sucesso!')

        conexao.close() # Encerrando a conexão com o Banco de Dados

    def consultarObras(self):
        conexao = self.conexao() # Esse comando indica que o Banco vai ser usado, portanto é obrigatório em todos os métodos (Def)
        consulta = conexao.cursor()

        sql = 'SELECT * FROM obras' # Indica o comando que vamos executar na tabela (Obras)
        consulta.execute(sql) # O sistema está executando os comandos informados pelo código

        resultado = consulta.fetchall() # O comando fetchall() indica que você está consultando os itens da tabela 'Obras'

        for itens in resultado: # Estrutura FOR que deve exibir todos os itens presentes nas linhas da tabela  
            if resultado == 0: # Se nenhuma obra for encontrada, o código retornará essa mensagem
                print('Nenhuma obra cadastrada')
            else: #Exibindo as obras com os seus atributos separadamente
                print(f'ID: {itens[0]}',end=' | ')
                print(f'Título da Obra: {itens[1]}',end=' | ')
                print(f'Artista: {itens[2]}',end=' | ')
                print(f'Preço: {itens[3]}',end=' | ')
                print(f'Descrição: {itens[4]}')
    
    def deletarObra(self, id):
        conexao = self.conexao() # Esse comando indica que o Banco vai ser usado, portanto é obrigatório em todos os métodos (Def)
        consulta = conexao.cursor()


        sql = 'DELETE FROM obras WHERE id = ?' # Indica o comando que vamos executar na tabela (Obras)
        campos = (id,) # sinifica que vamos usar o campo 'ID' para deletar alguma obra da tabela
        consulta.execute(sql, campos) # O sistema está executando os comandos informados pelo código

        conexao.commit()

        print(consulta.rowcount, ' obra deletada.')

        conexao.close() # Encerrando a conexão com o Banco de Dados
    
    def atualizarObra(self, preco, id): # Função que atualizará os dados da obra 
        conexao = self.conexao()  # Esse comando indica que o Banco vai ser usado, portanto é obrigatório em todos os métodos (Def)
        consulta = conexao.cursor()

        sql = 'UPDATE obras SET preco = ? WHERE id = ?' # Indica o comando que vamos executar na tabela (Obras)

        campos = (preco, id)

        consulta.execute(sql, campos) # O sistema está executando os comandos informados pelo código

        conexao.commit()

        print(consulta.rowcount, ' linha(s) atualizada(s) com sucesso')

        conexao.close() # Encerrando a conexão com o Banco de Dados

    
    def consultarObraIndividual(self, id): # Função que consulta cada obra de forma individual
        conexao = self.conexao()  # Esse comando indica que o Banco vai ser usado, portanto é obrigatório em todos os métodos (Def)
        consulta = conexao.cursor()
        
        sql = 'SELECT * FROM obras WHERE id = ?' # Indica o comando que vamos executar na tabela (Obras)
        campos = (id,) # sinifica que vamos usar o campo 'ID' para consultar a tabela
        consulta.execute(sql, campos) # O sistema está executando os comandos informados pelo código

        resultados = consulta.fetchall() # O comando fetchall() indica que você está consultando os itens da tabela 'Obras'

        if resultados: # O comando "if resultados" quer dizer que se houver algum resultado encontrado, o sistema irá exibir os dados encontrados 
            for item in resultados: #Exibindo os dados de apenas uma obra
                print(f'ID: {item[0]}')
                print(f'Título da obra: {item[1]}')
                print(f'Artista: {item[2]}')
                print(f'Preço: {item[3]}')
                print(f'Descrição: {item[4]}')

        else:
            print('Consulta inválida, o ID não existe')