'''
Descrição
Escreva um programa em Python3 que peça o valor do lado de um hexágono regular, calcule e imprima sua área e seu perímetro.
Sabemos que um hexágono regular é o polígono de 6 lados iguais e com todos os ângulos internos iguais entre si.

Formato de entrada
A entrada poderá ser qualquer número real positivo.

Formato de saída
A saída deverá ser formatada conforme o exemplo a seguir:

Lado do hexagono: <valor1> metros,
Area: <valor2> metros quadrados,
Perimetro: <valor3> metros.
Sendo valor 1, 2 e 3 respectivamente os valores do lado, da área e do perímetro do hexágono.

Dica: Usem um print() para cada linha da resposta, não usem o '\n'.
'''

import math

L = float(input())

A = 6*(math.pow(L,2)*math.pow(3,1/2))/4

print('Lado do hexagono: {:.1f} metros,'.format(L))
print('Area: {} metros quadrados,'.format(A))
print('Perimetro: {:.1f} metros.'.format(6*L))