# conjunto não ordenado de chave - valor
# chave tem que ser um objeto imutável (Tupla, string...)

pessoa = {"nome" : "Guilherme", "idade" : 28}       # cria dicionário
print(pessoa)

fruta = dict(tipo = "banana", cor = "amarela")      # cria dicionário
print(fruta)

pessoa["telefone"] = "3326-3342"        # adiciona elemento à dicionário existente
print(pessoa)

# acessar valor
print(pessoa["nome"])
print(pessoa["idade"])
print(pessoa["telefone"])

# sobrescrever valor
pessoa["nome"] = "André"
print(pessoa["nome"])
pessoa["idade"] = 29
print(pessoa["idade"])
pessoa["telefone"] = "99987-9283"
print(pessoa["telefone"])

# dicionários aninhados
contatos = {
    "andre@email.com" : {"nome" : "Andre", "telefone" : "3333-4444"},
    "ana@email.com" : {"nome" : "Ana", "telefone" : "3555-4455"},
    "jose@email.com" : {"nome" : "Jose", "telefone" : "3333-2109", "extra" : {"a" : 1}},
}

print(contatos["ana@email.com"]["nome"])        # Ana
print(contatos["jose@email.com"]["extra"]["a"]) # 1

# repetição

for chave in contatos:
    print(contatos[chave]["nome"])

for chave, valor in contatos.items():
    print(chave, valor)