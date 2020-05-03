mdc = []
mmc = []
primos = []
lista = (float(input('1º vlr: ')), float(input('2º vlr: ')), float(input('3º vlr: ')), float(input('4º vlr: ')), float(input('5º vlr: ')))
listaInt = []

if (lista[0]*10)%10 != 0:
    print('float')

listaInt.append = int(lista[0])


#Verifica se o valor adicionado na lista é primo
count0 = 0
for c in range(1, lista[0]+1):
    if lista[0]%c == 0:
        count0 +=1
if count0 <= 2:
    primos.append(lista[0])
count1 = 0
for c in range(1, lista[1]+1):
    if lista[1]%c == 0:
        count1 +=1
if count1 <= 2:
    primos.append(lista[1])
count2 = 0
for c in range(1, lista[2]+1):
    if lista[2]%c == 0:
        count2 +=1
if count2 <= 2:
    primos.append(lista[2])
count3 = 0
for c in range(1, lista[3]+1):
    if lista[3]%c == 0:
        count3 +=1
if count3 <= 2:
    primos.append(lista[3])
count4 = 0
for c in range(1, lista[4]+1):
    if lista[4]%c == 0:
        count4 +=1
if count4 <= 2:
    primos.append(lista[4])

print(primos)


if max(lista) > 10000:
    print('Meu programa não é obrigado a calcular isso.')
else:
    c=1
    while True:
       if lista[0]%c == 0 and lista[1]%c == 0 and lista[2]%c == 0 and lista[3]%c == 0 and lista[4]%c == 0:
           mdc.append(c)
       if c%lista[0] == 0 and c%lista[1] == 0 and c%lista[2] == 0 and c%lista[3] == 0 and c%lista[4] == 0:
           mmc.append(c)
       c+=1
       if len(mmc) == 1 and c >= max(lista):
           break
    print('mmc =',min(mmc))
    print('mdc =',max(mdc))



