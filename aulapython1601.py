#metoo sniper
'''Feitas as correções de calendário, definiu-se a nova regra
para o cálculo dos anos bissextos: De 4 em 4 anos é ano bissexto. De 100 em 100 anos não é ano
bissexto. De 400 em 400 anos é ano bissexto. Prevalecem as últimas regras sobre as primeiras.'''
# Programa calcula se ano digitado é ou não bissxeto
from datetime import date
ano = int(input('Digite um ano: (0 para ano atual) '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 or ano % 400 == 0 or ano != 100 == 0:
    print('O ano {} é BISSEXTO'.format(ano))
else:
    print('O ano {} não é BISSEXTO'.format(ano))
