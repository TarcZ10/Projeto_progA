from flask import Flask, render_template, request, redirect, url_for
from agencia import Agencia
from cliente import Cliente
from conta import Conta

app = Flask(__name__)

#Agência Única
agencia_001 = Agencia("Agência 001", "001")

# Lista geral de clientes
clientes = [] 

@app.route("/") 
def iniciar():
    return render_template("index.html")

@app.route("/cadastrar-cliente", methods=["GET","POST"])
def cadastrar():
    resultado = None

    if request.method == "POST":
        nome = request.form["nome"]
        cpf = request.form["cpf"]
        telefone = request.form["telefone"]
        salario = request.form["salario"]

        # Validação se o cliente já existe e criação
        cpf_existe = any(c.cpf == cpf for c in clientes)
        if not cpf_existe and nome != "" and cpf != "" and telefone != "" and salario != "":
            novo_cliente = Cliente(nome, cpf, telefone, salario)
            clientes.append(novo_cliente)
            resultado = True

    if resultado:
        return redirect(url_for("iniciar"))
    
    return render_template("cadastrar_cliente.html")

@app.route("/criar-conta", methods=["GET", "POST"])
def criar():
    conta_criada = None 

    if request.method == "POST":
        cpf = request.form["cpf"] 
        # Como o HTML ainda não tem esse campo, definimos 'Corrente' como padrão
        tipo = request.form.get("tipo", "Corrente") 

        # Busca o cliente pelo CPF
        cliente_encontrado = next((c for c in clientes if c.cpf == cpf), None)

        if cliente_encontrado:
            numero_conta = len(agencia_001.contas) + 1
            
            # REGRA II: A conta recebe APENAS 1 cliente (Titularidade)
            nova_conta = Conta(numero_conta, cliente_encontrado, tipo)
            
            # REGRA III: Múltiplas Contas. A trava que bloqueava CPFs repetidos 
            # foi removida. O cliente pode criar quantas quiser.
            agencia_001.adicionar_conta(nova_conta)
            conta_criada = nova_conta

    return render_template("criar_conta.html", conta_criada=conta_criada)

@app.route("/listar-contas")
def listar():
    contas_cadastradas = agencia_001.contas if len(agencia_001.contas) > 0 else None
    return render_template("listar_contas.html", contas=contas_cadastradas)

@app.route("/consultar-saldo", methods=["GET", "POST"])
def consultar_saldo():
    conta_encontrada = None
    if request.method == "POST":
        numero = int(request.form["numero"])
        conta_encontrada = agencia_001.buscar_conta(numero)
        
    return render_template("consultar_saldo.html", conta=conta_encontrada)

@app.route("/depositar", methods=["GET", "POST"])
def depositar():
    conta_encontrada = None
    sucesso = None
    if request.method == "POST":
        numero = int(request.form["numero"])
        valor = float(request.form["valor"])
        conta_encontrada = agencia_001.buscar_conta(numero)

        if conta_encontrada is not None:
            sucesso, novo_saldo = conta_encontrada.depositar(valor)

    return render_template("deposito.html", conta=conta_encontrada, sucesso=sucesso)

@app.route("/sacar", methods=["GET", "POST"])
def sacar():
    conta_encontrada = None
    sucesso = None
    if request.method == "POST":
        numero = int(request.form["numero"])
        valor = float(request.form["valor"])
        conta_encontrada = agencia_001.buscar_conta(numero)

        if conta_encontrada is not None:
            sucesso, novo_saldo = conta_encontrada.sacar(valor)

    return render_template("saque.html", conta=conta_encontrada, sucesso=sucesso)

@app.route("/procurar-conta", methods=["GET", "POST"])
def procurar():
    conta_encontrada = None
    if request.method == "POST":
        numero = int(request.form["numero"])
        conta_encontrada = agencia_001.buscar_conta(numero)

    return render_template("procurar_conta.html", conta=conta_encontrada)

@app.route("/transferir", methods=["GET", "POST"])
def transferir():
    conta_origem = None
    conta_destino = None
    sucesso = None

    if request.method == "POST":
        numero_origem = int(request.form["numero_origem"])
        numero_destino = int(request.form["numero_destino"])
        valor = float(request.form["valor"])

        conta_origem = agencia_001.buscar_conta(numero_origem)
        conta_destino = agencia_001.buscar_conta(numero_destino)

        if conta_origem is not None and conta_destino is not None and conta_origem.numero != conta_destino.numero:
            sucesso = conta_origem.transferir(valor, conta_destino)
        else:
            sucesso = False

    return render_template(
        "transferir.html",
        conta_origem=conta_origem,
        conta_destino=conta_destino,
        sucesso=sucesso
    )

@app.route("/patrimonio")
def patrimonio():
    total = agencia_001.calcular_patrimonio_total()
    return render_template(
        "patrimonio.html",
        agencia=agencia_001,
        total=total
    )