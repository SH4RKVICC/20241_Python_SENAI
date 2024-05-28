#92. receber dois números e efetuar a adição. Se o valor for maior que 20 deverá
#ser apresentando somando ele a mais 8, caso o valor somado seja menor ou igual
#a 20, mostralo subtraido por -5.
n1 = float(input('Digite o primeiro número: '))
n2 = float(input('Digite o segundo número: '))
s = n1 + n2
if (s > 20):
  ns = s + 8
else:
  ns = s - 5
print(f'Soma: {ns}')
print('by SH4RKVICC!')