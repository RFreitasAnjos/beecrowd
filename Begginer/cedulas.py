n = int(input())

print(n)

cedula100 = n //100
n %=100
cedula50 = n //50
n %=50
cedula20 = n //20
n %=20
cedula10 = n //10
n %=10
cedula5 = n //5
n %=5
cedula2 = n //2
n %=2
cedula1 = n //1
n %=1


print(f'{cedula100:.0f} nota(s) de R$ 100,00')
print(f'{cedula50:.0f} nota(s) de R$ 50,00')
print(f'{cedula20:.0f} nota(s) de R$ 20,00')
print(f'{cedula10:.0f} nota(s) de R$ 10,00')
print(f'{cedula5:.0f} nota(s) de R$ 5,00')
print(f'{cedula2:.0f} nota(s) de R$ 2,00')
print(f'{cedula1:.0f} nota(s) de R$ 1,00')
