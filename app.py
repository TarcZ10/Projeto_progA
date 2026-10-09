#importa as ferramentas do Flask e as funções do banco.py
from flask import Flask, render_template, request, redirect, url_for
from banco import clientes, contas, cadastrar_cliente, criar_conta, listar_contas, procurar_conta, realizar_deposito, realizar_saque

#inicia o servidor do site
app = Flask(__name__)

@app.route("/") #pagina principal do site
def iniciar():
    return render_template("index.html") #exibe a tela index.html

#acesso da pag com o GET e envio dos dados POST
@app.route("/cadastrar-cliente", methods=["GET","POST"])
def cadastrar():
        resultado = None

        #envia os dados
        if request.method == "POST":
              nome = request.form["nome"]
              cpf = request.form["cpf"]
              endereco = request.form["endereco"]
              telefone = request.form["telefone"]

            #chama a função do banco.py e passa os dados
              resultado = cadastrar_cliente(
                    clientes, 
                    nome, 
                    cpf, 
                    endereco, 
                    telefone
              )

        #print(clientes)
        if resultado:
            return redirect(url_for("iniciar"))
        
        # Se foi só um acesso ou erro, mostra a tela de cadastro
        return render_template("cadastrar_cliente.html")

@app.route("/criar-conta", methods=["GET", "POST"])
def criar():
    conta_criada = None #variavel pra guardar a conta

    if request.method == "POST":
        cpf = request.form["cpf"] #pega o CPF digitado

        #chama o banco.py para criar a conta
        resultado = criar_conta(
            contas,
            clientes,
            cpf
        )
    #se retornou True, pega a ultima conta da lista
        if resultado:
            conta_criada = contas[-1]
#passa a variável 'conta_criada' para o HTML mostrar na tela
    return render_template(
        "criar_conta.html",
        conta_criada=conta_criada
    )

@app.route("/listar-contas")
def listar():
    #pega a lista de contas do banco.py
    contas_cadastradas = listar_contas(contas)

    #passa as contas para o html
    return render_template(
        "listar_contas.html",
        contas=contas_cadastradas
    )

@app.route("/consultar-saldo", methods=["GET", "POST"])
def consultar_saldo():
    conta_encontrada = None

    if request.method == "POST":
        numero = int(request.form["numero"])

        conta_encontrada = procurar_conta(
            contas,
            numero
        )
    #não aparece nada caso não encontre a conta 
    return render_template(
        "consultar_saldo.html",
        conta=conta_encontrada
    )

@app.route("/depositar", methods=["GET", "POST"])
def depositar():
    conta_encontrada = None
    sucesso = None

    #converte os dados pra int e float
    if request.method == "POST":
        numero = int(request.form["numero"])
        valor = float(request.form["valor"])

        #procura a conta pelo número
        conta_encontrada = procurar_conta(contas, numero)

        #se achou a conta
        if conta_encontrada is not None:
            #chama a função de deposito e devolve se deu certo e o novo valor
            sucesso, novo_saldo = realizar_deposito(
                conta_encontrada["saldo"],
                valor
            )
            #se passou, atualiza na conta o novo saldo
            if sucesso:
                conta_encontrada["saldo"] = novo_saldo

    #retorna para a tela se deu sucesso e qual foi a conta movimentada
    return render_template(
        "deposito.html",
        conta=conta_encontrada,
        sucesso=sucesso
    )

@app.route("/sacar", methods=["GET", "POST"])
def sacar():
    conta_encontrada = None
    sucesso = None

    if request.method == "POST":
        numero = int(request.form["numero"])
        valor = float(request.form["valor"])

        conta_encontrada = procurar_conta(contas, numero)

        if conta_encontrada is not None:
            sucesso, novo_saldo = realizar_saque(
                conta_encontrada["saldo"],
                valor
            )

            if sucesso:
                conta_encontrada["saldo"] = novo_saldo

    return render_template(
        "saque.html",
        conta=conta_encontrada,
        sucesso=sucesso
    )

@app.route("/procurar-conta", methods=["GET", "POST"])
def procurar():
    conta_encontrada = None

    if request.method == "POST":
        numero = int(request.form["numero"])

        conta_encontrada = procurar_conta(
            contas,
            numero
        )

    return render_template(
        "procurar_conta.html",
        conta=conta_encontrada
    )