intervalo = float(input())

if intervalo == 25:
    print(f'Intervalo [0,25]')
elif intervalo >= 25 and intervalo <= 50:
    intervalo1 = intervalo * 2
    print(f'Intervalo ({intervalo:.0f},{intervalo1:.0f}]')
elif intervalo >= 75 and intervalo <= 100:
    intervalo1 = intervalo - 25
    print(f'Intervalo ({intervalo1:.0f},{intervalo:.0f}]')
else:
    print('Fora de intervalo')
