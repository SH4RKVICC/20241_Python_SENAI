#106. Receber nome e mostra-lo se o primeiro caractere for a letra A (considerar
# letra minúscula ou maiúscula).

n = input("Insira seu nome: ")
pl = n[0].lower() == 'a'
if (pl == True):
  print(f'Seu nome é {n} e começa com a letra A!')
else:
  print('Seu nome NÃO começa com a letra A!')
print("Fim! For SH4RKVICC!")