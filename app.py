from flask import Flask, render_template, request, redirect, url_for, render_template_string  # type: ignore
import secrets


app = Flask(__name__, static_url_path='/static', template_folder='templates')

foo = secrets.token_urlsafe(16)
app.secret_key = foo

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

@app.route("/Pilares Scrum")
def pilares_scrum():
    return render_template("Modulo-1/Capitulos/Capitulo-1/Pilares-Scrum.html")

@app.route("/Capitulo2")
def capitulo2():
    return render_template("Modulo-1/Capitulos/Capitulo-2/Capitulo2.html")

@app.route("/Time Scrum")
def time_scrum():
    return render_template("Modulo-1/Capitulos/Capitulo-2/Time-Scrum.html")

@app.route("/Capitulo3")
def capitulo3():
    return render_template("Modulo-1/Capitulos/Capitulo-3/Capitulo3.html")

@app.route("/Artefatos")
def artefatos():
    return render_template("Modulo-1/Capitulos/Capitulo-3/Artefatos.html")

@app.route("/Burndown")
def burndown():
    return render_template("Modulo-1/Capitulos/Capitulo-3/Burndown.html")













#Dicionário das respostas corretas
respostas_corretas = {
    'Alt-question-1': 'Paris',
    'Alt-question-2': 'Praga',
    'Alt-question-3': 'Sua mãe, aquela gorda',
    'Alt-question-4': '1010',
    'Alt-question-5': '42',
}


@app.route('/submit_quiz', methods=['POST'])
def submit_quiz():
    respostas_usuario = request.form
    correct_answers = 0
    incorrect_answers = 0
    for questao, resposta_correta in respostas_corretas.items():
        resposta_usuario = respostas_usuario.get(questao)
        if resposta_usuario == resposta_correta:
            correct_answers += 1
        else:
            incorrect_answers += 1
    return render_template("Quiz-de-conhecimento.html", modal_show=True, correct_answers = correct_answers, incorrect_answers = incorrect_answers)


if __name__ == "__main__":
    app.run(debug = True)