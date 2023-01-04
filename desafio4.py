letra = input().lower()

alfabeto = list("abcdefghijklmnopqrstuvwxyz")


if letra in alfabeto:
    print(alfabeto.index(letra)+1)
else:
    print("Valor digitado não era uma letra.")
