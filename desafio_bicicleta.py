import os

class Bicicleta :
    def __init__(self, cor, modelo, ano, valor):
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor
    
    def buzinar(self):
        print("Plim, plim...")

    def parar(self):
        print("Parando bicicleta...")
        print("Bicicleta parada.")

    def correr(self):
        print("Pedalando rapido!!!!")

    #def __str__(self):
    #    return f"Bicicleta: cor = {self.cor}, marca = {self.modelo}, ano = {self.ano}, valor = R${self.valor},00"
    
    def __str__(self):
        return(f"{self.__class__.__name__}: {', '.join([f'{chave} = {valor}' for chave, valor in self.__dict__.items()])}")


b1 = Bicicleta("vermelha", "Caloi", 2022, 600)
b1.buzinar()
b1.correr()
b1.parar()

print(b1.cor, b1.modelo, b1.ano, b1.valor)


os.system("pause")
os.system('cls' if os.name == 'nt' else 'clear')
##########################

b2 = Bicicleta("verde", "Specialized", 2018, 30000)

Bicicleta.buzinar(b2)       # Equivale a b2.buzinar()

print(b2)       # imprime self.__str__
