'''
Descrição
Escreva um programa em Python3 que receba um número real positivo e não nulo, calcule e imprima o resultado das seguintes operações aritméticas:
(IMAGEM)

Formato de entrada
A entrada será um número real positivo e não nulo. Não imprima nenhum texto para pedir o dado de entrada.

Formato de saída
A saída devera conter a resposta de cada item em uma linha diferente, contendo apenas o número do item e o valor calculado.
'''

import math

n = float(input())

i = n**2
ii = math.pow(n,math.e)
iii = math.pow(n,1/2)
iv = math.pow(n,1/3)
v = math.pow(n,1/n)
vi = math.e*n
vii = math.pi/n
viii = math.log(n,7)
ix = math.log(n,math.e)
x = math.log(n,math.pi)

print(f'i) {i}')
print(f'ii) {ii}')
print(f'iii) {iii}')
print(f'iv) {iv}')
print(f'v) {v}')
print(f'vi) {vi}')
print(f'vii) {vii}')
print(f'viii) {viii}')
print(f'ix) {ix}')
print(f'x) {x}')