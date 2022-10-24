valores = input().split() 

hotdogs = abs(int(valores[0]))
participants = abs(int(valores[1]))

#print(f"{hotdogs:.2f}")
#print(f"{participants:.2f}")

if hotdogs == 0:
    hotdogs = 1

if participants >1000:
    participants = 1000

#print(f"{hotdogs:.2f}")
#print(f"{participants:.2f}")

#average = round(hotdogs/participants,2)
notround = hotdogs/participants

#print(average)
#print(notround)
print(f"{notround:.2f}")