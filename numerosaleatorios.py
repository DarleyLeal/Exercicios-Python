from random import randint
num =  (randint(1, 10), randint(1, 10), 
        randint(1, 10),
        randint(1, 10), randint(1, 10))
print(f'Os valores sorteados foram {num}', end='')
print(f'\nO maior número é {max(num)}\nE o menor é {min(num)}')