#98. A prefeitura do Rio de Janeiro abriu uma linha de crédito para os funcionários
#estatutários. O valor máximo da prestação não poderá ultrapassar 30% do salário
#bruto. Receber com o salário bruto e o valor da prestação e informar se o
#empréstimo pode ou não ser concedido.
print("-------------------------")
print("BEM-VINDO, CAMARADA!")
print("-------------------------")
sal = float(input('Insira o valor do seu salário atual: R$'))
e = float(input('Insira o valor da prestação: R$'))
vm = (30/100) * sal
if (e > vm):
  print('Sinto muito, seu emprestimo foi negado!')
else:
  print('Parabéns! O emprestimo foi aprovado.')

print("Fim! By SH4RKVICC!")