from cliente import Cliente

class Conta:
    def __init__(self, numero, cliente):
        self._numero = numero
        self._cliente = cliente
        self._saldo = 0.0

    @property
    def numero(self):
        return self._numero

    @property
    def cliente(self):
        return self._cliente

    @property
    def saldo(self):
        return self._saldo

    # Os métodos de saque e depósito agora pertencem à Conta.
    # Eles acessam o próprio saldo através de "self._saldo"
    def realizar_deposito(self, valor):
        if valor > 0:  
            self._saldo = self._saldo + valor
        else:
            return False, self._saldo 
        return True, self._saldo 

    def realizar_saque(self, valor_saque):
        if valor_saque <= 0 or valor_saque > self._saldo: 
            return False, self._saldo 
        elif self._saldo >= valor_saque:
            self._saldo = self._saldo - valor_saque 
        return True, self._saldo 