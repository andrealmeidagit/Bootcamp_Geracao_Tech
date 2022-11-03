## estrutura de dados SET

# elementos únicos
# elimina os itens repetidos
# não confiar na ordenação


cj1 = set([1, 1, 1, 5, 3, 8, 9, 3, 4, 5, 6, 5, 5])      # {1, 3, 4, 5, 6, 8, 9}
print(cj1)

cj2 = set("abacaxi")        # {'a', 'c', 'i', 'b', 'x'}
print(cj2)

cj3 = set(("palio", "gol", "celta", "gol", "polo", "palio",))       # {'polo', 'celta', 'palio', 'gol'}
print(cj3)

linguagens = {"pyhton", "java", "pyhton"}       # {'java', 'pyhton'}
print(linguagens)

# conjuntos SET não possuem indexação (variável[0])

# para acessar conjuntos

numeros = {1, 1, 1, 5, 3, 8, 9, 3, 4, 5, 6, 5, 5}       # {1, 3, 4, 5, 6, 8, 9}
print(numeros)
numeros = list(numeros)         #converte para lista
print(numeros[1])

# iteração

for carro in cj3:
    print(carro)

# função enumerate

for indice, carro in enumerate(cj3):
    print(f"{indice}: {carro}")



## Metodos

# {}.union()

cj_a = {1, 2}
cj_b = {3, 4}

cj_ab = cj_a.union(cj_b)        # {1, 2, 3, 4}
print(cj_ab)


# {}.intersection()

cj_a = {1, 2, 3}
cj_b = {3, 4, 5}

cj_ab = cj_a.intersection(cj_b)     # {3}
print(cj_ab)


#{}.difference()

cj_ab = cj_a.difference(cj_b)       # {1, 2}
cj_ba = cj_b.difference(cj_a)       # {4, 5}
print(cj_ab)
print(cj_ba)


# {}.symmetric_difference()

cj_ab = cj_a.symmetric_difference(cj_b)       # {1, 2, 4, 5}
print(cj_ab)

# {}.issubset()

cj_a = {1, 2, 3}
cj_b = {4, 1, 2, 5, 6, 3}

print(cj_a.issubset(cj_b))      # True
print(cj_b.issubset(cj_a))      # False

# {}.issuperset()

print(cj_a.issuperset(cj_b))      # False
print(cj_b.issuperset(cj_a))      # True

# {}.isdisjoint()

cj_a = {1, 2, 3, 0}
cj_b = {4, 1, 2, 5, 6, 3}
cj_c = {10, 20, 30}

print(cj_a.isdisjoint(cj_b))    # False
print(cj_a.isdisjoint(cj_c))    # True

# {}.add()

cj_c.add(25)        # {25, 10, 20, 30}
print(cj_c)
cj_c.add(80)        # {10, 80, 20, 25, 30}
print(cj_c)
cj_c.add(25)        # {10, 80, 20, 25, 30}
print(cj_c)

# {}.clear()
cj_ba.clear()       # set()
print(cj_ba)

# {}.copy
cj_d = cj_b.copy()      # {1, 2, 3, 4, 5, 6}
print(cj_b, cj_d)
print(id(cj_b), id(cj_d))

# {}.discard()
cj_d.discard(1)     # {2, 3, 4, 5, 6}
print(cj_d)
cj_d.discard(45)    # {2, 3, 4, 5, 6}       não apresenta erro
print(cj_d)

# {}.pop
numeros = {1, 2, 3, 4, 5, 6, 7, 8, 9}
print(numeros.pop())    # 1
print(numeros.pop())    # 2
print(numeros.pop())    # 3
print(numeros.pop())    # 4
print(numeros.pop())    # 5
print(numeros.pop())    # 6
print(numeros)          # {7, 8, 9}

# {}.remove()
numeros.remove(8)
print(numeros)          # {7, 9}
numeros.remove(45)
print(numeros)          # key error - apresenta erro se tentar remover o que não existe

# in
numeros = {1, 2, 3, 1, 2, 4, 5, 5, 6, 7, 8, 9, 0}

print(1 in numeros)  # True
print(10 in numeros)  # False
