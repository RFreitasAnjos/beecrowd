A, B, MaiorAB = input().split()

A = int(A)
B = int(B)
MaiorAB = int(MaiorAB)

verifica=(A+B+abs(A-B))/2

if MaiorAB > verifica:
    print(f'{MaiorAB:.0f} eh o maior')
else:
    print(f'{verifica:.0f} eh o maior')
