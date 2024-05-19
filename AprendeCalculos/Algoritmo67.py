#67. calcular valor da prestacao em atraso
v = float(input("Insira o valor da prestação: "))
tx = float(input("Insira o valor da taxa: "))
t = float(input("Insira o tempo em meses: "))
p = v + (v*(t/100)*t)
print(f"O valor da prestação em atraso é R${p}.")
print("FROM SH4RKVICC")