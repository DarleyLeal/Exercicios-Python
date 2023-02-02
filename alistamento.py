from datetime import date
sexo = input('Digite seu sexo: M / F').upper()
if sexo == 'F':
    print('Você não precisa se alistar!')
anoNascimento = int(input('Ano de Nascimento:'))
anoAtual = date.today().year
idade = (anoAtual - anoNascimento)
if idade < 18:
    print('Você tem {} anos e falta {} anos para o seu alistamento.'.format(idade, (18 - idade)))
    print('O seu alistatamento será no ano {}'.format(anoAtual + (idade - 18)))
elif idade == 18:
    print('Você tem 18 anos e deve se alistar IMEDIATAMENTE!')
elif idade > 18:
    print('Você tem {} anos e seu alistamento foi há {} anos'.format(idade, idade - 18 ))
    print('O seu alistatamento foi no ano {}'.format(anoAtual - (idade - 18)))



