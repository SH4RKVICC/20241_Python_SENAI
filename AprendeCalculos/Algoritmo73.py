#73 ler numero real e calcular a parte inteira do numero, a parte fracionada e o numero arredondado
nr = float(input("Insira o número real desejado: "))
pi = int(str(nr).split('.')[0])
pf = int(str(nr).split('.')[1])
na = round(nr)
print(f"Parte Inteira do Núm.; {pi}.\nParte Fracionada: {pf}.\nNúm. Arredondado; {na}.")
print("FROM SH4RKVICC")