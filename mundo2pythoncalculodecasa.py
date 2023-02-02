valorCasa = float(input('Valor da casa: R$'))
salario = float(input('Salário comprador:'))
anos = int(input('Anos de financiamento:'))
validacaoCompra = (salario * 0.3)
prestacaoMensal = (valorCasa / (anos * 12))
if prestacaoMensal > validacaoCompra:
    print('Empréstimo Negado!')
    print('A sua prestação mensal seria R${:.2f} e esse valor ultrapassa 30% do seu salário,  que é R${} '.format(prestacaoMensal, validacaoCompra))
else:
    print('Empréstimo Aprovado!')
    print('A sua prestação mensal será R${:.2f} em {} vezes'.format(prestacaoMensal, anos))