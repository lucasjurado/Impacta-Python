while True:
    n = int(input())
    if 1<=n<=9:
        break
    else:
        print('Insira um número inicial entre 1 e 9')
while True:
    m = int(input())
    if 1<=m<=9:
        break
    else:
        print('Insira um número final entre 1 e 9')

if m>n or m==n:
    for d in range (n,m+1):
        for c in range(1,10):
            print(f'{d} x {c} = {d*c}')
        print()
elif n>m:
    print('Nenhuma tabuada nesse intervalo')