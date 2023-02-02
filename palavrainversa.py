frase = input('Digite uma frase').upper().strip()
palavra = frase.split()
junto = ''.join(palavra)
if frase[::-1] == junto:
    print('Palídromo')
else:
    print('Não é palídromo')
print('O inverso da frase {} é {}'.format(frase, frase[::-1]))