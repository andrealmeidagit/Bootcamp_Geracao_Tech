produto_1 = 20
produto_2 = 10
saldo = 500
saque = 250


# Aritméticos
print(produto_1 + produto_2)
print(produto_1 - produto_2)
print(produto_1 / produto_2)    # divisão float
print(produto_1 // produto_2)   # divisão inteira
print(produto_1 * produto_2)
print(produto_1 % produto_2)  # módulo (resto)
print(produto_1 ** produto_2)   # exponenciação


# De comparação
print(saldo == saque) # resultado boleano
print(saldo != saque) # resultado boleano
print(saldo > saque) # resultado boleano
print(saldo >= saque) # resultado boleano
print(saldo < saque) # resultado boleano
print(saldo <= saque) # resultado boleano

# Atribuição
dinheiro = 500
print(dinheiro)
dinheiro += 200
print(dinheiro)
dinheiro -= 100
print(dinheiro)
dinheiro *= 100
print(dinheiro)
dinheiro //= 10
print(dinheiro)
dinheiro /= 10
print(dinheiro)
dinheiro %= 580
print(dinheiro)
dinheiro **= 2
print(dinheiro)

# Lógicos
print(True or False)
print(True and False)
print(not "valor")
print(not "")

# Identidade
curso = "curso de pyhton"
nome_do_curso = curso
saldo, limite = 200, 200    # o gerenciador de memória do python aproveita o mesmo objeto
numeros_1 = [1, 2, 3]
numeros_2 = [1, 2, 3]

print(curso is nome_do_curso)       # verifica se ocupam a mesma região de memória
print(curso is not nome_do_curso)   # verifica se não ocupa a mesma região de memória
print(saldo is limite)              # verifica se ocupam a mesma região de memória
print(saldo is not limite)          # verifica se não ocupa a mesma região de memória
print(numeros_1 is numeros_2)       # verifica se ocupam a mesma região de memória
print(numeros_1 is not numeros_2)   # verifica se não ocupa a mesma região de memória

# Associação
curso = "curso de pyhton"
frutas = ["laranja", "maca", "pera"]
dividas = [1000, 500]

print("pyhton" in curso)
print("laranja" in frutas)
print(200 in dividas)
print("limão" not in frutas)
print("Laranja" in frutas)