# 113. Receber dois números e mostra-los em ordem crescente (suponha números diferentes).

n1 = float(input("Insira o primeiro núm.: "))
n2 = float(input("Insira o segundo núm.: "))
if (n1 > n2):
  print(f'{n2}, {n1}.')
elif (n2 > n1):
    print(f'{n1}, {n2}')
else:
  print(f'Os números são iguais!')
print("Fim! For SH4RKVICC!")