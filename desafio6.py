salario = int(input()) 

def imprime(novo_salario, reajuste, percentual):
    salario = str(f"{novo_salario:.2f}").replace(".",",")
    reajst = str(f"{reajuste:.2f}").replace(".",",")
    print(f"Novo salario: {salario}")
    print(f"Reajuste ganho: {reajst}")
    print(f"Em percentual: {percentual}%")


if salario <= 600:
    imprime(salario*1.17, salario*1.17-salario, 17)
elif salario<=900:
    imprime(salario*1.13, salario*1.13-salario , 13)
elif salario<=1500:
    imprime(salario*1.12, salario*1.12-salario , 12)
elif salario<=20000:
    imprime(salario*1.1, salario*1.1-salario , 10)
else:
    imprime(salario*1.05, salario*1.05-salario , 5)