frutas = ("laranja", "banana", "jabuticaba", "mamao",)      # vírgula no final - Boa prática
                                                            # evita problemas de conflitos com parêntesis de
                                                            # precedência aritmética
print(frutas)

letras = tuple("python")
print(letras)

numeros = tuple([1, 2, 3, 4, 5])
print(numeros)

pais = ("Brasil",)          # problema de conflito parêntesis acontece quando tem um elemento só
print(pais)

# Acesso direto
print(frutas[0])
print(frutas[2])
print(frutas[-1])
print(frutas[-2])

# tuplas aninhadas
matriz = (
    (1,2,3),
    (4,5,6),
    (7,8,9)
)

# fatiamento
print(letras[2:])
print(letras[:2])
print(letras[1:3])
print(letras[0:3:2])
print(letras[::])
print(letras[::-1])

# repetição
for fruta in frutas:
    print(fruta)

## Metodos de tupla
# ().count

print(frutas.count("banana"))

# ().index

print(frutas.index("banana"))

# len()

print(len(frutas))

