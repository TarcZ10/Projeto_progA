class Conta():
    def __init__(self, numero, cliente):
        self._numero = numero
        self._cliente = cliente
        self._saldo = 0.0
        self._historico_transacoes = []

    @property
    def numero(self):
        return self._numero

    @property
    def cliente(self):
        return self._cliente

    @property
    def tipo(self):
        pass

    @property
    def saldo(self):
        return self._saldo

    @property
    def historico_transacoes(self):
        return self._historico_transacoes

    def exibir_historico_saldo(self):
        return self.saldo, self.historico_transacoes

    def depositar(self, valor):
        if valor > 0:  
            self._saldo = self._saldo + valor
            self._historico_transacoes.append(f"Depósito: R$ {valor}")
            return True, self._saldo 
        return False, self._saldo 

    def sacar(self, valor_saque):
        if valor_saque <= 0 or valor_saque > self._saldo: 
            return False, self._saldo 
        elif self._saldo >= valor_saque:
            self._saldo = self._saldo - valor_saque 
            self._historico_transacoes.append(f"Saque: R$ {valor_saque}")
            return True, self._saldo 

    def transferir(self, valor, conta_destino):
        if valor > 0 and self._saldo >= valor:
            self._saldo -= valor
            conta_destino._saldo += valor
            self._historico_transacoes.append(f"Transferência enviada: R$ {valor} para conta {conta_destino.numero}")
            conta_destino.historico_transacoes.append(f"Transferência recebida: R$ {valor} da conta {self.numero}")
            return True
        return False
