#47. ler núm no formato CDU e imprimir invertido: UDC (Ex:123, sairá 321.)
#núm dv ser armazenado em outra variável antes de ser impresso
cdu = int(input("Insira o número de 3 dígitos: "))
c = cdu // 100
d = cdu % 100 // 10
u = cdu % 10
n1 = u * 100 + d*10 + c
print("\nNúmero: ", cdu)
print("\nInvertido: ", n1)
print("FROM SH4RKVICC")