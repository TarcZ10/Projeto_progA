class Cliente:
    def __init__(self, nome, cpf, telefone, salario):
        self._nome = nome
        self._cpf = cpf
        self._telefone = telefone
        self._salario = float(salario)

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def alterar_nome(self, novo_nome):
        if novo_nome == "":
            raise ValueError("Digite seu nome!")
        self._nome = novo_nome

    @property
    def cpf(self):
        return self._cpf

    @property
    def telefone(self):
        return self._telefone

    @telefone.setter
    def alterar_telefone(self, novo_telefone):
        if novo_telefone == "":
            raise ValueError("Digite seu número!")
        self._telefone = novo_telefone

    @property
    def salario(self):
        return self._salario
    
    @salario.setter
    def alterar_salario(self, novo_salario):
        if novo_salario == "":
            raise ValueError("Digite algum valor!")
        if float(novo_salario) <= 0:
            raise ValueError("Valor inválido!")
        if float(novo_salario) == self.salario:
            raise ValueError("Valor repetido!")
        self._salario = float(novo_salario)