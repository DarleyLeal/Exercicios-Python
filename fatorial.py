from math import factorial
while True:
    num = int(input('Digite um número para calcular seu fatorial:'))
    fatorial = factorial(num)
    print('A fatorial de {}! é {}!'.format(num, fatorial, end=' '))