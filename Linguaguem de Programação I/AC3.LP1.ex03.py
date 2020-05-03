'''
Escreva um programa em Python 3 para somar os n primeiros termos da seguinte série:

(IMAGEM)

DICA: Aqui todas as frações são somadas, mas como calcular o denominador? Tente primeiro fazer a exibição apenas dos denominadores.

Os denominaores são: 1, 4, 9, 16, 25, 36, .... qual a relação entre eles e a posição dos números?

Compare com a posição: 1, 2, 3, 4, 5, 6, ....
'''

n = int(input())
s1 = 1

for c in range(2,n+1):
    s1 += 1/(c**2)

print('{:.6f}'.format(round(s1,6)))