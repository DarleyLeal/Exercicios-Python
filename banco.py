print('{:=^50}'.format('\033[1;33mBANCO DARLEY\033[m'))
valor = float(input('Qual valor deseja sacar?'))
ced = 50
total =  valor
total_cedulas = 0
while True:
    if total_cedulas >= ced:
        total_cedulas -= ced
        total_cedulas += 1
    else:
        if total_cedulas > 0:
            print(f'Total de {total_cedulas} de cédulas de R${ced}')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        total_cedulas = 0
        if total == 0:
            break
print('Volte sempre!')

