# Variáveis globais
extrato = []
saldo = 0.0
saques_realizados = 0

def depositar(valor):
    global saldo
    global extrato
    if valor > 0:
        saldo += valor
        extrato.append(f"Depósito: R$ {valor:.2f}")
    else:
        print("O valor do depósito deve ser positivo.")

def sacar(valor):
    global saldo
    global extrato
    global saques_realizados

    LIMITE_SAQUE = 500.0
    MAX_SAQUES_DIARIOS = 3

    if saques_realizados >= MAX_SAQUES_DIARIOS:
        print("Limite de saques diários atingido.")
    elif valor > LIMITE_SAQUE:
        print(f"O valor máximo para saque é R$ {LIMITE_SAQUE:.2f}.")
    elif valor > saldo:
        print("Saldo insuficiente.")
    else:
        saldo -= valor
        extrato.append(f"Saque: R$ {valor:.2f}")
        saques_realizados += 1

def extrato_conta():
    global extrato
    global saldo

    if not extrato:
        print("Nenhuma transação realizada.")
    else:
        print("Extrato:")
        for transacao in extrato:
            print(transacao)
        print(f"Saldo atual: R$ {saldo:.2f}")

