class Transacao:
    def __init__(self, tipo, valor, conta_relacionada=None):
        self._tipo = tipo
        self._valor = float(valor)
        self._conta_relacionada = conta_relacionada

    @property
    def tipo(self):
        return self._tipo

    @property
    def valor(self):
        return self._valor

    @property
    def conta_relacionada(self):
        return self._conta_relacionada

    def __str__(self):
        if self._tipo == "Transferência enviada":
            return (
                f"Transferência enviada: R$ {self._valor:.2f} "
                f"para conta {self._conta_relacionada}"
            )

        elif self._tipo == "Transferência recebida":
            return (
                f"Transferência recebida: R$ {self._valor:.2f} "
                f"da conta {self._conta_relacionada}"
            )

        return f"{self._tipo}: R$ {self._valor:.2f}"