'''
Descrição
Faça um programa de resolução de tabuada. O programa deve inicialmente receber 2 números que indicam de quais números devem ser impressas a tabuada. Por exemplo, se forem recebidos os valores 2 e 5, seu programa deve imprimir a tabuada de 2, 3, 4 e 5. O programa só deve aceitar valores entre 1 e 9. Enquanto o usuário digitar valores que não sejam esses, emita uma mensagem de erro.

Formato de entrada
Dois números em 2 linhas distintas indicando o intervalos dos números das tabuadas.

Formato de saída
As tabuadas dos números dentro do intervalo.
'''

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