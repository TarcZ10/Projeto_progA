from conta import Conta

class ContaPoupanca(Conta):
    def __init__(self, numero, cliente):
        super().__init__(numero, cliente)
        self.__taxa_rendimento = 0.005

    @property
    def tipo(self):
        return "Poupança"

    def aplicar_rendimento(self):
        rendimento = self._saldo * self.__taxa_rendimento
        self._saldo += rendimento
        self._historico_transacoes.append(f"Rendimento: R$ {rendimento}")
        return True, self._saldo
