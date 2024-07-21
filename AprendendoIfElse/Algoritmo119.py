# 119. Entrar com três números e imprimi-los em ordem decrescente (suponha números
# diferentes).

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
    print(f'Ordem Descrescente: {c}, {b}, {a}.')
else:
    print('Os valores são iguais!')
print("Fim! For SH4RKVICC!")