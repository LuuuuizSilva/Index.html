from flask import render_template, request, Flask

app = Flask(__name__)

# Rota princial
@app.route("/")

def home ():  
    return render_template ("index.html",
    Texto = "Bem-vindo a minha pagina Interativa",
    saudacao = "Boa noite",
    prazer = "Espero que estejam bem :)") 
    
@app.route("/processar",methods= ["POST"])
def processar():
    nome = request.form["nome"]
    numero = request.form["numero"]
    mensagem = f"Olá {nome}, você digitou número {numero}"
    return render_template("index.html",resultadoForm = mensagem)
if __name__ == '__main__':
    app.run(debug=True)
