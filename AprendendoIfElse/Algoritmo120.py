# 120. Entrar com três números e armazená-los em três variáveis com os seguintes no-
# mes maior, intermediário e menor (suponha numeros diferentes)

a = float(input("Insira o primeiro núm.: "))
b = float(input("Insira o segundo núm.: "))
c = float(input("Insira o terceiro núm.: "))

if (a != b and a != c and b != c):
    if (a > b and a > c):
        maior = a
        if (b > c):
            intermediario = b
            menor = c
        else:
            intermediario = c
            menor = b            
    elif (b > a and b > c):
        maior = b
        if (a > c):
            intermediario = a
            menor = c
        else:
            intermediario = c
            menor = a     
    elif (c > a and c > b):
        maior = c
        if (a > b):
            intermediario = a
            menor = b
        else:
            intermediario = b
            menor = a   
    print(f'Maior: {maior}.\nIntermediario: {intermediario}.\nMenor: {menor}.')
else:
    print('Os valores são iguais!')
print("Fim! For SH4RKVICC!")