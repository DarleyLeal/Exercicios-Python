somaidade = 0
mediaidade = 0
maioridadehomem = 0
nomevelho = ''
mulher_menor20= 0
for p in range(1, 5):
    print('-----{}ª PESSOA -----'.format(p))
    nome = input('Nome: ').strip().upper()
    idade = int(input('Idade:'))
    sexo = input('Sexo: [M/F]').strip().upper()
    somaidade += 1
    if p == 1 and sexo in 'M':
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'M' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    if sexo == 'F' and idade < 20:
        mulher_menor20 += 1
mediaidade = somaidade / 4
print('A média de idade do grupo é de {} anos'.format(mediaidade))
print('O homem mais velho tem {} anos e se chama {}'.format(maioridadehomem, nomevelho))
print('Ao todo {} mulheres tem menos de 20 anos'.format(mulher_menor20))
