from flask import Flask, render_template, request
listaP = []
class Persona:
    def __init__(self, nome, mansione, stipendio, url):
        self.nome = nome
        self.mansione = mansione
        self.stipendio = stipendio
        self.url = url

    def __str__(self):
        return f"{self.nome} {self.mansione} {self.stipendio}"
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("formPersona.html")

@app.route('/process', methods=['GET', 'POST'])
def process():
    if request.method == 'POST':
        nome = request.form['nome']
        mansione = request.form['mansione']
        stipendio = request.form['stipendio']
        url = request.form['url']
        persona = Persona(nome, mansione, stipendio, url)
        listaP.append(persona)
        return render_template("stampaP.html", persona=persona)
@app.route("/stampaL", methods=['GET', 'POST'])
def stampaL():
    return render_template("listaD.html", lista = listaP)

@app.route("/processL", methods=['GET', 'POST'])
def processL():
    if request.method == 'POST':
        listaD = request.form.getlist('nomeD')
        listaTemp = []
        somma = 0
        for nome in listaD:
            for dip in listaP:
                if nome == dip.nome:
                    listaTemp.append(dip)
        for i in listaTemp:
            print(i)
            somma += int(i.stipendio)
        return render_template("elementiSelected.html", lista = listaTemp, somma = somma
                               )

if __name__ == '__main__':

   app.run(debug = True)
