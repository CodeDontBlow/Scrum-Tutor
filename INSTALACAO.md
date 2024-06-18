## GUIA INSTALACAO

**1. Clonar o Repositório** 
Primeiro, clone o repositório para sua máquina local usando o comando abaixo:

```bash
git clone https://github.com/CodeDontBlow/Scrum-Tutor.git
```

**2. Criar e Ativar um Ambiente Virtual**
É recomendável usar um ambiente virtual para isolar as dependências do projeto. Você pode criar e ativar um ambiente virtual com os seguintes comandos:


```bash
python -m venv venv

# Windows ativar o ambiente
venv\Scripts\activate

# Linux ou Mac ativar o ambiente
source venv/bin/activate
```

**3. Instalar Dependências**
Com o ambiente virtual ativado, instale todas as dependências listadas no arquivo requirements.txt:

```bash
pip install -r requirements.txt
```


**4. Configurando o Banco de Dados MySQL**
   
   > Certifique-se de que o MySQL está instalado e em execução.
   
a. Crie o banco de dados e as tabelas usando o script SQL fornecido: 
```bash 
mysql -u root -p < database/CDB_Database.sql 
# ou 
sudo mysql < database/CDB_Database.sql
```
b. Configurando o arquivo de ambiente Copie o arquivo .env.template para .env:

```bash
cp .env.template .env
```
c. Inserindo as informações do banco de dados

Edite o arquivo .env e insira as informações de configuração do banco de dados MySQL:
```bash
MYSQL_HOST=localhost
MYSQL_USER=root
MYSQL_PASS=sua_senha_aqui
MYSQL_DB=scrumtutor
```
Certifique-se de substituir sua_senha_aqui pela senha correta do seu usuário MySQL.

**5. Execute o servidor Flask**

Inicie o servidor Flask para rodar o projeto localmente:
```bash
flask run
```

**6. Acesse o Projeto:** 

Abra seu navegador e acesse o projeto em: http://localhost:5000


**Com esses passos você já está pronto para iniciar o desenvolvimento do projeto.**
