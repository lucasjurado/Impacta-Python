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