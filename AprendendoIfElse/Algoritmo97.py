#97. receber um núm. e informar se ele é divisível por 10, por 5 ou por 2.
n = int(input("Insira o número desejado: "))

if(n % 10 == 0 and n % 5 == 0 and n % 2 == 0 ):
    print("Esse número é divisivel por 2, 5 e 10.")
elif(n % 10 ==0 and n % 5 == 0):
    print("Esse número é divido por 10 e por 5.")
elif(n % 10 ==0 and n % 2 == 0):
    print("Esse número é divido por 10 e por 2.")
elif(n % 2 ==0 and n % 5 == 0):
    print("Esse número é divido por 2 e por 5.")
else:
    print("Esse número não é divisivel nem por 2, 5 e 10.")
print("Fim! By SH4RKVICC!")