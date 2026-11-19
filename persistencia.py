import json

from agencia import Agencia
from cliente import Cliente
from corrente import ContaCorrente
from poupanca import ContaPoupanca
from transacao import Transacao


ARQUIVO_DADOS = "dados.json"


def transacao_para_dict(transacao):
    return {
        "tipo": transacao.tipo,
        "valor": transacao.valor,
        "conta_relacionada": transacao.conta_relacionada
    }


def cliente_para_dict(cliente):
    return {
        "nome": cliente.nome,
        "cpf": cliente.cpf,
        "telefone": cliente.telefone,
        "salario": cliente.salario
    }


def conta_para_dict(conta):
    historico = []

    for transacao in conta.historico_transacoes:
        historico.append(
            transacao_para_dict(transacao)
        )

    return {
        "numero": conta.numero,
        "saldo": conta.saldo,
        "tipo": conta.tipo,
        "titular_cpf": conta.cliente.cpf,
        "historico_transacoes": historico
    }


def salvar_dados(agencia, clientes):
    clientes_json = []

    for cliente in clientes:
        clientes_json.append(
            cliente_para_dict(cliente)
        )

    contas_json = []

    for conta in agencia.contas:
        contas_json.append(
            conta_para_dict(conta)
        )

    dados = {
        "clientes": clientes_json,

        "agencia": {
            "nome": agencia.nome,
            "numero": agencia.numero,
            "contas": contas_json
        }
    }

    with open(
        ARQUIVO_DADOS,
        "w",
        encoding="utf-8"
    ) as arquivo:

        json.dump(
            dados,
            arquivo,
            ensure_ascii=False,
            indent=4
        )


def carregar_dados():
    try:
        with open(
            ARQUIVO_DADOS,
            "r",
            encoding="utf-8"
        ) as arquivo:

            dados = json.load(arquivo)

    except (FileNotFoundError, json.JSONDecodeError):
        return Agencia("Agência 001", "001"), []

    clientes = []

    # Recriando os objetos Cliente
    for dados_cliente in dados.get("clientes", []):

        cliente = Cliente(
            dados_cliente["nome"],
            dados_cliente["cpf"],
            dados_cliente["telefone"],
            dados_cliente["salario"]
        )

        clientes.append(cliente)

    dados_agencia = dados.get("agencia", {})

    # Recriando o objeto Agencia
    agencia = Agencia(
        dados_agencia.get("nome", "Agência 001"),
        dados_agencia.get("numero", "001")
    )

    # Recriando as contas
    for dados_conta in dados_agencia.get("contas", []):

        cliente_encontrado = None

        for cliente in clientes:
            if cliente.cpf == dados_conta["titular_cpf"]:
                cliente_encontrado = cliente
                break

        if cliente_encontrado is None:
            continue

        # Descobre qual classe deve ser criada
        if dados_conta["tipo"] == "Corrente":

            conta = ContaCorrente(
                dados_conta["numero"],
                cliente_encontrado
            )

        elif dados_conta["tipo"] == "Poupança":

            conta = ContaPoupanca(
                dados_conta["numero"],
                cliente_encontrado
            )

        else:
            continue

        # Recupera o saldo salvo
        conta._saldo = float(
            dados_conta.get("saldo", 0.0)
        )

        # Recupera o histórico de transações
        for dados_transacao in dados_conta.get(
            "historico_transacoes",
            []
        ):

            transacao = Transacao(
                dados_transacao["tipo"],
                dados_transacao["valor"],
                dados_transacao.get(
                    "conta_relacionada"
                )
            )

            conta._historico_transacoes.append(
                transacao
            )

        agencia.adicionar_conta(conta)

    return agencia, clientes