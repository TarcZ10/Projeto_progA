#Funções
#Função que permite cadastrar o cliente:
def cadastrar_cliente(clientes, nome,cpf,endereco,telefone):

    for cliente in clientes:
        if cliente['cpf'] == cpf:
            print("ERRO: CPF já cadastrado!")
            return False

    if nome != "" and cpf != "" and endereco != "" and telefone != "":       
        novo_cliente = {
            "nome": nome,
            "cpf": cpf,
            "endereco": endereco,
            "telefone": telefone
        }
        clientes.append(novo_cliente)

        print(f"Cliente {nome} adicionado com sucesso!")    
        return True
    else:
        print("ERRO: Todos os dados precisam estar preenchidos!")
        return False

#Função que cria a conta e busca se já existe:
def criar_conta(contas, clientes, cpf):
    # 1. Verifica se já existe uma conta cadastrada para este CPF
    for conta in contas:
        if conta["cliente"]["cpf"] == cpf:
            print(f"ERRO: O CPF {cpf} está indisponível!")
            return False

    # 2. Busca o cliente pelo CPF
    cliente_encontrado = None
    for c in clientes:
        if c['cpf'] == cpf:
            cliente_encontrado = c
            break

    # 3. Se não tinha conta, cria uma nova conta
    if cliente_encontrado:
        numero_conta = len(contas) + 1
        nova_conta = {
            "numero": numero_conta,
            "cliente": cliente_encontrado,
            "saldo": 0.0
        }
        contas.append(nova_conta)
        print(f"\nConta #{numero_conta} criada com sucesso para {cliente_encontrado['nome']}!")
        return True
    else:
        print("ERRO: Cliente com este CPF não foi encontrado! Cadastre o cliente primeiro.")
        return False

#Função que lista todas as contas cadastradas:
def listar_contas(contas):
    if len(contas) == 0:
        print("\nNenhuma conta cadastrada ainda!")
        return False

    print("\n--- LISTA DE CONTAS ---")
    for conta in contas:
        print(f"Conta #{conta['numero']}")
        print(f"  Cliente: {conta['cliente']['nome']}")
        print(f"  CPF: {conta['cliente']['cpf']}")
        print(f"  Saldo: R${conta['saldo']:.2f}")
        print("-----------------------")
    return True

#Função que procura uma conta pelo número:
def procurar_conta(contas, numero):
    for conta in contas:
        if conta["numero"] == numero:
            return conta
    return None

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
clientes = []
contas = []
opcao = -1

#Inicializador do sistema
while opcao != 0:

    print("\n______ SISTEMA BANCÁRIO ______ ")
    print("1 - Cadastrar cliente")
    print("2 - Criar conta")
    print("3 - Consultar saldo")
    print("4 - Depositar")
    print("5 - Sacar")
    print("6 - Listar contas")
    print("7 - Procurar conta pelo número")
    print("0 - Sair")
    
    opcao = int(input("Escolha uma opção:\n"))

    if opcao == 1:
        print("CADASTRO DO CLIENTE:\n")

        nome = input("Digite seu nome: ")
        cpf = input("Digite seu cpf: ")
        telefone = input("Digite seu telefone: ")
        endereco = input("Digite seu endereço: ")

        cliente_cadastrado = cadastrar_cliente(clientes, nome, cpf, endereco, telefone)

    elif opcao == 2:
        print("\n--- CRIAÇÃO DE CONTA ---")
        cpf = input("Digite seu CPF: ")
        criar_conta(contas, clientes, cpf)

    elif opcao == 3:
        print("\n--- CONSULTAR SALDO ---")
        numero = int(input("Digite o número da conta: "))
        conta_encontrada = procurar_conta(contas, numero)

        if conta_encontrada != None:
            print(f"Saldo: R$ {conta_encontrada['saldo']:.2f}")
        else:
            print("Conta não encontrada!")

    elif opcao == 4:
        print("\n--- DEPÓSITO ---")
        numero = int(input("Digite o número da conta: "))
        conta_encontrada = procurar_conta(contas, numero)

        if conta_encontrada != None:
            conta_encontrada["saldo"] = realizar_deposito(conta_encontrada["saldo"])
        else:
            print("Conta não encontrada!")

    elif opcao == 5:
        print("\n--- SAQUE ---")
        numero = int(input("Digite o número da conta: "))
        conta_encontrada = procurar_conta(contas, numero)

        if conta_encontrada != None:
            conta_encontrada["saldo"] = realizar_saque(conta_encontrada["saldo"])
        else:
            print("Conta não encontrada!")

    elif opcao == 6:
        listar_contas(contas)

    elif opcao == 7:
        print("\n--- PROCURAR CONTA ---")
        numero = int(input("Digite o número da conta: "))
        conta_encontrada = procurar_conta(contas, numero)

        if conta_encontrada != None:
            print(f"\nConta #{conta_encontrada['numero']} encontrada!")
            print(f"  Cliente: {conta_encontrada['cliente']['nome']}")
            print(f"  CPF: {conta_encontrada['cliente']['cpf']}")
            print(f"  Telefone: {conta_encontrada['cliente']['telefone']}")
            print(f"  Endereço: {conta_encontrada['cliente']['endereco']}")
            print(f"  Saldo: R${conta_encontrada['saldo']:.2f}")
        else:
            print("Conta não encontrada!")