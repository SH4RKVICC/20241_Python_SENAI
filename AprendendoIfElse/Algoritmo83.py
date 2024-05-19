#83 receber núm. e se ele for positivo emitir seu inverso,
#caso contrario emitir o valor absoluto do núm;
n = int(input('Insira o núm. inteiro desejado: '))
if (n < 0):
    a = abs(n)
    print(f'Absoluto: {a}')
else:
    i = 1 / n
    print(f'Inverso: {i}')
print("FROM SH4RKVICC")