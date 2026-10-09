#Funções
#Função que permite cadastrar o cliente:
def cadastrar_cliente(clientes, nome, cpf, endereco, telefone):
    #Se o cpf já foi cadastrado retorna False
    for cliente in clientes:
        if cliente['cpf'] == cpf:
            return False 

    if nome != "" and cpf != "" and endereco != "" and telefone != "":       
        # Cria um dicionário com os dados
        novo_cliente = {
            "nome": nome,
            "cpf": cpf,
            "endereco": endereco,
            "telefone": telefone
        }
        clientes.append(novo_cliente) # Guarda os dados dentro da lista de clientes
        return True
    else:
        #Se algum dado estiver vazio retorna False
        return False

#Função que cria a conta e busca se já existe:
def criar_conta(contas, clientes, cpf):
    # 1. Verifica se já existe uma conta cadastrada com o CPF
    for conta in contas:
        if conta["cliente"]["cpf"] == cpf:
            return False #Se já tiver, impede a ação

    # 2. Busca o cliente pelo CPF na lista de clientes
    cliente_encontrado = None
    for c in clientes:
        if c['cpf'] == cpf:
            cliente_encontrado = c #se achar ele vai pra variavel
            break #para de procurar, pq já achou

    # 3. Se achou o cliente, cria a conta dele
    if cliente_encontrado:
        #soma um na quantidade de contas para gerar o nmr da nova conta
        numero_conta = len(contas) + 1
        #liga o cliente a conta e ao saldo zerado
        nova_conta = {
            "numero": numero_conta,
            "cliente": cliente_encontrado,
            "saldo": 0.0
        }
        #add a conta na lista de contas
        contas.append(nova_conta)
        return True
    else:
         # Cliente com este CPF não foi encontrado retona False
        return False

#Função que lista todas as contas cadastradas:
def listar_contas(contas):
    #verifica se existe alguma conta
    if len(contas) == 0:
        return None
    else:
        return contas #não estava vazia, ent mostra a lista completa

#Função que procura uma conta pelo número:
def procurar_conta(contas, numero):
    #procura na lista o nmr digitado
    for conta in contas:
        if conta["numero"] == numero:
            return conta #retorna a conta encontrada
    return None #se não, não devolve nada

#Função para realizar depósito
def realizar_deposito(saldo,valor):
    if valor > 0:  #apenas numeros positivos
        saldo = saldo + valor
    else:
        return False, saldo #retorna false e mantem o saldo
    return True, saldo #retorna True e atualiza o saldo

#Função para realizar o saque
def realizar_saque (saldo,valor_saque):
    if valor_saque <= 0 or valor_saque > saldo: #apenas nmr positivo e dentro do saldo atual
        return False, saldo #mantem o saldo
    elif saldo >= valor_saque:
        saldo = saldo - valor_saque #ação do saque
    return True, saldo #atualiza o saldo

#DADOS PARA INICIAR O SISTEMA
clientes = [] #lista de clientes
contas = [] #lista de contas