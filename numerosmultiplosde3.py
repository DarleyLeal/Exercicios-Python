n = 0
cont = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        cont += 1
        n += c
print('A soma dos números é {}, {} números impares divisiveis por 3'.format(n, cont,  end=' '))