#lista que recebe todos os valor MDC
mdc = []
#lista que recebe todos os valores MMC
mmc = []
#lista que recebe todos os valores primos
primos = []
#lista com todos os inputs
lista = [float(input('1º vlr: ')), float(input('2º vlr: ')), float(input('3º vlr: ')), float(input('4º vlr: ')), float(input('5º vlr: '))]

#Verifica se algum dos valores digitados é maior que o limite estabelecido (lim = 10000)
if max(lista) > 10000:
    print('Meu programa não é obrigado a calcular isso.')
    exit()

#Verifica se os valores adicionados são naturais (inteiro e positivo)
if (lista[0]*10)%10 != 0 or (lista[1]*10)%10 != 0 or (lista[2]*10)%10 != 0 or (lista[3]*10)%10 != 0 or (lista[4]*10)%10 != 0:
    print('Você digitou um número flutuante! Não é possível calcular mmc e mdc com os números fornecidos.')
    exit()
if (lista[0]<0 or lista[1]<0 or lista[2]<0 or lista[3]<0 or lista[4]<0):
    print('Você digitou um numero negativo! Não é possível calcular mmc e mdc com os números fornecidos.')
    exit()

#transforma os valores float em int
lista[0] = int(lista[0])
lista[1] = int(lista[1])
lista[2] = int(lista[2])
lista[3] = int(lista[3])
lista[4] = int(lista[4])

#Verifica se o valor adicionado na lista é primo, se o número de count é menor ou igual a 2, significa que ele é primo
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

if len(primos) > 0:
    print(f'Os números primos são = {primos}')
else:
    print('Nenhum número lido é primo.')

#Calcula o MDC e o MMC de cada valor da lista
c = 1
while True:
    if lista[0] % c == 0 and lista[1] % c == 0 and lista[2] % c == 0 and lista[3] % c == 0 and lista[4] % c == 0:
        mdc.append(c)
    if c % lista[0] == 0 and c % lista[1] == 0 and c % lista[2] == 0 and c % lista[3] == 0 and c % lista[4] == 0:
        mmc.append(c)
    c += 1
    if len(mmc) == 1 and c >= max(lista):
        break
print(f'mmc = {min(mmc)}; mdc = {max(mdc)}')





