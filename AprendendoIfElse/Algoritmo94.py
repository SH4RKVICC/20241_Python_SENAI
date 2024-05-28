#94. receber número e mostrar  uma das mensagens
n = int(input("Insira o número que deseja saber se é multiplo de 3: "))
c = n % 3
if(c == 0):
    print("Oba! Ele é multiplo de 3.")
else:
    print("Poxa! Não foi dessa vez, seu número não é multiplo de 3")
print("by SH4RKVICC!")