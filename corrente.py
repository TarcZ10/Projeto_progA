from conta import Conta


class ContaCorrente(Conta):
    def __init__(self, numero, cliente):
        super().__init__(numero, cliente)
        self.__taxa_manutencao = 10.0

    @property
    def tipo(self):
        return "Corrente"

    def descontar_taxa(self):
        if self._saldo < self.__taxa_manutencao:
            return False, self._saldo
        self._saldo -= self.__taxa_manutencao
        self._historico_transacoes.append(
            f"Taxa de manutenção: R$ {self.__taxa_manutencao}"
        )
        return True, self._saldo
