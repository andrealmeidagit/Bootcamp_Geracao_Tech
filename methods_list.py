# [].append

lista = []
lista.append(1)
lista.append("python")  # [1, 'python']
lista.append([40, 30, 20])      # [1, 'python', [40, 30, 20]]
print(lista)

# [].clear
lista.clear()       # []
print(lista)

# [].copy
lista = [1, 'python', [40, 30, 20]]
l2 = lista.copy()
print(l2)
print(id(l2), id(lista))        # IDs diferentes, outra lista
l2[0] = 360
print(l2)
print(lista)

# [].count
cores = ["vermelho", "verde", "azul", "verde"]
print(cores.count("vermelho"))      # 1
print(cores.count("verde"))         # 2
print(cores.count("azul"))          # 1

# [].extend
linguagens = ["python", "c#", "js"]     # ['python', 'c#', 'js']
print(linguagens)
linguagens.extend(["java", "c++"])      # ['python', 'c#', 'js', 'java', 'c++']
print(linguagens)
linguagens.extend(["ruby", "pyhton"])   # ['python', 'c#', 'js', 'java', 'c++', 'ruby', 'pyhton'] pyhton 2 vezes
print(linguagens)

# [].index
print(linguagens.index("js"))       # 2
print(linguagens.index("python"))   # 0 (retorna somente a primeira ocorrência)

# [].pop
print(linguagens.pop())     # "pyhton"
print(linguagens)                   # ['python', 'c#', 'js', 'java', 'c++', 'ruby']
print(linguagens.pop())     # "ruby"
print(linguagens)                   # ['python', 'c#', 'js', 'java', 'c++']
print(linguagens.pop(1))    # "c#"
print(linguagens)                   # ['python', 'js', 'java', 'c++']

# [].remove
linguagens.remove("java")
print(linguagens)           # ['python', 'js', 'c++']
linguagens.extend(["c", "c#", "c"])      # ['python', 'js', 'c++', 'c', 'c#', 'c']
linguagens.remove("c")      # remove a primeira instância
print(linguagens)           # ['python', 'js', 'c++', 'c#', 'c']

# [].sort
linguagens = ['python', 'c#', 'js', 'java', 'c++', 'ruby']
linguagens.sort()       # ['c#', 'c++', 'java', 'js', 'python', 'ruby']
print(linguagens)
linguagens = ['python', 'c#', 'js', 'java', 'c++', 'ruby']
linguagens.sort(reverse=True)       # ['ruby', 'python', 'js', 'java', 'c++', 'c#']
print(linguagens)
linguagens = ['python', 'c#', 'js', 'java', 'c++', 'ruby']
linguagens.sort(key = lambda x: len(x))       # ['c#', 'js', 'c++', 'java', 'ruby', 'python']   função customizada
print(linguagens)
linguagens.sort(key = lambda x: len(x), reverse=True)  # ['python', 'java', 'ruby', 'c++', 'c#', 'js']
print(linguagens)

# len() - função - pega o tamanho do elemento iterável
print(len(linguagens))  # 6

# sorted() - função - igual [].sort
print(sorted(linguagens))           # ['c#', 'c++', 'java', 'js', 'python', 'ruby']
print(sorted(linguagens, key = lambda x: len(x), reverse=True))     # ['python', 'java', 'ruby', 'c++', 'c#', 'js']