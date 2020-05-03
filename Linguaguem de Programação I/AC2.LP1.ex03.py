'''
Descrição
Dados dois números inteiros A e B, exibir:

- 'A eh maior', se A for maior do que B;
- 'B eh maior', se B for maior do que A;
- 'iguais', se os números forem iguais.

Formato de entrada
Na primeira linha o número inteiro correspondente ao A; na segunda linha o número inteiro correspondente ao B.

Formato de saída
A frase 'A eh maior' (sem aspas) ou 'B eh maior' (sem aspas) ou 'iguais' (sem aspas), de acordo com o caso.
'''
n1 = int(input())
n2 = int(input())

if n1>n2:
    print('A eh maior')
elif n1<n2:
    print('B eh maior')
else:
    print('iguais')    