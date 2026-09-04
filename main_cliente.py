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


#DADOS PARA INICIAR O SISTEMA
cliente_cadastrado = False
conta_criada = False
saldo = 0.0
opcao = -1

#Inicializador do sistema
while opcao != 0:

    print("\n===== SISTEMA BANCÁRIO =====")
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
            saldo = 0.0
            print("Número da conta:\n", numero_conta, "Saldo:\n", saldo)
            conta_criada = criar_conta(cliente_cadastrado)
        else:
            print("ERRO: Cadastre um cliente primeiro!")