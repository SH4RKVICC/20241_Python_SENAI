#103. Receber ano de nascimento de uma pessoa e o ano atual.
# Mostrar idade da pessoa. Não se esqueça de verificar se o ano de
# nascimento é um ano válido.

an = int(input('Insira seu ano de nascimento: '))
aa = int(input('Insira o ano atual: '))
i = aa - an
if (an > aa):
  print(f'Esse ano não é valido!')
else:
  print(f'Sua idade é {i} anos!')
print("Fim! By SH4RKVICC!")