from flask import Flask, render_template, request, redirect, url_for, session, flash
app = Flask(__name__)

app.secret_key = "Ukiddingme,bro?"

#3 marias
def check_list():
    if "tarefas" not in session:
        session["tarefas"] = []
    return session["tarefas"]

def add_tarefa(titulo):
    lista = check_list()
    lista.append(titulo)
    session.modified = True

def remove_tarefa(indice):
    lista = check_list()
    lista.pop(indice)
    session.modified = True

@app.route("/remove/<int:indice>")
def removing(indice):
    remove_tarefa(indice)
    session.modified = True
    return redirect('/')
    

@app.route("/redireciona")
def redirecionando():
    session.modified = True
    return redirect("/")

@app.route("/", methods = ["POST", "GET"])
def render_index():
    lista = check_list() #Return session["tarefas"]
    if request.method == "GET":
        return render_template('index.html', tarefas = lista)
    if request.method == "POST": #Se for post, peguei o formulário, adiciono tarefas, renderizo sucesso

        #Pego formulário
        titulo = request.form.get("titulo")

        #Adiciono tarefas
        add_tarefa(titulo)

        #rederia a sucesso (que volta para o index)
        return render_template("success.html")