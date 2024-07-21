# 121. Efetuara leitura de cinco números inteiros diferentes e identificar o maior e o me-
# nor valor.

a = int(input("Insira o primeiro núm. inteiro: "))
b = int(input("Insira o segundo núm. inteiro: "))
c = int(input("Insira o terceiro núm. inteiro: "))
d = int(input("Insira o quarto núm. inteiro: "))
e = int(input("Insira o quinto núm. inteiro: "))

if (a > b and a > c and a > d and a > e):
    print(f'O maior valor é o de A, que equivale a {a}')
elif (b > a and b > c and b > d and b > e):
    print(f'O maior valor é o de B, que equivale a {b}')
elif (c > a and c > b and c > d and c > e):
    print(f'O maior valor é o de B, que equivale a {b}')
elif (b > a and b > c and b > d and b > e):
    print(f'O maior valor é o de C, que equivale a {c}')
elif (d > a and d > b and a > d and d > e):
    print(f'O maior valor é o de D, que equivale a {d}')
else:
    print(f'O maior valor é o de E, que equivale a {e}')
