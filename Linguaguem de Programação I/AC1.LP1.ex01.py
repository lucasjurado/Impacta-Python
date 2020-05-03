'''
Descrição
Escreva um programa em Python3 que receba quatro números reais (a, b, c, d) e reproduza as seguintes expressões algébricas:

Formato de entrada
As entradas poderão ser quaisquer números reais, positivos ou negativos mas não nulos.
Não imprima nenhum texto para pedir os dados de entrada.

Formato de saída
A saída deve conter o número do item e o valor calculado arredondado para a 4a. casa de precisão, para todos os itens.

Para arredondar um número em Python3 usamos a função: 
round(n, d)
Que retorna o valor de n arredondado para d casas após a vírgula. Se d for omitido, é feito o arredondamento para um número inteiro.

Obs.: Essa função não faz parte do módulo de matemática, podendo ser acessada diretamente.
'''


import math

a= float(input())
b= float(input())
c= float(input())
d= float(input())

list=[a,b,c,d]

e1 = (((a**2)+(3*b))/c)+d
e12 = round(e1,4)

e2 = math.log10(a) + math.e ** (-b/c) - ((d**2)/math.pi)
e22 = round(e2,4)

e3 = ((math.pow(a,2/3))*(math.pow(b,1/3)) + (c*d))/(a+b+c+d)
e33 = round(e3,4)

e4 = (a+b)*(c+d)/(a*b*c*d)
e44 = round(e4,4)

e5 = (((a**2)+(b**2))/(c*d)) - (((c**2)+(d**2))/(a*b))
e55 = round(e5,4)

e6 = sum(list)**2
e66 = round(e6,4)

e7 = math.pow(a,2)+math.pow(b,2)+math.pow(c,2)+math.pow(d,2)
e77 = round(e7,4)

e8 = math.pow((a*b*c*d),1/3)
e88 = round(e8,4)

print(f'i) {e12}')
print(f'ii) {e22}')
print(f'iii) {e33}')
print(f'iv) {e44}')
print(f'v) {e55}')
print(f'vi) {e66}')
print(f'vii) {e77}')
print(f'viii) {e88}')