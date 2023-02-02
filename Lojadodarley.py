print('{:=^90}'.format('DARLEY STORE'))
valor_produto = float(input('Valor do produto: R$'))
print('1 - À vista dinheiro ou cheque\n2 - À vista no cartão\n3 - Em até 3x no cartão\n4 - Em 3x ou mais')
condicao_pagamento = int(input('Escolha uma forma de pagamento:'))
if condicao_pagamento == 1:
    print('Valor a pagar com 10% de desconto R${:.2f}'.format(valor_produto - (valor_produto * 0.1)))
elif condicao_pagamento == 2:
    print('Valor a pagar com 5% de desconto R${:.2f}'.format(valor_produto - (valor_produto * 0.05)))
elif condicao_pagamento == 3:
    print('A compra será parcelada em 2x, valor a pagar R${:.2f}'.format(valor_produto / 2))
elif condicao_pagamento == 4:
    vezes = int(input('Em quantas vezes você quer dividir?'))
    print('O valor a pagar será R${:.2f} com 20% de Juros'.format((valor_produto / vezes) + (valor_produto * 0.2) ))
else:
    print('\033[0;33mOPÇÃO INVÁLIDA, TENTE NOVAMENTE!')

