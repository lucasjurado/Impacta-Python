'''
Descrição
Imagine que você fora contratado para fazer um programa para uma loja de tintas, com o objetivo de calcular quantas latas de tinta são necessárias para pintar uma determinada área e calcular o preço final da compra.

A loja trabalha com latas de tinta de:
24 litros, vendidas a R$91,00 cada e,
5.4 litros, vendidas a R$23,00 cada.
Sabe-se ainda que cada litro de tinta cobre uma superfície de 7 metros quadrados.

Faça um programa que receba o valor da área a ser pintada em metros quadrados, calcule e imprima:
a) A quantidade de latas de tinta e o preço final, considerando apenas latas de 24 litros.
b) A quantidade de latas de tinta e o preço final, considerando apenas latas de 5.4 litros.
c) A quantidade de latas de tinta e o preço final, considerando ambas as latas, de 24 e 5.4 litros.

Formato de entrada
A entrada será um número real positivo não nulo, não deve ser impresso nenhum texto para pedir os dados de entrada.

Formato de saída
A saída deverá ser impressa conforme o exemplo abaixo:

a) 2 lata(s) de 24 litros: R$ 182.00
b) 6 lata(s) de 5.4 litros: R$ 138.00
c) 1 lata(s) de 24 litros e 1 lata(s) de 5.4 litros: R$ 114.00
Com o número de latas impresso como número inteiro e o custo final impresso com duas casas decimais.

Dicas:
Usem as funções math.ceil(n) e math.floor(n) para arredondar os números para os inteiros acima e abaixo de n, respectivamente.
Usem o método str.format() para formatar a string e definir o número de casas decimais dos números a serem impressos.
'''

import math

area_total = float(input())

lg_area = 24.0*7
lp_area = 5.4*7

lg_preco = 91.00
lp_preco = 23.00

lg_compra = math.ceil(area_total/lg_area)
lp_compra = math.ceil(area_total/lp_area)

mix1 = area_total//lg_area
arealp = area_total%lg_area
mix2 = math.ceil(arealp/lp_area)

print('a) {} lata(s) de 24 litros: R$ {:.2f}'.format(lg_compra,lg_compra*lg_preco))
print('b) {} lata(s) de 5.4 litros: R$ {:.2f}'.format(lp_compra,lp_compra*lp_preco))
print('c) {:.0f} lata(s) de 24 litros e {:.0f} lata(s) de 5.4 litros: R$ {:.2f}'.format(mix1,mix2,(mix1*lg_preco+mix2*lp_preco)))
