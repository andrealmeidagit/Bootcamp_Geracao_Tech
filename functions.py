import os

# funções são definidas pelo marcador DEF

def show_message():
    print("Hello Function!")

def show_message2(name):            # se não passar argumento dá erro
    print(f"Welcome, {name}!")

def show_message3(name = "Anonimo"):    # argumento padrão, pode chamar sem passar argumento
    print(f"Hi, {name}!")

show_message()
show_message2(name = "Andre")
show_message3()
show_message3(name = "Astolfo")

os.system("pause")
os.system('cls' if os.name == 'nt' else 'clear')

## Retornando valores usando return - retorna NONE por padrão

def calculate_total(numbers):
    return sum(numbers)

def predecessor_and_successor(number):
    predecessor = number - 1
    successor = number + 1
    return predecessor, successor

total_sum = calculate_total([10, 20, 34])       # 64
print(total_sum)
pred_and_suc = predecessor_and_successor(10)    # (9, 11) - tupla (pq é imutável)
print(pred_and_suc)

def func_none():
    print("Hello World!")

print(func_none())      # Hello World + None


# os.system("pause")
#os.system('cls' if os.name == 'nt' else 'clear')