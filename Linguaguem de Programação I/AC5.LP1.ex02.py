lst = []

while True:
    sub_lst = []
    vlr = input().split()
    cod = int(vlr[0])
    sub_lst.append(cod)
    qnt = int(vlr[1])
    sub_lst.append(qnt)
    custo = float(vlr[2])
    sub_lst.append(custo * qnt)

    lst.append(sub_lst)

    if cod == 0:
        break
    sub_lst = []

if lst[0][0] == 0:
    print('nao tem compras')
    exit()

lst_caro = []

for item in lst:
    if item[0] != 0:
        lst_caro.append(item[2])

max = max(lst_caro)

for item in lst:
    if item[2] == max:
        print('Item mais caro')
        print(f'Codigo: {item[0]}')
        print(f'Quantidade: {item[1]}')
        print('Custo: {:.2f}'.format(item[2]))
        break