soma = 0
qtd = 0
maior = menor = 0
pergunta = 'Ss'
while pergunta in 'Ss':
    num = int(input('Digite um número: '))
    soma += num
    qtd += 1
    if qtd == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    pergunta = input('Deseja continuar? [S/N]').upper().strip()[0]
    if pergunta == 'S':
        continue
    else:
        break
print('Maior número :{}\nMenor número: {}'.format(maior, menor))
print('Média dos valores: {}'.format(soma / qtd))
