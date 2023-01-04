while True: 
    try: 
        lado = input().lower()
        if lado == "esquerda":
            print("ingles")
        elif lado == "direita":
            print("frances")
        elif lado == "nenhuma":
            print("portugues")
        elif lado == "ambas":
            print("caiu")
            break
        else:
            break
    except EOFError: 
        break