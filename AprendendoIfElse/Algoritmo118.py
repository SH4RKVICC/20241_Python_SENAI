# 118. Entrar com três números e imprimi-los em ordem crescente (suponha números diferentes).

a = float(input("Insira o primeiro núm.: "))
b = float(input("Insira o segundo núm.: "))
c = float(input("Insira o terceiro núm.: "))

if (a != b and a != c and b != c):
    if (a > b):
        aux = a
        a = b
        b = aux
    elif (a > c):
        aux = a
        a = c
        c = aux
    elif (b > c):
        aux = b
        b = c
        c = aux
    print(f'Ordem Crescente: {a}, {b}, {c}.')
else:
    print('Os valores são iguais!')
print("Fim! For SH4RKVICC!")