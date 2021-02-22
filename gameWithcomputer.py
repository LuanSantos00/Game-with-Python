from random import randint

print('-'*40)
print('Vamos iniciar o jogo. \n\n Para sair digite: -1')
print('-'*40)

while True:
    print('-=-'*20)
    print('Vou pensar em um número entre 0 e 5. Tente advinhar......')
    print('-=-'*20)
    computador = randint(0,5)
    jogador = int(input('Em que número eu pensei ? '))
    if jogador < 0: 
        print('JOGO FINALIZADO!') 
        break
    else:
        if(jogador == computador):
            print('PARABÉNS! Você acertou')
            break
        elif(jogador > computador):
            print('Você Exagerou!O valor que eu pensei é menor!')
        else:
            print('EU GANHEI!\nVocê errou, eu pensei no {} e não no {}'.format(computador,jogador))


