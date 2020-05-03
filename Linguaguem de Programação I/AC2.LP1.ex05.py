'''
Descrição
Na empresa em que você trabalha há muitos funcionários, e às vezes o depósito do INSS é feito incorretamente para alguns deles pois é um processo manual e portanto sujeito a erros. Com isso você decidiu propor a automação de tal processo, para torná-lo mais rápido e reduzir a chance de erros. Escreva um programa que receba o salário base de um funcionário e calcule qual a contribuição devida ao INSS, dada de acordo com a seguinte tabela:

(IMAGEM)

Lembrando que esta tabela define um teto para o salário considerado, portanto salários maiores que o salário máximo serão descontados de um valor fixo e igual a 11% do valor do teto.

Formato de entrada
A entrada será um número real, representando o salário base do funcinário.

Formato de saída
A saída deverá ser apresentada no seguinte formato:

Desconto do INSS: R$ 120.00
Onde 120.00 é o valor da contribuição calculado para um salário de 1500.00 reais
'''

salario = float(input())

r1 = 1751.81
r2 = 1751.82
r3 = 2919.72
r4 = 2919.73
r5 = 5839.45

f1=0
f2=0
f3=0
f4=0

if salario <= r1:
    f1 = salario * 0.08
elif r2 <= salario <= r3:
    f2 = salario * 0.09
elif r4 <= salario <= r5:
    f3 = salario * 0.11
else:
    f4 = r5 * 0.11
soma = (f1+f2+f3+f4)

print(f'Desconto do INSS: R$ {soma:.2f}')