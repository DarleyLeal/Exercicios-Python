peso = float(input('Digite seu peso: KG'))
altura = float(input('Digite sua altura: m'))
imc = peso / (altura ** 2)
if imc < 18.5:
    print('Seu IMC é {:.1f}, você está abaixo do peso'.format(imc))
elif imc < 25:
    print('Seu IMC é {:.1f}, você está no peso ideal'.format(imc))
elif imc < 30:
    print('Seu IMC é {:.1f}, seu peso está acima do ideal'.format(imc))
elif imc < 40:
    print('Seu IMC é {:.1f}, você está com obesidade'.format(imc))
elif imc > 40:
    print('Seu IMC é {:.1f}, você está com obesidade mórbida'.format(imc))