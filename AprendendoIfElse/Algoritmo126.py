# 126. Ler um número e imprimir se ele é iguala 5, a 200, a 400, se está no intervalo en-
#tre 500 e 1000, inclusive, ou se ele está fora dos escopos anteriores.

n = int(input('Digite um número: '))

if (n == 5):
    print(f'O número é {n}')
elif (n == 200):
    print(f'O número é {n}')
elif (n == 400):
    print(f'O número é {n}')
elif (n >= 200 and n <= 400):
    print(f'O número está entre 200 e 400')
else:
    print('Fora do Escopo!')
print('BY SH4RKVICC!')