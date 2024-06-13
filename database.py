import sqlite3

#Criação do banco de dados
#Criar o banco de dados e do objeto conexão

conexao = sqlite3.connect("database/Questions.db")

#Criar um objeto cursor (é o objeto que consegue iterar pelos itens do banco de dados)
cursor = conexao.cursor()

#Criação de uma tabela (apenas é executado uma vez)
cursor.execute("CREATE TABLE Perguntas_Capitulo1(Numero, questao, resposta)")

#Criação de uma tabela (apenas é executado uma vez)
cursor.execute("CREATE TABLE Perguntas_Capitulo2(Numero, questao, resposta)")

#Criação de uma tabela (apenas é executado uma vez)
cursor.execute("CREATE TABLE Perguntas_Capitulo3(Numero, questao, resposta)")

#Criação de uma tabela (apenas é executado uma vez)
cursor.execute("CREATE TABLE Perguntas_final(Numero, questao, resposta)")

#Verificar agora se a tabela foi crawdad
resultado = cursor.execute("SELECT name FROM sqlite_master")
resultado.fetchone()

perguntas_Cap_1 = [(1, 'Defina o Scrum:', 'Alternativa B'),
                   (2, 'Os valores do Scrum são:', 'Alternativa C'),
                   (3, 'O Scrum se baseia em 3 pilares, sendo eles:', 'Alternativa A'),]


perguntas_Cap_2 = [(1, 'Qual é a função do Product Owner em um projeto ágil?', 'Alternativa D'),
                   (2, 'Qual das seguintes definições corresponde a um dos estágios de um time auto-organizado?', 'Alternativa A'),
                   (3, 'Qual a responsabilidade do Facilitador?', 'Alternativa D'),]

perguntas_Cap_3 = [(1, 'Verdadeiro ou Falso. Sprint podem ser definidas como:', 'Alternativa A'),
                   (2, 'A respeito do Sprint Backlog:', 'Alternativa D'),
                   (3, 'Qual a função do Burndown Chart?', 'Alternativa B'),]


perguntas_Cap_final = [(1, 'O que são as cerimônias e porque são importantes?', 'Alternativa B'),
                       (2, 'O que se pode fazer com relação às estimativas quando se usa a metodologia ágil e o método Scrum?','Alternativa A'),
                       (3, 'A respeito de uma equipe que usa a filosofia ágil e a metodologia Scrum, o que se pode afirmar verdadeiramente:','Alternativa D'),
                       (4, 'Assinale a afirmação verdadeira a seguir:', 'Alternativa C'),
                       (5, 'A respeito da Sprint Planning Meeting, pode se afirmar o seguinte:', 'Alternativa B'),
                       (6, 'Qual o papel do Product Owner?', 'Alternativa A'),
                       (7, 'Qual é a definição de Scrum Master no Scrum?', 'Alternativa D'),
                       (8, 'Quais são as perguntas recorrentes do Daily Scrum?', 'Alternativa C'),
                       (9, 'Qual o formato de uma User Story?', 'Alternativa A'),
                       (10, 'Uma Release Planning Meeting é composta por:', 'Alternativa B'),
                       (11, 'Qual das seguintes alternativas descreve corretamente a essência de um processo empírico no contexto do Scrum?', 'Alternativa D'),
                       (12, 'Qual é a importância da transparência dentro do Scrum?', 'Alternativa B'),
                       (13, 'Como o Product Owner garante que o desenvolvimento do produto está alinhado com as necessidades do negócio?', 'Alternativa A'),
                       (14, 'Qual das seguintes opções descreve corretamente a importância dos três pilares do Scrum (Transparência, Inspeção e Adaptação)?', 'Alternativa B'),
                       (15, 'Qual é o principal objetivo de uma User Story no Scrum?', 'Alternativa C'),
                       (16, 'O Scrum master não pode comparecer a daily, e você irá assumir o papel temporariamente, para que o processo não seja quebrado! Qual é as perguntas que se deve fazer aos outros membros?', 'Alternativa A'),
                       (17, 'Dada a seguinte situação, escolha a alternativa INCORRETA: Durante a Sprint planning, todos os integrantes da equipe Scrum devem se reunir para organizar o que entregar e como produzir essa entrega de valor, respeitando o tempo da Sprint. Abaixo, estão listadas algumas dos passos para uma boa Sprint planning, escolha a alternativa INCORRETA:', 'Alternativa C')]

#Inserir linhas na tabela
cursor.executemany("INSERT INTO Perguntas_Capitulo1 (Numero, questao, resposta) VALUES(?, ?, ?)", perguntas_Cap_1)

#Inserir linhas na tabela
cursor.executemany("INSERT INTO Perguntas_Capitulo2 (Numero, questao, resposta) VALUES(?, ?, ?)", perguntas_Cap_2)

#Inserir linhas na tabela
cursor.executemany("INSERT INTO Perguntas_Capitulo3 (Numero, questao, resposta) VALUES(?, ?, ?)", perguntas_Cap_3)


#Inserir linhas na tabela
cursor.executemany("INSERT INTO Perguntas_final (Numero, questao, resposta) VALUES(?, ?, ?)", perguntas_Cap_final)



#Precisa commitar toda alteração na tabela
conexao.commit()


resultado_cap_1 = cursor.execute("SELECT questao FROM Perguntas_Capitulo1")
resultado_cap_1.fetchall()

resultado_cap_2 = cursor.execute("SELECT questao FROM Perguntas_Capitulo2")
resultado_cap_2.fetchall()

resultado_cap_3 = cursor.execute("SELECT questao FROM Perguntas_Capitulo3")
resultado_cap_3.fetchall()


resultado_para_perguntas_final = cursor.execute("SELECT questao FROM Perguntas_final")
resultado_para_perguntas_final.fetchall()
#fechar conexão
conexao.close()