print('\033[1;31mGERADOR DE PROGRESSÃO ARITMÉTICA')
print('\033[1;34m=*=' * 40)
termo = int(input('\033[mPrimeiro termo da PA:'))
razao = int(input('Razão: '))
primeiro_termo = termo
cont = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont <= total :
        print('{} ->'.format(primeiro_termo), end=' ')
        primeiro_termo += razao
        cont += 1
    print('PAUSA...')
    print('Progressão finalizada com {} termos mostrados'.format(total))
    mais = int(input('Quantos termos você deseja mostrar?'))
print('FIM')
