#importa as ferramentas do Flask
from flask import Flask, render_template, request, redirect, url_for
from banco import Banco

#inicia o servidor do site
sistema_banco = Banco()
app = Flask(__name__)

@app.route("/") 
def iniciar():
    return render_template("index.html") 

@app.route("/cadastrar-cliente", methods=["GET","POST"])
def cadastrar():
    resultado = None

    if request.method == "POST":
        nome = request.form["nome"]
        cpf = request.form["cpf"]
        endereco = request.form["endereco"]
        telefone = request.form["telefone"]
        salario = request.form["salario"]

        # Chama a função de cadastro que está DENTRO do objeto sistema_banco
        resultado = sistema_banco.cadastrar_cliente(nome, cpf, endereco, telefone, salario)

    if resultado:
        return redirect(url_for("iniciar"))
    
    return render_template("cadastrar_cliente.html")

@app.route("/criar-conta", methods=["GET", "POST"])
def criar():
    conta_criada = None 

    if request.method == "POST":
        cpf = request.form["cpf"] 

        resultado = sistema_banco.criar_conta(cpf)
        
        if resultado:
            conta_criada = sistema_banco.contas[-1]

    return render_template("criar_conta_preview.html", conta_criada=conta_criada)

@app.route("/listar-contas")
def listar():
    contas_cadastradas = sistema_banco.listar_contas()

    return render_template("listar_contas_preview.html", contas=contas_cadastradas)

@app.route("/consultar-saldo", methods=["GET", "POST"])
def consultar_saldo():
    conta_encontrada = None

    if request.method == "POST":
        numero = int(request.form["numero"])
        conta_encontrada = sistema_banco.procurar_conta(numero)
        
    return render_template("consultar_saldo_preview.html", conta=conta_encontrada)

@app.route("/depositar", methods=["GET", "POST"])
def depositar():
    conta_encontrada = None
    sucesso = None

    if request.method == "POST":
        numero = int(request.form["numero"])
        valor = float(request.form["valor"])

        conta_encontrada = sistema_banco.procurar_conta(numero)

        if conta_encontrada is not None:
            # Em POO, o depósito é uma ação DA CONTA. Portanto, chamamos a função a partir da conta encontrada!
            sucesso, novo_saldo = conta_encontrada.realizar_deposito(valor)

    return render_template("deposito_preview.html", conta=conta_encontrada, sucesso=sucesso)

@app.route("/sacar", methods=["GET", "POST"])
def sacar():
    conta_encontrada = None
    sucesso = None

    if request.method == "POST":
        numero = int(request.form["numero"])
        valor = float(request.form["valor"])

        conta_encontrada = sistema_banco.procurar_conta(numero)

        if conta_encontrada is not None:
            # O mesmo para o saque: a ação pertence ao objeto da conta.
            sucesso, novo_saldo = conta_encontrada.realizar_saque(valor)

    return render_template("saque_preview.html", conta=conta_encontrada, sucesso=sucesso)

@app.route("/procurar-conta", methods=["GET", "POST"])
def procurar():
    conta_encontrada = None

    if request.method == "POST":
        numero = int(request.form["numero"])
        conta_encontrada = sistema_banco.procurar_conta(numero)

    return render_template("procurar_conta_preview.html", conta=conta_encontrada)