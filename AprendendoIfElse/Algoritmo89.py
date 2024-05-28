#89. Seu peso em outro planeta!

print("Planetas Disponiveis Para Análise")
print("1. Mercurio.\n2. Vênus.\n3. Marte.\n4. Jupiter.\n5. Saturno.\n6. Urano")
ps = input('Selecione o Planeta: ')
pt = float(input('Insira seu peso no planeta Terra: '))

if (ps == '1'):
  pf = (pt/10)*0.37

elif (ps == '2'):
  pf = (pt/10)*0.88

elif (ps == '3'):
  pf = (pt/10)*0.38

elif (ps == '4'):
  pf = (pt/10)*2.64

elif (ps == '5'):
  pf = (pt/10)*1.15

elif (ps == '6'):
  pf = (pt/10)*1.17

else:
  print('Esse Planeta não é uma opção.')
print(f'Seu peso nesse planeta é: {pf}')
print('By SH4RKVICC!')