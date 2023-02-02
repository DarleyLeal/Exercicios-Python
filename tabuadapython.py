'''cont = 1
while True:
    num = int(input('Quer ver a tabuada de qual valor?'))
    num2 = int(input('Digite um número:'))
    op = input('\033[1;33mOperações:\n+ = Adição\n* = Multiplição\n/ = Divisão\n- = Subtração\033[m')
    if num <= 0:
        print('\033[1;31mEncerrando programa, volte sempre\033[m')
        break
    if op == '*':
        for i in range(10):
            print(f'{num} x {num2} = {num * (num2 + cont)}')
            cont += 1
    elif op == '+':
        for i in range(10):
            print(f'{num} + {cont} = {num + cont}')
            cont += 1
    elif op == '/':
        for i in range(10):
            print(f'{num} x {cont} = {num / cont}')
            cont += 1
    elif op == '-':
        for i in range(10):
            print(f'{num} x {cont} = {num - cont}')
            cont += 1
'''