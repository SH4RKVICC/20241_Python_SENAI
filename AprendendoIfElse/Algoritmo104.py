#104. Receber nome, sexo e idade de uma pessoa. Se a pessoa for do sexo feminino e
#tiver menos que 25 anos, mostrar nome e a mensagem: ACEITA. Caso contrário,
#nome nome e a mensagem: NÃO ACEITA. (Considerar f ou F.)

n = input("Insira seu nome: ")
s = input("Insira seu sexo: ")
i = int(input("Insira sua idade: "))
if (i >= 25 and s == 'f' or s == 'F'):
  print(f'{n}, ACEITA!')
else:
  print(f'{n}, NÃO ACEITA!')
print("Fim! By SH4RKVICC!")