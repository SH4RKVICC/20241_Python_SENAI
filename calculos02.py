#65. apresentar o valor do vol. de uma lata de oleo
# a = float(input("Insira a altura da lata: "))
# r = float(input("Insira o raio da lata: "))
# v = 3.14159 * ((r**2) * a)
# print(f"O volume da lata é {v}")

#66. calcular qtde de litros de combustivel gastos em uma viagem
#carro faz 12km com 1 litro /
# tg = float(input("Insira o tempo gasto em horas: "))
# vm = float(input("Insira a velocidade média: "))
# d = tg * vm
# lu = d / 12
# print(f"SUa distância percorrida foi {d}Km e seus {lu}L usados.")

#67. calcular valor da prestacao em atraso
# v = float(input("Insira o valor da prestação: "))
# tx = float(input("Insira o valor da taxa: "))
# t = float(input("Insira o tempo em meses: "))
# p = v + (v*(t/100)*t)
# print(f"O valor da prestação em atraso é R${p}.")

#68.ler dois valores para as variaveis A e B, trocar valores e apresenta-los
# a = float(input("Insira o valor de A: "))
# b = float(input("Insira o valor de B: "))
# na = b
# nb = a
# print(f'A ={na}.\n\nB = {nb}')

#69. ler numerador e denominador de uma fração e transfome-o em num decimal
# n = int(input("Insira o valor de A: "))
# dn = int(input("Insira o valor de B: "))
# d = n / dn
# print(f'Resultado: {d}')

#70.
# vc = float(input("Insira o valor da conta: R$"))
# g = vc *1.1
# print("O Valor final com gorjeta é R$", g)

#71. ler valor de hora e informar quantos minutos se passaram desde o inicio do dia
# ha = int(input("Insira a hora atual: "))
# ma = int(input("Insira o minuto atual: "))
# tm = (ha * 60) + ma
# print(f"Até agora se passaram {tm} minutos.")

#72. ler valor de um deposito e o valor da taxa de juros. calcular e mostrar o
#valor do rendimento e o valor total dps do rendimento
# vd = float(input("Insira o valor do deposito: "))
# vt = float(input("Insira o valor da taxa de juros: "))
# v = (vd * vt) / 100
# t = vd + v
# print(f"O valor do rendimento é {v}, portanto o valor total é aprox. {t}")

#73 ler numero real e calcular a parte inteira do numero, a parte fracionada e o numero arredondado
# nr = float(input("Insira o número real desejado: "))
# pi = int(str(nr).split('.')[0])
# pf = int(str(nr).split('.')[1])
# na = round(nr)
# print(f"Parte Inteira do Núm.; {pi}.\nParte Fracionada: {pf}.\nNúm. Arredondado; {na}.")

#74. ler o valor do sal. minimo, salario de uma pessoa e calcular quanto salarios minimos ela ganha
# sm = float(input("Insira o valor atual do salário minimo: "))
# ss = float(input("Insira o valor atual do seu salário: "))
# qtdesalmin = ss / sm
# print(f'Você ganha {qtdesalmin:.2f} salarios minimos.')

#75. ler a parte inteira do peso de uma pessoa, calcular e imprimir o peso em
#gramas e o novo peso em gramas caso ela engordar 12%
# pp = float(input('Insira o seu peso em Kg: '))
# pg = pp * 1000
# np = pg * 1.12
# print(f'Peso em Gramas: {pg}g.\nNovo Peso: {np}g.')

#76. ler num entre 0 e 60 e mostrar seu sucessor, o sucesso de 60 é 0.
#Não pode ser utilizado nenhum comando de seleção, nem de repetição.
# print("-------------------------- DESCOBRINDO O SUCESSOR! -------------------------")
# n = float(input('Insira o número (0-60) desejado: '))
# s = (n + 1) % 61
# print(f'O sucessor é {s:.0f}.') 
# print('----------------------------------------------------------------------------')

#77. ler dois numeros reais e imprimir o quadrado da diferença do primeiro valor pelo segundo e a diferença dos quadrados
# v1 = float(input('Insira o primeiro valor: '))
# v2 = float(input('Insira o segundo valor: '))
# qd = (v1 - v2) **2
# dq = v1**2 - v2**2
# print(f'Quadrado da Diferença: {qd}.\nDiferença dos Quadrados: {dq}.')

#78.dado um poligono convexo de n lados, podemos calcular o num. de diagonais
#desse poligno pela formula nd = n (n - 3) /2. Ler quandos lados tem o poligono,
#calcular e escrever o num. de diagonais diferentes
# nl = int(input('Insira o num. de lados do poligono:'))
# nd = nl * (nl - 3) / 2
# print(f'Num. de Diagonais: {nd:.0f}.')