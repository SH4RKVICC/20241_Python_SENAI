#107. Entrar com o nome de uma pessoa e so imprimi-lo se o prenome for JOSE.

n = input("Insira seu nome: ")
nd = n.split()[0]
if (nd == 'jose' or nd == 'JOSE'):
  print(f'Seu nome é {n}!')
else:
  print('Seu prenome NÃO começa com Jose!')
print("Fim! For SH4RKVICC!")