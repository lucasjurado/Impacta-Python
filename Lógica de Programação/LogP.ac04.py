print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
print('\t\t\t<<<<<< AC04 - LÓGICA DE PROGRAMAÇÃO >>>>>>')
print('-----------------------------------------------------------------')
while True:
    try:
        n = int(input('Digite a quantidade de nomes da Lista: '))
        if 3 < n < 10:
            break
        else:
            print('Erro! Por favor, digite um valor entre 4 e 9.')
            print('-----------------------------------------------------------------')
    except:
        print('Erro! Por favor, digite um <número inteiro>.')
        print('-----------------------------------------------------------------')
        continue
print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')

lista = []
for i in range(n):
    if i==3:
        lista.append('TESTE')
        print(f'O índice [{i}] foi preenchido automaticamente com: "TESTE".')
    else:
        nome = str(input(f'Digite um nome para o índice [{i}] da lista: ')).upper()
        lista.append(nome)

print('\n=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
print(f'Lista após o prenchimento inicial com {n} nomes:\n{lista}')

print('\n=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
exc = lista[2]
del lista[2]
print(f'Lista após a exclusão do indíce [2] => "{exc}" da lista:\n{lista}')

print('\n=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
ana = lista.count('ANA')

if ana>0:
    print(f'O nome "ANA" aparece {ana} vez(es) na lista.')
    print(f'Sendo apresentado pela primeira vez na posição [{lista.index("ANA")}] da lista.')
else:
    print('O nome "ANA" não existe na lista.')

print('\n=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
lista.sort()
print('Lista em ordem alfabética: ', end='')
for pos,p in enumerate(lista):
    if pos == len(lista)-1:
        print(p, end='.')
    elif pos == len(lista)-2:
        print(p, end=' e ')
    else:
        print(p, end=', ')
print('\n=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')