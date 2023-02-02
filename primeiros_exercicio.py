soma = 0
qtd = 0
while True:
    num = int(input('Digite um número: [999 para sair]'))
    if num == 999:
        break
    soma += num
    qtd += 1
print(f"Foram digitados {qtd} números")
print(f'A soma dos números é {soma}')
