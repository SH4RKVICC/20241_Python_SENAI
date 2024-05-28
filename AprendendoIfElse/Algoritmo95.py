#95. receber número e informar se é ou não divisível por 5.
n = int(input("Insira o número desejado: "))
if(n % 3 == 0 and n % 7 == 0):
    print("Este número é divisivel tanto por 3 quanto por 7.")

elif(n % 3 == 0):
    print("Esse número é divisivel somente por 7, mas não por 3.")

elif(n % 7 == 0):
    print("Esse número é divisivel somente por 7, mas não por 3.")

else:
    print("Esse número não é divisivel nem por 3, nem por 7")
print("Fim! By SH4RKVICC")