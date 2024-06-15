#105. Entrar com a sigla do estado de uma pessoa e imprimir uma das mensagens:
# carioca;
# paulista;
# mineiro;
# outros estados.

s = input("Insira a sigla do seu estado: ")
if (s == 'sp' or s == 'SP'):
  print('Paulista!')
elif (s == 'rj' or s == 'RJ'):
  print('Carioca!')
elif (s == 'mg' or s == 'MG'):
  print('Mineiro!')
elif (s == 'ba' or s == 'BA'):
  print('Baiano!')
elif (s == 'es' or s == 'ES'):
  print('Capixaba!')
else:
  print(f'Você é de outro estado!')
print("Fim! For SH4RKVICC!")