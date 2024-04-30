import sqlite3

#Criação do banco de dados
#Criar o banco de dados e do objeto conexão

conexao = sqlite3.connect("database/Questions.db")

#Criar um objeto cursor (é o objeto que consegue iterar pelos itens do banco de dados)
cursor = conexao.cursor()

#Criação de uma tabela (apenas é executado uma vez)
cursor.execute("CREATE TABLE Perguntas_Capitulo1(Numero, questao, resposta)")


#Verificar agora se a tabela foi crawdad
resultado = cursor.execute("SELECT name FROM sqlite_master")
resultado.fetchone()

todas_perguntas = [(1, 'Defina o Scrum:', 'Framework com o qual as pessoas resolvem problemas complexos e adaptáveis, enquanto entregam produtos de forma produtiva e criativa.'),
                   (2, 'Os valores do Scrum são:', 'II, III e V estão corretas.'),
                   (3, 'O Scrum se baseia em 3 pilares, sendo eles:', 'Transparência, Inspeção, Adaptação.'),]

#Inserir linhas na tabela
cursor.executemany("INSERT INTO Perguntas_Capitulo1 (Numero, questao, resposta) VALUES(?, ?, ?)", todas_perguntas)

#Precisa commitar toda alteração na tabela
conexao.commit()


resultado = cursor.execute("SELECT questao FROM Perguntas_Capitulo1")
resultado.fetchall()
#fechar conexão
conexao.close()