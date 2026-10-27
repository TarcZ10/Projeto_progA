from cliente import Cliente 
from conta import Conta

class Banco:
    def __init__(self):
        self.clientes = [] 
        self.contas = [] 

    def cadastrar_cliente(self, nome, cpf, endereco, telefone, salario):
        for cliente in self.clientes:
            if cliente.cpf == cpf:  # Agora chamamos .cpf (atributo) em vez de ['cpf'] (dicionário)
                return False 

        if nome != "" and cpf != "" and endereco != "" and telefone != "" and salario != "":       
            novo_cliente = Cliente(nome, cpf, endereco, telefone, salario) # Instancia o Objeto
            self.clientes.append(novo_cliente) 
            return True
        else:
            return False

    def criar_conta(self, cpf):
        for conta in self.contas:
            if conta.cliente.cpf == cpf:
                return False 

        cliente_encontrado = None
        for c in self.clientes:
            if c.cpf == cpf:
                cliente_encontrado = c 
                break 

        if cliente_encontrado:
            numero_conta = len(self.contas) + 1
            nova_conta = Conta(numero_conta, cliente_encontrado) # Instancia o Objeto
            self.contas.append(nova_conta)
            return True
        else:
            return False

    def listar_contas(self):
        if len(self.contas) == 0:
            return None
        else:
            return self.contas 

    def procurar_conta(self, numero):
        for conta in self.contas:
            if conta.numero == numero:
                return conta 
        return None 