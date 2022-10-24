# exemplo 1

saldo = 2000.0
saque = float(input("Informe o valor do saque: "))

if saldo >= saque:
    print("realizando saque")
    saldo -= saque
    print("seu saldo é: ", saldo)
else:
    print("seu saldo é insuficiente.")

# exemplo 2
opcao = int(input("digite [1] para saque e [2] para depósito."))
if opcao == 1:
    print("saque realizado")
elif opcao == 2:
    print("deposito realizado.")
else:
    print("opcao invalida.")

# If ternário - inline

status = "Sucesso" if saldo>=saque else "Falha"
print(f"{status} ao realizar o saque!")