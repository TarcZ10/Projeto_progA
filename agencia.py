class Agencia:
    def __init__(self, nome, numero):
        self.nome = nome
        self.numero = numero
        self.contas = [] 

    def adicionar_conta(self, conta):
        self.contas.append(conta)

    def buscar_conta(self, numero):
        for conta in self.contas:
            if conta.numero == numero:
                return conta 
        return None 

    def calcular_patrimonio_total(self):
        # Soma o saldo de todas as contas vinculadas à agência
        return sum(conta.saldo for conta in self.contas)