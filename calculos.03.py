#79. calcular rendimento de uma poupança, fornecer o valor
#constante de aplicação mensal, tava e num. de meses.
#A fórmula é valor acumulado = (P * (1 + i)^n - 1) / i
# p = float(input('Insira o valor aplicado: R$'))
# m = int(input('Insira o num. de meses:'))
# t = float(input('Insira a taxa (0-1): '))
# va = (p* (1 + t)**n - 1) / t
# print(f'Valor Acumulado: R${va:.2f}.')

#80.ler qtde. de fitas de uma locadora possui e o valor que ela cobra por
#cada aluguel. mostrar infos:
##sabendo que um terço das fitas sao alugadas por mes, exibir faturamento local
##quando o cliente atrasa a entrega é cobrado uma multa de 10%
##um decimo das fitas sao devolvidas com atraso, calcule o valor ganho com multas por mes
##2% de fitas se estragam ao longo do ano e um decimo do total é comprado p/repor
#exibir qtde. de fitas que a locadora terá no final do ano
# qtdef = int(input('Insira a qtde. de fitas: '))
# va = float(input('Insira o valor do aluguel: '))
# fanual = qtdef/3 * va * 12
# print(f'Faturamento Anual: {fanual}.')
# m = va * 0.1 * (qtdef/3)/10
# print(f'Multas Mensais: {m}.')
# qtdefinal = qtdef - (qtdef * 0.02 + (qtdef/10))
# print(f'Qtde. de Fitas no Final do Ano: {qtdefinal}.')

#81. criar algoritmo que dado um num. de conta corrente com 3 digitos
#retornar o seu digito verificador
d = int(input('Insira seu núm de 3 dígitos: '))
d1 = round((d / 100) * 1)
d2 = round((d % 100 / 10) * 2)
d3 = round((d % 100 % 10) * 3)
dv = d1 + d2 + d3
print(f'Digito Verificador: {dv}.')