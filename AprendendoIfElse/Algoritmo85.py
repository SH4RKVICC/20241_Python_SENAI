#85. descubra!
a = float(input('Insira o primeiro número: '))
b = float(input('Insira o segundo número: '))
c = float(input('Insira o terceiro número: '))
if (a > b):
    if (a > c):
        max = a
    else:
        max = c
else:
    if (b > c):
        max = b
    else:
        max = c
print(f'Max: {max:.2f}')
print("FROM SH4RKVICC")