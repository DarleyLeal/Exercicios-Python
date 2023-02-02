campeonato_brasileiro = (   
                            'Palmeiras', 'Internacional','Fluminense','Corinthians',
                            'Flamengo','Atlético Paranaense', 'Atlético Mineiro', 'Fortaleza', 
                            'São Paulo','América', 'Botafogo', 'Santos', 'Goiás', 'Bragantino', 
                            'Coritiba', 'Cuiabá', 'AC Goianiense', 'Avaí','Juventude'
                        )
print(f'\033[1;33mCinco primeiros colocados: {campeonato_brasileiro}\033[m')
print('=' * 45)
print(f'\033[1;31mÚltimos cinco colocados: {campeonato_brasileiro[15:]}\033[m')
print('=' * 45)
print(f'\033[1;35mTimes em ordem alfabética: {sorted(campeonato_brasileiro)}\033[m')
print('=' * 45)
print(f'Coritiba está na {campeonato_brasileiro.index("Coritiba") + 1}ª posição')