valores = input().split()

CONSUMPTION = 12

time = abs(int(valores[0]))
avg_speed = abs(int(valores[1]))

distance = avg_speed * time
liters = distance / CONSUMPTION

print(f"{liters:.3f}")