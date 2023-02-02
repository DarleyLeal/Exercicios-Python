from datetime import date
menor_idade = 0
maior_idade = 0
for c in range(7):
    ano = int(input('Ano de nascimento: '))
    ano_atual = (date.today().year - ano)
    if ano_atual < 18:
        menor_idade += 1
    else:
        maior_idade += 1
print('{} pessoas são menores de idade'.format(menor_idade))
print('{} pessoas são maiores de idade'.format(maior_idade))

