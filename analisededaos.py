num =   ( 
        int(input('Digite um número:')),
        int(input('Digite um número:')),
        int(input('Digite um número:')),
        int(input('Digite um número:'))
        )
print(f'\033[1;31mVocê digitou os números {num}\033[m')
print(f'O número 9 aparece {num.count(9)} vezes')
if 3 in num:
    print(f'O número 3 apareceu na {num.index(3) + 1}ª posição')
else:
    print('O valor 3 não foi encontrado na Tupla')
for v in num:
    if v % 2 == 0:
        print(f'O valor {v} \033[1;34mé par\033[m ')
    else:
        print(f'O valor {v} \033[1;34mé ímpar\033[m')



