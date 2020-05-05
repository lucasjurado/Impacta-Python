def inserir(n):
    lista.append(n)

def remover(n):
    if n in lista:
        lista.remove(n)

def parcial():
    lista.sort()
    for pos, item in enumerate(lista):
        if pos == len(lista)-1:
            print(item)
        else:
            print(item, end=' ')

def final():
    lista.sort()
    for item in lista:
        print(item, end=' ')
    exit()


lista = []
inicial = input('').split()
for item in inicial:
    t = int(item)
    lista.append(t)

while True:
    cmd = input('').split()
    if cmd[0] == 'parcial':
        parcial()
    elif cmd[0] == 'inserir':
        n1 = int(cmd[1])
        inserir(n1)
    elif cmd[0] == 'remover':
        n2 = int(cmd[1])
        remover(n2)
    elif cmd[0] == 'final':
        final()

