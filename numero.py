cont = 0
soma = 0
num = 0
num = int(input('Digite um número: [999 para encerrar]'))
while num != 999:
    if num == '999':
        print('\033[1;33mENCERRANDO PROGRAMA...\033[m')
        break
    else:
        soma += num
        cont += 1
num = int(input('Digite um número: [999 para encerrar]'))
print('{} números foram digitados e a soma entre eles foi de {}'.format(cont, soma))

