# 122. Ler três números e imprimir se eles podem ou não ser lados de um triângulo.

print('Olá, querido! Vamos descobrir se seu triângulo é valido!')
l1 = float(input("Insira o primeiro lado do triângulo: "))
l2 = float(input("Insira o segundo lado do triângulo: "))
l3 = float(input("Insira o terceiro lado do triângulo: "))


if (l1 + l2 > l3) and (l1 + l3 > l2) and (l2 + l3 > l1):
    print('Seu triângulo é válido!')
else:
     print('Ele NÃO pode ser um triângulo!')