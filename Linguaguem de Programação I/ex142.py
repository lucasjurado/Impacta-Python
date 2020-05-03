import random
print('<<<<<<<<< Jokenpô >>>>>>>>>')

#variavel recebe o nome do jogador
nome = str(input('Qual é o seu nome? '))

#contador do número de jogos
c = 0
#contador das vitórias do pc
pcWin = 0
#contador das vitórias do jogador
playerWin = 0
#contador de empates
draw = 0

while True:
    #variável recebe a opção do jogador de acordo com a sua referencia(0,1,2)
    num = int(input('''Suas opções:
    [0] Pedra
    [1] Papel
    [2] Tesoura
    Qual é a sua jogada? '''))

    #se o valor da variável for diferente das apresentadas, o programa pede novamente para digitá-la
    if num != 0 and num != 1 and num != 2:
        print('Opção inválida! Tente novamente')
        print('-=' * 20)
    else:
        print('-='*20)

        #o computador escolhe uma das opções randomizadas dentro da lista
        lista = ('Pedra','Papel','Tesoura')
        pc = random.choice(lista)
        p1 = lista[num]

        print(f'{nome} [{p1}] X [{pc}] Computador')

        #sequencia lógica que define o vencedor e o atribui 1 ponto no caso de vitória
        if pc == p1:
            print('> Empate!')
            draw += 1
        elif pc == 'Pedra' and p1 == 'Papel' or pc == 'Papel' and p1 == 'Tesoura' or pc == 'Tesoura' and p1 == 'Pedra':
            print(f'> {nome}, você venceu!')
            playerWin += 1
        else:
            print(f'> {nome}, você perdeu!')
            pcWin += 1
        print('-=' * 20)

        #contador de jogos recebe mais 1 e caso o seu total seja multiplo de 5, é perguntado se deseja continuar o jogo
        c+=1
        if c%5==0:
            while True:
                again = str(input('Você quer continuar [S/N]? ')).upper().strip()[0]
                print('-=' * 20)
                if again in 'SN':
                    if again in 'N':
                        print(f'<Depois de {c} jogos> Placar final: {nome} {playerWin} x {pcWin} Computador. E {draw} empates.')
                        exit()
                    elif again in 'S':
                        break
                else:
                    print('Opção inválida! Tente novamente.')



