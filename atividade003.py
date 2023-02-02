from datetime import date
ano_de_nascimento = int(input('Ano de nascimento:'))
ano_atual = date.today().year
idade = ano_atual - ano_de_nascimento
if idade <= 9:
    print('Você é um nadador Mirim e tem {} anos.'.format(idade))
elif idade <= 14:
    print('Você é um nadador Infantil e tem {} anos.'.format(idade))
elif idade <= 19:
    print('Você é um nadador Junior e tem {} anos.'.format(idade))
elif idade <= 25:
    print('Você é um nadador Sênior e tem {} anos.'.format(idade))
else:
    print('Você é um nadador Master e tem {} anos.'.format(idade))
