#91. ler dois valores numéricos inteiros e efetue a adição; caso o resultado seja maior que 10, apresente!
n1 = int(input('Insira o primeiro número: '))
n2 = int(input('Insira o segundo número: '))
s = n1 + n2
if (s > 10):
  print(f'Resultado: {s}')
else:
  print('O resultado é menor que 10, tente novamente!')
print('By SH4RKVICC!')