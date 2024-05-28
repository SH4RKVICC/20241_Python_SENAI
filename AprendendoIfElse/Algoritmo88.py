#88. calculadora.

print("---------------------------")
print("CALCULADORA ATIVAR!")
print("---------------------------")
print("Para Somar: +\nPara Subtrair: -\nPara Multiplicar: *\nPara Dividir: /")
o = input("Digite a Opção: ")
n1 = float(input("Digite o número desejado: "))
n2 = float(input("Digite o outro número desejado: "))

if (o == '+'):
  r = n1 + n2
elif (o == '-'):
  r = n1 - n2
elif (o == '*'):
  r = n1 * n2
elif (o == '/'):
  r = n1 / n2
else:
  print('Essa operação não é uma opção.')

print(f"Resultado: {r}")
print('By SH4RKVICC!')