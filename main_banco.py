#Funções
#Função que permite cadastrar o cliente:
def cadastrar_cliente(nome,cpf,endereco,telefone):
    if nome != "" and cpf != "" and endereco != "" and telefone != "":
        print(f"Cliente {nome} adicionado com sucesso!")    
        return True
    else:
        print("ERRO: Todos os dados precisam estar preenchidos!")
        return False

#Função que cria a conta recebendo o cliente cadastrado:
def criar_conta(cliente_cadastrado):
    if cliente_cadastrado == True:
        print("Conta Criada!")
        return True

    else:
        print("ERRO: Cliente não cadastrado!")
        return False

#Função para realizar depósito
def realizar_deposito(saldo):
    valor = float(input("Valor do depósito: R$ "))
    if valor > 0:
        saldo = saldo + valor
        print("Depósito realizado!")
        print(f"Saldo atual: R${saldo:.2f}")
    else:
        print("Valor inválido.")
    return saldo

#Função para realizar o saque
def realizar_saque (saldo):
    print(f"Saldo atual: R${saldo:.2f}")
    valor_saque = float(input("Digite o valor desejado para saque: R$ "))
    if valor_saque <= 0:
        print("Digite uma quantia válida!")
    elif saldo >= valor_saque:
        saldo = saldo - valor_saque
        print("Saque realizado!")
        print(f"Saldo atual: R${saldo:.2f}")
    else:
        print("Saldo indisponível")
    return saldo
#DADOS PARA INICIAR O SISTEMA
opcao = -1
cliente_cadastrado = False
conta_criada = False
saldo = 0.0
valor_saque = 0.0

#Inicializador do sistema
while opcao != 0:

    print("\n______ SISTEMA BANCÁRIO ______ ")
    print("1 - Cadastrar cliente")
    print("2 - Criar conta")
    print("3 - Consultar saldo")
    print("4 - Depositar")
    print("5 - Sacar")
    print("0 - Sair")
    
    opcao = int(input("Escolha uma opção:\n"))

    if opcao == 1:
        print("CADASTRO DO CLIENTE:\n")

        nome = input("Digite seu nome: ")
        cpf = input("Digite seu cpf: ")
        telefone = input("Digite seu telefone: ")
        endereco = input("Digite seu endereço: ")

        cliente_cadastrado = cadastrar_cliente(nome, cpf, telefone, endereco)

    elif opcao == 2:
        if cliente_cadastrado == True:
            numero_conta = "0001"
            conta_criada = criar_conta(cliente_cadastrado)
            print("Número da conta:\n", numero_conta, "\nSaldo:\n", saldo)
        else:
            print("ERRO: Cadastre um cliente primeiro!")

    elif opcao == 3:
         print(f"Saldo: R$ {saldo:.2f}")

    elif opcao == 4:
        saldo = realizar_deposito(saldo)

    elif opcao == 5:
        saldo = realizar_saque(saldo)
