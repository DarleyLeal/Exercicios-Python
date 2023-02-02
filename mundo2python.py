valorCasa = float(input('Qual o valor da casa? R$'))
salario = float(input('Qual o valor do seu salário?'))
qtdMeses = int(input('Em quantos meses você quer pagar?'))

validacaoCompra = (salario * 0.3)
prestacaoMensal = (valorCasa / qtdMeses)
if prestacaoMensal > validacaoCompra:
    print('Empréstimo Negado!')
    print('A sua prestação mensal seria R${:.2f} e esse valor ultrapassa 30% do seu salário, R${} '.format(prestacaoMensal, validacaoCompra))
else:
    print('Empréstimo Aprovado!')
    print('A sua prestação mensal será R${:.2f} em {} vezes'.format(prestacaoMensal, qtdMeses))