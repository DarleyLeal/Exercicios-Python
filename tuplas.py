extenso = ( 'zero','um', 'dois', 'três', 'quatro',
            'cinco','seis', 'sete', 'oito', 'nove', 
            'dez' ,'onze', 'doze', 'treze',
            'quatorze', 'quinze', 'dezesseis', 'dezessete', 
            'dezoito', 'dezenove', 'vinte')
while True:
    numero = int(input('Digite um número de 0 a 20:'))
    if 0 < numero > 20:
        numero = int(input('Tente novamente. Digite um número entre 0 e 20:'))
        continue
    procura = extenso[numero]
    print(f'Você digitou o número: {procura}')