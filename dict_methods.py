# {:}.copy()

# {:}.fromkeys() - cria chaves vazias ou com valor padrão

contatos = dict.fromkeys(["telefone", "endereço"])  # {'telefone': None, 'endereço': None}
print(contatos)
contatos = dict.fromkeys(["telefone", "endereço"],"vazio")  # {'telefone': 'vazio', 'endereço': 'vazio'}
print(contatos)


# {:}.get()

#print(contatos["CPF"])      # key error
print(contatos.get("CPF"))              # None
print(contatos.get("CPF", {}))          # {}
print(contatos.get("telefone", {}))     # valor da chave


# {:}itens() - retorna lista de tuplas - útil para iterar

contatos = {
    "andre@email.com" : {"nome" : "Andre", "telefone" : "3333-4444"}, 
}
print(contatos.items())     # dict_items([('andre@email.com', {'nome': 'Andre', 'telefone': '3333-4444'})])


# {:}.keys() - retorna lista das chaves

print(contatos.keys())      # dict_keys(['andre@email.com'])


# {:}.pop() - remove uma chave

contatos["ana@email.com"] = {"nome":"ana", "telefone":"3232-3232"}

print(contatos.pop("ana@email.com"))            # {'nome': 'ana', 'telefone': '3232-3232'}
print(contatos.pop("antonio@email.com", {}))    # {}
print(contatos.keys())      # dict_keys(['andre@email.com'])


# {:}.popitem - remove itens na ordem

print(contatos.popitem())       # ('andre@email.com', {'nome': 'Andre', 'telefone': '3333-4444'})
#print(contatos.popitem())       # KeyError: 'popitem(): dictionary is empty'


# {:}.setdefault()

contatos = {"nome":"Andre", "tele" : "999999999"}
print(contatos.setdefault("nome","pedro"))          # Andre
print(contatos)                                     # {'nome': 'Andre', 'tele': '999999999'}
print(contatos.setdefault("idade", 28))             # 28
print(contatos)                                     # {'nome': 'Andre', 'tele': '999999999', 'idade': 28}

# {:}.update()

contatos.update({"nome" : "Ana"})
contatos.update({"CPF": "013139314134"})
print(contatos)       # {'nome': 'Ana', 'tele': '999999999', 'idade': 28, 'CPF': '013139314134'}


# {:}.values()

print(contatos.values())        # dict_values(['Ana', '999999999', 28, '013139314134'])

# in

print("nome" in contatos)       # True
contatos["ana@email.com"] = {"ch1": 1, "ch2" : 2}
print(contatos)
print("ch1" in contatos["ana@email.com"])       # True

# del

del contatos["tele"]
print(contatos)     # {'nome': 'Ana', 'idade': 28, 'CPF': '013139314134', 'ana@email.com': {'ch1': 1, 'ch2': 2}}
del contatos["ana@email.com"]["ch2"]
print(contatos)     # {'nome': 'Ana', 'idade': 28, 'CPF': '013139314134', 'ana@email.com': {'ch1': 1}}
del contatos
#print(contatos)     # NameError: name 'contatos' is not defined
