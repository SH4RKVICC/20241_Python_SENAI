#117. Receber três números e armazenar o maior numero na variavel de nome maior
# (suponha números diferentes).

a = float(input("Insira o primeiro núm.: "))
b = float(input("Insira o segundo núm.: "))
c = float(input("Insira o terceiro núm.: "))

if (a > b):
    maior = a
else:
    maior = b
if (c > maior):
    maior = c
print(f'Maior: {maior}.')
print("Fim! For SH4RKVICC!")