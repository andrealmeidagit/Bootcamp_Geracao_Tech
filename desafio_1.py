entrada = input().split()

distancia = abs(int(entrada[0]))
diametro1 = abs(int(entrada[1]))
diametro2 = abs(int(entrada[2]))

#print(f"{distancia}.")
#print(f"{diametro1}.")
#print(f"{diametro2}.")

if distancia >= 10000:
    distancia = 9999
elif distancia == 0:
    distancia = 1

if diametro1 == 0:
    diametro1 = 1

if diametro2 >=100:
    diametro2 = 99

#print(f"{distancia}.")
#print(f"{diametro1}.")
#print(f"{diametro2}.")
print(f"{(distancia/(diametro1+diametro2)):.2f}")