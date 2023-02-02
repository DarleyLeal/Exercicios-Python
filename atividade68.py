from random import randint
vitoria = 0
while True:
    jogador = int(input('Digite um número:'))
    computador = randint(0, 10)
    total = jogador + computador
    tipo = ''
    while tipo not in 'PI':
        tipo = input('Par ou Impar? [P/I]').upper().strip()[0]
    print(f'Você jogou {jogador} e o computador jogou {computador}. Total: {total}.')
    print('Deu Par' if total % 2 == 0 else 'Deu impar' )
    if tipo == 'P':
        if total  % 2 == 0:
            print('Você Venceu!')
            vitoria += 1
        else:
            print('Você perdeu!')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('Você Venceu')
            vitoria += 1
        else:
            print('Você perdeu!')
            break
    print('Vamos jogar novamente...')
print(f'Game over! Você venceu {vitoria} vezes.')



