'''
Descrição
Você deve pedir que o usuário entre com um número inteiro, e deverá dizer se ele eh impar ou se ele eh par:

Se ele for par imprima "O numero eh N e ele eh par"
Se ele for impar imprima "O numero eh N e ele eh impar"
Onde N eh o numero digitado pelo usuário

Formato de entrada
94

Formato de saída
O numero eh 94 e ele eh par
'''

num = int(input())

if num%2 == 0:
    print(f'O numero eh {num} e ele eh par')
else:
    print(f'O numero eh {num} e ele eh impar')