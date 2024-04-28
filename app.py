from flask import Flask, render_template, request, redirect, url_for, render_template_string  # type: ignore
import sqlite3 as sql


app = Flask(__name__, static_url_path='/static', template_folder='templates')


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

@app.route("/Scrum Master")
def scrum_master():
    return render_template("Scrum-Master.html")


@app.route("/Games interativos")
def games_interativos():
    return render_template("Games-interativos.html")


@app.route("/Quiz de conhecimento")
def quiz_conhecimentos():
    return render_template("Quiz-de-conhecimento.html")

@app.route("/Capitulo1")
def capitulo1():
    return render_template("Modulo-1/Capitulos/Capitulo-1/Capitulo1.html")

@app.route("/Pilares Scrum")
def pilares_scrum():
    return render_template("Modulo-1/Capitulos/Capitulo-1/Pilares-Scrum.html")


@app.route("/Capitulo2")
def capitulo2():
    return render_template("Modulo-1/Capitulos/Capitulo-2/Capitulo2.html")

@app.route("/Time Scrum")
def time_scrum():
    return render_template("Modulo-1/Capitulos/Capitulo-2/Time-Scrum.html")

@app.route("/submit_quiz", methods=['POST'])
def test_quiz():
    if request.method == 'POST':
        # Conectar ao banco de dados SQLite
        conn = sql.connect('database/Questions.db')
        cur = conn.cursor()

        # Inicializar contagem de respostas corretas
        correct_answers = 0

        # Verificar cada resposta
        for i in range(1, 4):  # Assumindo que há 3 perguntas
            user_answer = request.form.get(f'Alt-question-{i}')
            correct_answer = cur.execute(f"SELECT resposta FROM Perguntas_Capitulo1 WHERE Numero = ?", (i,)).fetchone()[0]

            if user_answer == correct_answer:
                correct_answers += 1

        # Fechar a conexão com o banco de dados
        conn.close()

        # Renderizar o template com o número de respostas corretas
        return render_template("Modulo-1/Capitulos/Capitulo-1/Pilares-Scrum.html", score=correct_answers)
if __name__ == "__main__":
    app.run(debug = True)