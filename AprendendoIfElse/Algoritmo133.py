#133. Segundo uma tabela medica o peso ideal esta relacionado com a altura e o sexo

# Fazer um algoritmo que receba a altura e o sexo de uma pessoa, calcular e impri-
# ir o seu peso ideal utilizando as seguintes formulas m

# para homens: (72.7 * H) -58
# para mulheres (62 1 * H) -44.7

s = input('Insira seu gênero (M/F): ')
a = float(input('Insira sua altura atual em M:'))
ss = s.upper()

if (ss == 'M'):
    pi = (72.7 * a) - 58
else: 
    pi = (72.7 * a) - 44.7
print(f'Seu Peso Ideal: {pi:.2f}Kg.')
