from flask import Flask, render_template, request, redirect, url_for, render_template_string  # type: ignore
import secrets


app = Flask(__name__, static_url_path='/static', template_folder='templates')

foo = secrets.token_urlsafe(16)
app.secret_key = foo

@app.route("/")
def homepage():
    return render_template("index.html")


@app.route("/Scrum Introduction")
def scrum_introduction():
    return render_template("Scrum-Introduction.html")

@app.route("/Trilhas de Aprendizagem")
def trilhas_aprendizagem():
    return render_template("Trilhas-de-Aprendizagem.html")

@app.route("/Scrum Master")
def scrum_master():
    return render_template("Scrum-Master.html")


@app.route("/Games interativos")
def games_interativos():
    return render_template("Games-interativos.html")



@app.route("/Quiz de conhecimento")
def quiz_conhecimentos():
    return render_template("Quiz-de-conhecimento.html")



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
    resultados = []
    for questao, resposta_correta in respostas_corretas.items():
        resposta_usuario = respostas_usuario.get(questao)
        if resposta_usuario == resposta_correta:
            resultados.append(f'A resposta à alternativa está correta!')
        else:
            resultados.append(f'A resposta está incorreta. A resposta certa é {resposta_correta}.')
    return '<br>'.join(resultados)


if __name__ == "__main__":
    app.run(debug=True)