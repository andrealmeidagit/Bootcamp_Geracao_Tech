# em python a identação muda o escopo do código, não tem '{}' para abrir e fechar os blocos

def sacar (valor):
    saldo = 500

    if saldo>=valor:
        print("valor sacado")
        print("retire o dinheiro")
        saldo -= valor
        print("seu saldo é: ", saldo)

    print("obrigado por ser nosso cliente")

def depositar(valor):
    saldo = 500
    saldo += valor
    print("seu novo saldo é ", saldo)


sacar(200)
depositar(200)