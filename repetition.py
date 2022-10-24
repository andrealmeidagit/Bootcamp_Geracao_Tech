# Exemplo 1 - for

texto = input("Digite algo:")
VOGAIS = "AEIOU"

for letra in texto:
    if letra.upper() in VOGAIS:
        print(letra, end="")

print()     # pula uma linha

# Exemplo 2 - range

print(range(10))
print(list(range(10)))
print(list(range(1, 11)))
print(list(range(0,51,5)))

for numero in range(0, 10):
    print(numero, end=" ")
print()

# exemplo 3 - while
opcao = -1
while opcao != 0:
    opcao = int(input("[1] Sacar\n[2] Extrato\n[0] Sair:\n"))
    if opcao == 1:
        print("sacando....")
    elif opcao == 2:
        print("extrato...")


# exemplo 4 - break
opcao = int(input("Informe um número (10 para sair):\n"))
while True:
    print(opcao)
    if opcao == 10:
        break
    opcao = int(input())

print ("ate logo")