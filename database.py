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

perguntas_Cap_1 = [(1, 'Defina o Scrum:', 'Framework com o qual as pessoas resolvem problemas complexos e adaptáveis, enquanto entregam produtos de forma produtiva e criativa.'),
                   (2, 'Os valores do Scrum são:', 'II, III e V estão corretas.'),
                   (3, 'O Scrum se baseia em 3 pilares, sendo eles:', 'Transparência, Inspeção, Adaptação.'),]


perguntas_Cap_2 = [(1, 'Qual é a função do Product Owner em um projeto ágil?', 'O Product Owner atua como uma ponte entre o cliente e o development team, apresentando as tarefas da sprint com base nos requisitos do cliente e validando o trabalho desenvolvido após sua conclusão.'),
                   (2, 'Qual das seguintes definições corresponde a um dos estágios de um time auto-organizado?', 'Performing: É o estágio em que o time começa a operar de forma coordenada e com um desempenho satisfatório.'),
                   (3, 'Qual a responsabilidade do Facilitador?', 'Otimizar processos, evitar que o grupo tome decisões erradas, reduzir conflitos e motivá-los.'),]

perguntas_Cap_3 = [(1, 'Verdadeiro ou Falso. Sprint podem ser definidas como:', 'I e III estão corretas.'),
                   (2, 'A respeito do Sprint Backlog:', 'É o quadro onde terão as tarefas e subtarefas a serem desenvolvidas pelo Scrum Team, juntamente com uma ordem de prioridade, estimativa de conclusão e descrição.'),
                   (3, 'Qual a função do Burndown Chart?', 'Tornar visível a evolução diária do trabalho do time, mostrando a comparação entre o trabalho estimado com a quantidade de esforço.'),]


perguntas_Cap_final = [(1, 'O que são as cerimônias e porque são importantes?', 'As cerimônias são eventos específicos e esperados, são importantes porque ajudam a compreender a linha do tempo geral'),
                       (2, 'O que se pode fazer com relação às estimativas quando se usa a metodologia ágil e o método Scrum?','Estimativas são sempre importantes, mas não podem ser estáticas, ser ágil significa adaptabilidade constante e encontrar novas formas de lidar com problemas complexos'),
                       (3, 'A respeito de uma equipe que usa a filosofia ágil e a metodologia Scrum, o que se pode afirmar verdadeiramente:','Os papéis são estáveis, mas não são fixos, e à medida que os processos se desenvolvem, pessoas podem assumir novas funções, todos devem opinar e decidir, não há hierarquias'),
                       (4, 'Assinale a afirmação verdadeira a seguir:', 'A melhor forma de começar uma Sprint Planning Meeting é apresentando a Visão do Produto'),
                       (5, 'A respeito da Sprint Planning Meeting, pode se afirmar o seguinte:', 'É a primeira cerimônia Scrum, onde todos os detalhes precisam ser minuciosamente pensados'),
                       (6, 'Qual o papel do Product Owner?', 'Gerenciar o Backlog, garantir o ROI, definir a visão do produto, gerenciar a entrada de requisitos e definir prioridades'),
                       (7, 'Qual é a definição de Scrum Master no Scrum?', 'O Scrum Master é um facilitador, que ajuda a equipe a entender e adotar o Scrum, removendo impedimentos e promovendo um ambiente de trabalho colaborativo'),
                       (8, 'Quais são as perguntas recorrentes do Daily Scrum?', 'O que fiz desde a última Daily? O que pretendo fazer até a próxima? Existe algum impedimento?'),
                       (9, 'Qual o formato de uma User Story?', 'Como &lt tipo de usuário &gt quero &lt funcionalidade desejada &gt para quem/o/a  &lt usuário final &gt'),
                       (10, 'Uma Release Planning Meeting é composta por:', 'Abertura - Visão do Produto - Status do Projeto - Tema - Estimativa - Mapear Itens - Plano de Riscos - Plano de Comunicação e Logística  - Gráficos - Retrospectiva'),
                       (11, 'Qual das seguintes alternativas descreve corretamente a essência de um processo empírico no contexto do Scrum?', 'Um processo que adapta e melhora continuamente através da prática e experiência, enfrentando imprevistos'),
                       (12, 'Qual é a importância da transparência dentro do Scrum?', 'Assegurar que todos os membros da equipe compreendam claramente os processos e estejam alinhados nos termos utilizados'),
                       (13, 'Como o Product Owner garante que o desenvolvimento do produto está alinhado com as necessidades do negócio?', 'Definindo, priorizando e aceitando o trabalho a ser realizado pela equipe de desenvolvimento com base nas expectativas dos stakeholders'),
                       (14, 'Qual das seguintes opções descreve corretamente a importância dos três pilares do Scrum (Transparência, Inspeção e Adaptação)?', 'Eles proporcionam um ambiente onde o progresso pode ser monitorado continuamente e ajustes podem ser feitos com base em feedback constante'),
                       (15, 'Qual é o principal objetivo de uma User Story no Scrum?', 'Descrever uma funcionalidade desejada de forma que tenha valor para o usuário, focando no ponto de vista do cliente'),
                       (16, 'O Scrum master não pode comparecer a daily, e você irá assumir o papel temporariamente, para que o processo não seja quebrado! Qual é as perguntas que se deve fazer aos outros membros?', 'O que fiz desde a última Daily? O que pretendo fazer até a próxima? Existe algum impedimento?'),
                       (17, 'Dada a seguinte situação, escolha a alternativa INCORRETA: Durante a Sprint planning, todos os integrantes da equipe Scrum devem se reunir para organizar o que entregar e como produzir essa entrega de valor, respeitando o tempo da Sprint. Abaixo, estão listadas algumas dos passos para uma boa Sprint planning, escolha a alternativa INCORRETA:', 'Analizar a Sprint anterior (caso tenha) buscando melhorar e culpar os membros que atrasaram entregas')]

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