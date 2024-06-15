from flask import Flask, jsonify, render_template, request, redirect, url_for, render_template_string, send_file # type: ignore
from flask_mysqldb import MySQL
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A3
import io 


app = Flask(__name__, static_url_path='/static', template_folder='templates')

# Configurações do MySQL
app.config['MYSQL_USER'] = 'root'
# app.config['MYSQL_PASSWORD'] = '2#J5E8@s*8$WgokH'
app.config['MYSQL_PASSWORD'] = 'admin'
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_DB'] = 'CDB_Database'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'


mysql = MySQL(app)


@app.route('/generate-pdf')
def generate_pdf():
    buffer = io.BytesIO()
    
    # Configurações do pdf certificado
    cnv = canvas.Canvas(buffer, pagesize=A3)
    cnv.drawImage("static/img/cont/CertificadoCDB.png", 0, 0,  width= 850, height=1200)
    cnv.save()

    buffer.seek(0)

    return send_file(buffer, as_attachment=True, download_name='Certificado.pdf', mimetype='application/pdf')

@app.route("/")
def homepage():
    return render_template("index.html")


@app.route("/scrumintroducion")
def scrum_introduction():
    return render_template("scrumintroducion.html")


@app.route("/trilha")
def trilha():
    return render_template("trilha.html")


@app.route("/sobre")
def sobre():
    return render_template("sobre.html")


@app.route("/jogo")
def jogo():
    return render_template("jogo.html")


@app.route("/exame")
def exame():
    return render_template("examefinal.html")


@app.route("/Capitulo1")
def capitulo1():
    return render_template("Modulo-1/Capitulos/Capitulo-1/Capitulo1.html")

@app.route("/Fundamentos")
def fundamentos():
    return render_template("Modulo-1/Capitulos/Capitulo-1/FundamentosScrum.html")

@app.route("/Valores")
def valores():
    return render_template("Modulo-1/Capitulos/Capitulo-1/ValoresScrum.html")

@app.route("/Pilares Scrum")
def pilares_scrum():
    return render_template("Modulo-1/Capitulos/Capitulo-1/Pilares-Scrum.html")


@app.route("/Capitulo2")
def capitulo2():
    return render_template("Modulo-1/Capitulos/Capitulo-2/Capitulo2.html")


@app.route("/Time Scrum")
def time_scrum():
    return render_template("Modulo-1/Capitulos/Capitulo-2/Time-Scrum.html")

@app.route("/Skills")
def skills():
    return render_template("Modulo-1/Capitulos/Capitulo-2/Skills.html")

@app.route("/Conceitos")
def conceitos():
    return render_template("Modulo-1/Capitulos/Capitulo-2/Conceitos.html")

# << << << < HEAD


@app.route("/Capitulo3")
def capitulo3():
    return render_template("Modulo-1/Capitulos/Capitulo-3/Capitulo3.html")

@app.route("/Eventos")
def eventos():
    return render_template("Modulo-1/Capitulos/Capitulo-3/Eventos.html")

@app.route("/Artefatos")
def artefatos():
    return render_template("Modulo-1/Capitulos/Capitulo-3/Artefatos.html")

@app.route('/CerimoniasPT-1')
def cerimonias1():
    return render_template('Modulo-1/Capitulos/Capitulo-3/Cerimonias-pt1.html')

@app.route('/CerimoniasPT-2')
def cerimonias2():
    return render_template('Modulo-1/Capitulos/Capitulo-3/Cerimonias-pt2.html')

@app.route("/Burndown")
def burndown():
    return render_template("Modulo-1/Capitulos/Capitulo-3/Burndown.html")

@app.route("/DoR_DoD")
def DoR_DoD():
    return render_template("Modulo-1/Capitulos/Capitulo-3/DoR_DoD.html")

@app.route("/Estimativas")
def estimativa():
    return render_template("Modulo-1/Capitulos/Capitulo-3/Estimativas.html")



@app.route("/jogoPO")
def jogoPO():
    return render_template("Modulo-2/jogoPO.html")

@app.route("/jogoBacklog")
def jogoBacklog():
    return render_template("Modulo-2/jogoBacklog.html")

@app.route('/jogoSM')
def jogoSM():
    return render_template('Modulo-2/jogoSM.html')

@app.route("/jogoST")
def jogoST():
    return render_template("Modulo-2/jogoST.html")

@app.route("/Exame final")
def examefinal():
    return render_template("/Modulo-3/examefinal.html")

@app.route("/comentario")
def comentario():
    return render_template("/Modulo-3/comentario.html")

# @app.route("/adm")
# def adm():
#     return render_template("/adm.html")

# == == == =


#Verificando se as respostas do quizz 1 estão certas usando o MySQL
@app.route("/submit_quiz_cap_1", methods=["POST"])
def submit():
    if request.method == 'POST':
        # Conectar ao banco de dados
        conn = mysql.connection
        cursor = conn.cursor()

      # Inicializar contagem de respostas corretas
        correct_answers = 0
             
    # Verificar cada resposta
    for i in range(1, 4):  # Assumindo que há 3 perguntas
       user_answer = request.form.get(f'Alt-question-{i}')
       cursor.execute(f"SELECT Resposta FROM Perguntas_Capitulo1 WHERE Numero = %s", (i,))
       correct_answer = cursor.fetchone()['Resposta']

       if user_answer == correct_answer:
           correct_answers += 1

    # Renderizar o template com o número de respostas corretas
    return render_template("Modulo-1/Capitulos/Capitulo-1/Pilares-Scrum.html", score=correct_answers)

#=========================================================================================================


#Verificando se as respostas do quizz 2 estão certas usando o MySQL
@app.route("/submit_quiz_cap_2", methods=['POST'])
def quiz_capitulo_2():
    if request.method == 'POST':
        # Conectar ao banco de dados SQLite
        conn = mysql.connection
        cursor = conn.cursor()



      # Inicializar contagem de respostas corretas
        correct_answers = 0

# Verificar cada resposta
    for i in range(1, 4):  # Assumindo que há 3 perguntas
       user_answer = request.form.get(f'Alt-question-{i}')
       cursor.execute(f"SELECT Resposta FROM Perguntas_Capitulo2 WHERE Numero = %s", (i,))
       correct_answer = cursor.fetchone()['Resposta']

       if user_answer == correct_answer:
           correct_answers += 1

    # Renderizar o template com o número de respostas corretas
    return render_template("Modulo-1/Capitulos/Capitulo-2/Conceitos.html", score_cap2=correct_answers)

#=========================================================================================================

#Verificando se as respostas do quizz 3 estão certas usando o MySQL
@app.route("/submit_quiz_cap_3", methods=['POST'])
def quiz_capitulo_3():
    if request.method == 'POST':
        # Conectar ao banco de dados SQLite
        conn = mysql.connection
        cursor = conn.cursor()



      # Inicializar contagem de respostas corretas
        correct_answers = 0

# Verificar cada resposta
    for i in range(1, 4):  # Assumindo que há 3 perguntas
       user_answer = request.form.get(f'Alt-question-{i}')
       cursor.execute(f"SELECT Resposta FROM Perguntas_Capitulo3 WHERE Numero = %s", (i,))
       correct_answer = cursor.fetchone()['Resposta']

       if user_answer == correct_answer:
           correct_answers += 1

    # Renderizar o template com o número de respostas corretas
    return render_template("Modulo-1/Capitulos/Capitulo-3/Estimativas.html", score_cap3=correct_answers)

#=========================================================================================================

#Verificando se as respostas do quizz final estão certas usando o MySQL
correct_answers = 0

@app.route("/submit_quiz_final", methods=['POST'])
def test_quiz_final():
    global correct_answers
    if request.method == 'POST':
        # Conectar ao banco de dados SQLite
        conn = mysql.connection
        cursor = conn.cursor()



      # Inicializar contagem de respostas corretas
        correct_answers = 0

# Verificar cada resposta
    for k in range(1, 21):  # Assumindo que há 20 perguntas
       user_answer = request.form.get(f'Alt-question-{k}')
       correct_answer = cursor.execute(f"SELECT Resposta FROM Perguntas_Exame_Final WHERE Numero = %s", (k,))
       correct_answer = cursor.fetchone()['Resposta']

       if user_answer == correct_answer:
           correct_answers += 1

    # Renderizar o template com o número de respostas corretas
    return render_template("Modulo-3/comentario.html", score_final=correct_answers)


#=========================================================================================================
#Inserindo comentários no banco de dados
@app.route("/submit_comentarios", methods=["POST"])
def comentarios():
    # Obter dados do formulário
    Nome = request.form['Nome']
    RA = request.form['RA']
    Comentario = request.form['Comentario']

    # Conectar ao banco de dados
    conn = mysql.connection
    cursor = conn.cursor()

    # Inserir dados no banco de dados
    query = "INSERT INTO Comentarios (Nome, RA, Nota, Comentario) VALUES (%s, %s, %s, %s)"
    cursor.execute(query, (Nome, RA, correct_answers, Comentario))
    conn.commit()

    # Fechar a conexão com o banco de dados
    cursor.close()

    return render_template("Modulo-3/comentario.html")
   
#Exibir lista de alunos (comentários)
@app.route('/adm')
def adm():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM Comentarios")
    Comentarios = cur.fetchall()
    cur.close()
    return render_template('adm.html', Comentarios=Comentarios)    


if __name__ == "__main__":
    app.run(debug= True)
