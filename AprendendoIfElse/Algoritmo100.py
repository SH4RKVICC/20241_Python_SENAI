#100. receber um número inteiro de 4 casas e mostrar se é ou não múltiplo de quatro
#o número formado pelos algarismos que estão nas casas das unidades de milhar e
#das centenas.
n = int(input("Insira Um Número Inteiro de 4 Dígitos: "))
c = n / 100
if (n % 4 == 0):
  print(f'O número é múltiplo de 4! Aqui está: {c}.')
else:
  print(f'O número não é múltiplo de 4: {c}')
print("Fim! By SH4RKVICC!")