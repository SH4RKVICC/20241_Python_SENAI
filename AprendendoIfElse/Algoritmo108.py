# 108. Idem ao anterior, porém considerar: JOSÉ, José ou josé.

n = input("Insira seu nome: ")
nd = n.split()[0]
if (nd == 'jose' or nd == 'JOSE' or nd == 'Jose' or nd == 'josé' or nd == 'JOSÉ' or nd == 'José'):
  print(f'Seu nome é {n}!')
else:
  print('Seu prenome NÃO começa com Jose!')
print("Fim! For SH4RKVICC!")