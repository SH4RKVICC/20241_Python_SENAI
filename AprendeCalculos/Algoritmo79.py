#79. calcular rendimento de uma poupança, fornecer o valor
#constante de aplicação mensal, tava e num. de meses.
#A fórmula é valor acumulado = (P * (1 + i)^n - 1) / i
p = float(input('Insira o valor aplicado: R$'))
m = int(input('Insira o num. de meses:'))
t = float(input('Insira a taxa (0-1): '))
va = (p* (1 + t)**n - 1) / t
print(f'Valor Acumulado: R${va:.2f}.')
print("FROM SH4RKVICC")