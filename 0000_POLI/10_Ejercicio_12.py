import random
numeros = []
for i in range (10):
    numeros.append (random.randint(1, 50))

numeros.sort()
print(numeros)