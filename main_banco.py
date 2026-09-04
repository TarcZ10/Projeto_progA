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

#parte para o sistema de menu
elif opcao == 4:
        saldo = realizar_deposito(saldo)
