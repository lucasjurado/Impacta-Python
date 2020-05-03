'''
Descrição
Escreva um programa que irá receber duas entradas: uma sequencia de caracteres e um único caractere e irá contar quantas vezes o caractere aparece na sequencia. Você deve escrever uma função que irá receber como parâmetros a sequencia e o caractere, e retornar o número de ocorrências pedido. No código principal do programa, faça a leitura dos dados de entrada (input's), chame a sua função para contar o número de ocorrências, e em seguida imprima o resultado pedido.

OBS: Não é permitido o uso do .count() para realizar a contagem. 

DICA: A ideia é criar uma função que faça a mesma coisa que o .count(), portanto você pode usar o .count() para comparar os seus resultados e validar a sua função. Para fazer a contagem, faça um laço (for ou while) iterando sobre a sequência e criei um contador para guardar quantas vezes o caractere foi encontrado.
'''

def vlr(fr,crt):
    count = 0
    for c in fr:
        if c == crt:
            count+=1
    if count>0:
        print(f'O caractere buscado ocorre {count} vezes na sequencia.')
    else:
        print('Caractere nao encontrado.')

frase = str(input(''))
caract = str(input(''))

vlr(frase,caract)

#FUNÇÃO COUNT
print(frase.count(caract))