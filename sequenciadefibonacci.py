print('=' * 30)
print('\033[1;31mSEQUÊNCIA DE FIBONACCI\033[m')
print('=' * 30)
n = int(input('Quantos termos devem ser mostrados?'))
termo1 = 0
termo2 = 1
print('~' * 30)
print('{} -> {}'.format(termo1, termo2), end='')
cont = 3
while cont <= n:
    termo3 = termo1 + termo2
    print('-> {}'.format(termo3), end='')
    termo1 = termo2
    termo2 = termo3
    cont += 1
print('-> FIM')