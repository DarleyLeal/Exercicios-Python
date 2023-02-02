print('-' * 47)
print('{:-^57}'.format('\033[1;31mLISTAGEM DE PREÇO\033[m'))
print('-'* 47)
listagem = (
            'Lápis', 1.75,
            'Borracha', 2.00,
            'Caderno', 15.90,
            'Estojo', 25.00,
            'Transferidor', 4.20,
            'Compasso', 9.99,
            'Mochila', 120.32,
            'Compasso', 22.30,
            'Canetas', 22.30,
            'Livros', 34.90
            )
for pos in range(0, len(listagem)):
    if pos % 2 == 0:
        print(f'{listagem[pos]:.<30} R$  {listagem[pos + 1]:>7.2f}')

