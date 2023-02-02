from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0,2)
print('Suas Opções:\n0 - Pedra\n1 - Papel\n2 - Tesoura')
jogador = int(input('Qual é a sua jogada? '))
print('\033[1;33mJO')
sleep(1)
print('\033[1;34mKEN')
sleep(1)
print('\033[1;35mPO')
sleep(1)
print('\033[1;33m=' * 40)
print('\033[0;32mO computador escolheu {}'.format(itens[computador]))
print('\033[0;36mO jogador escolheu {}'.format(itens[jogador]))
print('\033[1;33m=' * 40)
if computador == 0:
    if jogador == 0:
        print('EMPATE')
    elif jogador == 1:
        print('JOGADOR VANCE')
    elif jogador == 2:
        print('COMPUTADOR VENCE')
    else:
        print('Opção inválida')
elif computador == 1:
    if jogador == 0:
        print('COMPUTADOR VENCE')
    elif jogador == 1:
        print('EMPATE')
    elif jogador == 2:
        print('JOGADOR VENCE')
    else:
        print('Opção inválida')
elif computador == 2:
    if jogador == 0:
        print('JOGADOR VENCE')
    elif jogador == 1:
        print('COMPUTADOR VANCE')
    elif jogador == 2:
        print('EMPATE')
    else:
        print('Opção inválida')
