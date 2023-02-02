homem = 0
mulher_menor20 = 0
mais18_anos = 0
usuario = 0
while True:
    cadastro = input('Deseja se cadastrar? [S/N]').upper().strip()
    if cadastro == 'S':
        usuario += 1
    else:
        print('\033[1;31mEncerrando programa...\033[m')
        break
    idade = int(input('Idade:'))
    sexo = input('Sexo: [M/F]').upper().strip()[0]
    if idade > 18:
        mais18_anos += 1
    if sexo == 'M':
        homem += 1
    if sexo == 'F' and idade < 20:
        mulher_menor20 += 1
    pergunta = input('Deseja continuar? [S/N]').upper().strip()[0]
    if pergunta == 'N':
        break
    else:
        continue
print(f'Foram cadastradas {usuario} usuários') 
print(f'Foram cadastradas {mais18_anos} usuário com mais de 18 anos. ')
print(f'Foram cadastrados {homem} homens.')
print(f'Foram cadastradas {mulher_menor20} mulheres com menos de 20 anos.')

