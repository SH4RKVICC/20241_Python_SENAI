#78.dado um poligono convexo de n lados, podemos calcular o num. de diagonais
#desse poligno pela formula nd = n (n - 3) /2. Ler quandos lados tem o poligono,
#calcular e escrever o num. de diagonais diferentes
nl = int(input('Insira o num. de lados do poligono:'))
nd = nl * (nl - 3) / 2
print(f'Num. de Diagonais: {nd:.0f}.')
print("FROM SH4RKVICC")