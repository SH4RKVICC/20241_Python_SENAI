# 116. Entrar com três números e imprimir o maior número (suponha números diferentes).

n1 = float(input("Insira o primeiro núm.: "))
n2 = float(input("Insira o segundo núm.: "))
n3 = float(input("Insira o terceiro núm.: "))

if (n1 != n2 and n1 != n3 and n2 != n3):
    if (n1 > n2 and n1 > n3): 
        print(f'O maior valor é {n1}.')
    elif (n2 > n1 and n2 > n3): 
        print(f'O maior valor é {n2}.')
    else:
        print(f'O maior valor é {n3}.')
else:
    print('Os números são iguais!')
print("Fim! For SH4RKVICC!")

