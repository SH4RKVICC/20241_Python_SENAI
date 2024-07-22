# 123. Ler três números, os possíveis lados de um triângulo, e imprimira classificação
#  segundo os lados.

a = float(input("Insira o primeiro lado do triângulo: "))
b = float(input("Insira o segundo lado do triângulo: "))
c = float(input("Insira o terceiro lado do triângulo: "))

if (a < b + c and b < a + c and c < a + b):
    if (a == b and a == c):
        t = 'Equilatero'
    else:
        if (a == b or a == c or b == c):
            t = 'Isoceles'
        else:
            t = 'Escaleno'
    print(f'Triangulo {t}')
else:
    print('As medidas não formam um triângulo.')