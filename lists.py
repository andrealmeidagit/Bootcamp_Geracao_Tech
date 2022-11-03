# criando listas

frutas = ["laranja", "banana", "jabuticaba"]        # cria lista com chaves "[]"

print(frutas)

frutas = []          # cria lista vazia

print(frutas)

frutas = ["laranja", "banana", "jabuticaba"]

letras = list("python")     # lista onde cada letra é um elemento - método "list" pede um argumento iterável - string é iterável

print(letras)

numeros = list(range(10))   # range dá números sequenciais

print(numeros)

carro = ["Ferrari", "F8", 4200000.0, 2020, 2900, "São Paulo", True]     # lista com tipos diferentes

print(carro)

print(frutas[0])        # acessando por acesso direto

print(frutas[2])        # acessando por acesso direto

print(frutas[-1])        # acessando por acesso direto com índice negativo (-1 retorna o últmo elemento)

print(frutas[-2])        # acessando por acesso direto com índice negativo

matriz = [              # matriz ou lista de listas
    [1, "a", 2],
    ["b", 3, 4],
    [6, 5, "c"]
]

print(matriz[0])
print(matriz[1][1])
print(matriz[0][-1])
print(matriz[-1][-1])


# Fatiamento

print(letras[2:])       # ['t', 'h', 'o', 'n']
print(letras[:2])       # ['p', 'y']
print(letras[1:3])      # ['y', 't']
print(letras[0:3:2])    # ['p', 't']            ->[inicio:fim:step]
print(letras[::])       # ['p', 'y', 't', 'h', 'o', 'n']
print(letras[::-1])     # ['n', 'o', 'h', 't', 'y', 'p']

# percorrer lista usando 'for'

carros = ["gol", "celta", "palio"]

for carro in carros:
    print(carro)


# obtendo informações úteis de listas
# filtro

numeros = list(range(30,111))
pares = []

for numero in numeros:
    if numero % 2 == 0:
        pares.append(numero)

print(pares)

# inline
impares = [numero for numero in numeros if numero % 2 != 0]
print(impares)