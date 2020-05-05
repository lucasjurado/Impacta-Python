def bis(ano):
    if len(ano) == 4:
        n = int(ano)
        if n % 4 == 0 and n % 100 != 0 or n % 400 == 0:
            if n >= 2020:
                print(f'O ano {n} serah bissexto')
            else:
                print(f'O ano {n} foi bissexto')
        else:
            print(f'O ano {n} NAO eh bissexto')
    else:
        print('Ano invalido')


vlr = input().split()

for i in vlr:
    bis(i)