name = "Andre"
age = 28
profession = "engineer"
language = "Python"

dados = {"nome":"Andre", "idade":28, "profissao":"engineer", "linguagem":"Pyhton"}      # python dictionary

# Old style of variables concatenation (%)

print("1 - Hello! My name is %s, I am %d years old, I am a %s and I'm learning %s." %(name, age, profession, language))

# Better style: 'format' method

print("2 - Hello! My name is {}, I am {} years old, I am a {} and I'm learning {}.".format(name, age, profession, language))
print("3 - Hello! My name is {2}, I am {1} years old, I am a {0} and I'm learning {3}.".format(profession, age, name, language))
print("4 - Hello! My name is {0}, I am {0} years old, I am a {0} and I'm learning {3}.".format(profession, age, name, language))
print("5 - Hello! My name is {nome}, I am {idade} years old, I am a {profissao} and I'm learning {linguagem}.".format(nome = name, idade = age, profissao = profession, linguagem = language))

print("6 - Hello! My name is {nome}, I am {idade} years old, I am a {profissao} and I'm learning {linguagem}.".format(**dados))

# Best style - 'f' method

print(f"7 - Hello! My name is {name}, I am {age} years old, I am a {profession} and I'm learning {language}.")


## Casas decimais

PI = 3.14159

print(f"8 - O valor de 'pi' é: {PI:.2f}")
print(f"9 - O valor de 'pi' é: {PI:10.2f}")     # {float:WIDTH.DECIMALSf}