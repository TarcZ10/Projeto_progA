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


#Parte para introduzir no sistema de menu
valor_saque = 0.0

    elif opcao == 5:
        saldo = realizar_saque(saldo)
