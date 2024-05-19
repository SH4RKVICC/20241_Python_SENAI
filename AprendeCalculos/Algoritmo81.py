#81. criar algoritmo que dado um num. de conta corrente com 3 digitos
#retornar o seu digito verificador
d = int(input('Insira seu núm de 3 dígitos: '))
d1 = round((d / 100) * 1)
d2 = round((d % 100 / 10) * 2)
d3 = round((d % 100 % 10) * 3)
dv = d1 + d2 + d3
print(f'Digito Verificador: {dv}.')
print("FROM SH4RKVICC")