#25. ler data no formato ddmmaa e imprimir: dia, mês e ano separados.
#recebendo dado
data = int(input("Digite a data no formato ddmmaa: "))

#realizando calculos
d = data // 10000
m = data % 10000 //100
a = data % 100

#mostrando resultados
print("\nDia: ",d)
print("\nMês: ",m)
print("\nAno: ",a)
print("FROM SH4RKVICC")