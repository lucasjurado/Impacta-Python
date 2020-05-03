import random

matriz = []

def geramatriz(matriz):
    vlrs = list(range(16))
    for j in range (4):
        linha = []
        for i in range (4):
            x = random.choice(vlrs)
            linha.append(x)
            vlrs.remove(x)
        matriz.append(linha)

for i in range(3):
    matriz = []
    geramatriz(matriz)
    print(matriz)