#26. ler data no formato ddmmaa e imprimir no formato mmddaa.
#recebendo dado
data = int(input("Digite a data no formato ddmmaa: "))
#realizando calculos
d = data // 10000
m = data % 10000 // 100
a = data % 100
nd = m * 10000 + d*100 + a
#mostrando resultados.
print("\nDia: ",d)
print("\nMês: ",m)
print("\nAno: ",a)
print("\n\nDATA NO FORMATO MMDDAA: ", nd)
print("FROM SH4RKVICC")