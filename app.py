from flask import Flask, render_template, request, redirect, url_for
from cliente import Cliente
from corrente import ContaCorrente
from poupanca import ContaPoupanca
from persistencia import salvar_dados, carregar_dados

app = Flask(__name__)

agencia_001, clientes = carregar_dados()

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
            salvar_dados(agencia_001, clientes)
            resultado = True

    if resultado:
        return redirect(url_for("iniciar"))
    
    return render_template("cadastrar_cliente.html")

@app.route("/criar-conta", methods=["GET", "POST"])
def criar():
    conta_criada = None 

    if request.method == "POST":
        cpf = request.form["cpf"] 
        tipo = request.form.get("tipo", "Corrente") 

        # Busca o cliente pelo CPF
        cliente_encontrado = next((c for c in clientes if c.cpf == cpf), None)

        if cliente_encontrado and tipo in ("Corrente", "Poupança"):
            numero_conta = len(agencia_001.contas) + 1
            
            if tipo == "Corrente":
                nova_conta = ContaCorrente(numero_conta, cliente_encontrado)
            else:
                nova_conta = ContaPoupanca(numero_conta, cliente_encontrado)
            
            agencia_001.adicionar_conta(nova_conta)
            salvar_dados(agencia_001, clientes)
            conta_criada = nova_conta

    return render_template("criar_conta.html", conta_criada=conta_criada)

@app.route("/listar-contas")
def listar():
    contas_cadastradas = agencia_001.contas if len(agencia_001.contas) > 0 else None
    return render_template("listar_contas.html", contas=contas_cadastradas)

@app.route("/listar-clientes")
def listar_clientes():
    lista_clientes = []

    for cliente in clientes:
        contas_do_cliente = []
        for conta in agencia_001.contas:
            if conta.cliente.cpf == cliente.cpf:
                contas_do_cliente.append(conta)

        lista_clientes.append({
            "cliente": cliente,
            "contas": contas_do_cliente
        })

    return render_template("listar_clientes.html", lista_clientes=lista_clientes)

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

            if sucesso:
                salvar_dados(agencia_001, clientes)

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

        if sucesso:
            salvar_dados(agencia_001, clientes)

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

            if sucesso:
                salvar_dados(agencia_001, clientes)
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
