#93. receber um núm. e mostra sua raiz quadrada caso ele seja positivo e o
#quadrado do número caso ele seja negaivo.
import math
n = float(input("Insira o Número Desejado: "))
if (n < 0):
  r = math.sqrt(n)
  print(f'Raiz: {r}.')
elif (n > 0):
  q = n ** 2
  print(f'Quadrado: {q}.')
else:
  print('Número igual a 0? Nananinanão!')
print('by SH4RKVICC!')