# Programa 035 - Identifica se cálculo das retas podem formar um triângulo
print('=' * 180)
print(' ' * 75, 'ANALISADOR DE TRIÂNGULOS: ')
print('=' * 180)
lado1 = float(input('Digite o primeiro comprimento:'))
lado2 = float(input('Digite o segundo comprimento :'))
lado3 = float(input('Digite o terceiro comprimento:'))
if lado1 < lado2 + lado3 and lado2 < lado1 + lado3 and lado3 < lado1 + lado2:
    print('Os segmentos podem formar um Triângulo')
    if lado1 == lado2 == lado3:
        print('O Triângulo é Equiátero')
    elif lado1 != lado2 != lado3 != lado1:
        print('O Triângulo é Escaleno')
    else:
        print('O Triângulo é Isósceles')
else:
    print('Os seguimentos não podem formar um triângulo')
