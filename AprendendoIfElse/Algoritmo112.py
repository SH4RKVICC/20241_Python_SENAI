# 112. Receber dois números e mostrar o menor numero (suponha números diferentes).

n1 = float(input("Insira o primeiro núm.: "))
n2 = float(input("Insira o segundo núm.: "))
if (n1 > n2):
  print(f'O menor número é {n2}.')
elif (n1 < n2):
    print(f'O menor número é {n1}')
else:
  print(f'Os números são iguais!')
print("Fim! For SH4RKVICC!")