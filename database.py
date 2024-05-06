import sqlite3

#Criação do banco de dados
#Criar o banco de dados e do objeto conexão

conexao = sqlite3.connect("database/Questions.db")

#Criar um objeto cursor (é o objeto que consegue iterar pelos itens do banco de dados)
cursor = conexao.cursor()

#Criação de uma tabela (apenas é executado uma vez)
cursor.execute("CREATE TABLE Perguntas_Capitulo1(Numero, questao, resposta)")

#Criação de uma tabela (apenas é executado uma vez)
cursor.execute("CREATE TABLE Perguntas_final(Numero, questao, resposta)")

#Verificar agora se a tabela foi crawdad
resultado = cursor.execute("SELECT name FROM sqlite_master")
resultado.fetchone()

perguntas_Cap_1 = [(1, 'Defina o Scrum:', 'Framework com o qual as pessoas resolvem problemas complexos e adaptáveis, enquanto entregam produtos de forma produtiva e criativa.'),
                   (2, 'Os valores do Scrum são:', 'II, III e V estão corretas.'),
                   (3, 'O Scrum se baseia em 3 pilares, sendo eles:', 'Transparência, Inspeção, Adaptação.'),]

perguntas_Cap_final = [(1, 'O que são as cerimônias e porque são importantes?', 'As cerimônias são eventos específicos e esperados, são importantes porque ajudam a compreender a linha do tempo geral'),
                       (2, 'O que se pode fazer com relação às estimativas quando se usa a metodologia ágil e o método Scrum?','Estimativas são sempre importantes, mas não podem ser estáticas, ser ágil significa adaptabilidade constante e encontrar novas formas de lidar com problemas complexos'),
                       (3, 'A respeito de uma equipe que usa a filosofia ágil e a metodologia Scrum, o que se pode afirmar verdadeiramente:','Os papéis são estáveis, mas não são fixos, e à medida que os processos se desenvolvem, pessoas podem assumir novas funções, todos devem opinar e decidir, não há hierarquias'),
                       (4, 'Assinale a afirmação verdadeira a seguir:', 'A melhor forma de começar uma Sprint Planning Meeting é apresentando a Visão do Produto'),
                       (5, 'A respeito da Sprint Planning Meeting, pode se afirmar o seguinte:', 'É a primeira cerimônia Scrum, onde todos os detalhes precisam ser minuciosamente pensados'),
                       (6, 'Qual o papel do Product Owner?', 'Gerenciar o Backlog, garantir o ROI, definir a visão do produto, gerenciar a entrada de requisitos e definir prioridades'),
                       (7, 'Qual é a definição de Scrum Master no Scrum?', 'O Scrum Master é um facilitador, que ajuda a equipe a entender e adotar o Scrum, removendo impedimentos e promovendo um ambiente de trabalho colaborativo'),
                       (8, 'Quais são as perguntas recorrentes do Daily Scrum?', 'O que fiz desde a última Daily? O que pretendo fazer até a próxima? Existe algum impedimento?'),
                       (9, 'Qual o formato de uma User Story?', 'Como <tipo de usuário> quero <funcionalidade desejada> para <motivo que remeta um valor ao negócio>'),
                       (10, 'Uma Release Planning Meeting é composta por:', 'Abertura - Visão do Produto - Status do Projeto - Tema - Estimativa - Mapear Itens - Plano de Riscos - Plano de Comunicação e Logística  - Gráficos - Retrospectiva')]

#Inserir linhas na tabela
cursor.executemany("INSERT INTO Perguntas_Capitulo1 (Numero, questao, resposta) VALUES(?, ?, ?)", perguntas_Cap_1)

#Inserir linhas na tabela
cursor.executemany("INSERT INTO Perguntas_final (Numero, questao, resposta) VALUES(?, ?, ?)", perguntas_Cap_final)



#Precisa commitar toda alteração na tabela
conexao.commit()


resultado = cursor.execute("SELECT questao FROM Perguntas_Capitulo1")
resultado.fetchall()

resultado_para_perguntas_final = cursor.execute("SELECT questao FROM Perguntas_final")
resultado_para_perguntas_final.fetchall()
#fechar conexão
conexao.close()