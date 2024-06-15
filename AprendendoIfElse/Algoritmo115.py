# 115. Receber dois números e mostrar o quadrado do menor número e a raiz quadrada do maior número, se for possível.
import math
n1 = float(input("Insira o primeiro núm.: "))
n2 = float(input("Insira o segundo núm.: "))

if (n1 > n2):
    q = math.pow(n2, 2)
    rq = math.sqrt(n1)
    print(f'Quadrado do Menor Núm.: {q}.\nRaiz Quadrada do Maior Núm.: {rq}.')
elif (n2 > n1):
    q = math.pow(n1, 2)
    rq = math.sqrt(n2)
    print(f'Quadrado do Menor Núm.: {q}.\nRaiz Quadrada do Maior Núm.: {rq}.')
else:
  print(f'Os números são iguais!')
print("Fim! For SH4RKVICC!")
