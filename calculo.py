menu = 0
while menu != 5:
    valor1 = int(input('Digite um valor: '))
    valor2 = int(input('Digite outro valor: '))
    menu = input('Escolha uma opção:\n1 - Somar\n2 - Multiplicar\n3 - Maior\n4 - Exponenciação\n5 - Sair do programa')
    if menu == '1':
        soma = valor1 + valor2
        print('A soma entre {} + {} é {}'.format(valor1, valor2, soma))
    elif menu == '2':
        mulltiplicacao = valor1 * valor2
        print('A multiplicação entre {} * {} é {}'.format(valor1, valor2, mulltiplicacao))
    elif menu == '3':
        maior = max(valor1, valor2)
        menor = min(valor1, valor2)
        print('O maior valor é {} e o menor {}'.format(maior, menor))
    elif menu == '4':
        print('\033[1;34mO primeiro valor será elevado ao segundo:')
        exponenciacao = valor1 ** valor2
        print('{} elevado a {} é {}'.format(valor1, valor2, exponenciacao))
    elif menu == '5':
        print('\33[1;34mSaindo do programa...')
        break
    else:
        print('Opção inválida, tente novamente!')
print('=*=' * 30)
print('Fim do programa, volte sempre!')


