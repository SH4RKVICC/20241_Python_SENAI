# 124. Ler três números, os possíveis lados de um triângulo, e imprimira classificação
# segundo os ângulos.

a = float(input("Insira o primeiro lado do triângulo: "))
b = float(input("Insira o segundo lado do triângulo: "))
c = float(input("Insira o terceiro lado do triângulo: "))

# Verificando se os lados formam um triângulo
if a < b + c and b < a + c and c < a + b:
    # Identificando o maior lado
    if a >= b and a >= c:
        maior = a ** 2
        lados = b ** 2 + c ** 2
    elif b >= a and b >= c:
        maior = b ** 2
        lados = a ** 2 + c ** 2
    else:
        maior = c ** 2
        lados = a ** 2 + b ** 2

    # Classificando o triângulo
    if maior == lados:
        t = 'Retângulo'
    elif maior > lados:
        t = 'Obtusângulo'
    else:
        t = 'Acutângulo'

    print(f'Triângulo {t}')
else:
    print('As medidas não formam um triângulo.')
