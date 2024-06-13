show databases;
create database CDB_Database;
use CDB_Database;

/*Criação das tabelas de perguntas, quiz final e comentário*/
create table Perguntas_Capitulo1(
	Numero int auto_increment primary key,
    Questao varchar(250) not null,
    Resposta varchar(250) not null
);

create table Perguntas_Capitulo2(
	Numero int auto_increment primary key,
    Questao varchar(250) not null,
    Resposta varchar(250) not null
);

create table Perguntas_Capitulo3(
	Numero int auto_increment primary key,
    Questao varchar(250) not null,
    Resposta varchar(250) not null
);


create table Perguntas_Exame_Final(
	Numero int auto_increment primary key,
    Questao LONGTEXT not null,
    Resposta LONGTEXT not null
);

create table Comentarios(
	id int auto_increment primary key,
    Nome varchar(250) not null,
    RA BIGINT not null,
    Comentario varchar(500) not null
);

/*Linha de código para excluir uma tabela*/
DROP table Comentarios;

/*Inserção de perguntas do capítulo 1*/
INSERT INTO Perguntas_Capitulo1 (Questao, Resposta) 
VALUES 
('Defina o Scrum:', 'Alternativa B'),
('Os valores do Scrum são:', 'Alternativa C'),
('O Scrum se baseia em 3 pilares, sendo eles:', 'Alternativa A');

/*INserção de perguntas do capítulo 2*/
INSERT INTO Perguntas_Capitulo2 (Questao, Resposta) 
VALUES 
('Qual é a função do Product Owner em um projeto ágil?', 'Alternativa D'),
('Qual das seguintes definições corresponde a um dos estágios de um time auto-organizado?', 'Alternativa A'),
('Qual a responsabilidade do Facilitador?', 'Alternativa D');


/*Inserção de perguntas do capítulo 3*/
INSERT INTO Perguntas_Capitulo3 (Questao, Resposta) 
VALUES 
('Verdadeiro ou Falso. Sprint podem ser definidas como:', 'Alternativa A'),
('A respeito do Sprint Backlog:', 'Alternativa D'),
('Qual a função do Burndown Chart?', 'Alternativa B');


/*Inserção de perguntas do exame final*/
INSERT INTO 
Perguntas_Exame_Final (Questao, Resposta)
VALUES 
('O que são as cerimônias e porque são importantes?', 'Alternativa B'),
('O que se pode fazer com relação às estimativas quando se usa a metodologia ágil e o método Scrum?','Alternativa A'),
('A respeito de uma equipe que usa a filosofia ágil e a metodologia Scrum, o que se pode afirmar verdadeiramente:','Alternativa D'),
('Assinale a afirmação verdadeira a seguir:', 'Alternativa C'),
('A respeito da Sprint Planning Meeting, pode se afirmar o seguinte:', 'Alternativa B'),
('Qual o papel do Product Owner?', 'Alternativa A'),
('Qual é a definição de Scrum Master no Scrum?', 'Alternativa D'),
('Quais são as perguntas recorrentes do Daily Scrum?', 'Alternativa C'),
('Qual o formato de uma User Story?', 'Alternativa A'),
('Uma Release Planning Meeting é composta por:', 'Alternativa B'),
('Qual das seguintes alternativas descreve corretamente a essência de um processo empírico no contexto do Scrum?', 'Alternativa D'),
('Qual é a importância da transparência dentro do Scrum?', 'Alternativa B'),
('Como o Product Owner garante que o desenvolvimento do produto está alinhado com as necessidades do negócio?', 'Alternativa A'),
('Qual das seguintes opções descreve corretamente a importância dos três pilares do Scrum (Transparência, Inspeção e Adaptação)?', 'Alternativa B'),
('Qual é o principal objetivo de uma User Story no Scrum?', 'Alternativa C'),
('O Scrum master não pode comparecer a daily, e você irá assumir o papel temporariamente, para que o processo não seja quebrado! Qual é as perguntas que se deve fazer aos outros membros?', 'Alternativa A'),
('Dada a seguinte situação, escolha a alternativa INCORRETA: Durante a Sprint planning, todos os integrantes da equipe Scrum devem se reunir para organizar o que entregar e como produzir essa entrega de valor, respeitando o tempo da Sprint. Abaixo, estão listadas algumas dos passos para uma boa Sprint planning, escolha a alternativa INCORRETA:', 'Alternativa C');


SELECT * from Perguntas_Capitulo1;
SELECT * from Perguntas_Capitulo2;
SELECT * from Perguntas_Capitulo3;
SELECT * FROM Perguntas_Exame_Final;
SELECT * FROM Comentarios;

truncate Comentarios;

SHOW TABLES IN CDB_Database;