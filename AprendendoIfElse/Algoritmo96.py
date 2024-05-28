#96.ler numero e dizer se ele é divisivel por 3 ou por 7
n = int(input("Insira o número desejado: "))

if (n % 3 == 0 and n % 7 ==0):
  print("Esse número é divisivel por 3 e por 7!")
elif(n % 7 == 0):
  print("Esse número é divisivel por 7!")
elif(n % 3 == 0):
  print("Esse número é divisivel por 3!")
else:
  print("Esse número não é divisivel nem por 3, nem por 7!")
print("Fim! By SH4RKVICC")