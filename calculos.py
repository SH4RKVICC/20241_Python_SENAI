#51. ler raio e imprimir perimetro e area
# r = float(input("Insira a medida do raio: "))
# p = 2* 3.14 * r
# a = 3.14 * r **2
# print(f"\nPerimetro: {p}")
# print(f"\nArea: {a}")

#52. ler lado de 1 quadrado e
# lq = float(input("Insira o valor do lado do quadrado:"))
# p = 4 * lq
# a = lq ** 2
# d = lq * (2 ** (1/2))
# print(f"\nPerimetro: {p}")
# print(f"\nArea: {a}")
# print(f"\nDiagonal: {d}")

#53. entrar com lado a, b e c de um paralelepipedo
# import math
# a = float(input("Insira a base: "))
# b = float(input("Insira a altura: "))
# c = float(input("Insira a profundidade: "))
# d = math.sqrt((a**2) + (b**2) + (c**2))
# print(f"\nDiagonal: {d}")

#54. calcula e mostra area de triangulo
# a = float(input("Insira a base: "))
# b = float(input("Insira a altura do triangulo: "))
# area = (a*b)/2
# print(f"\nÁrea: {area}")

#55.
# ma = float(input("Insira a medida diagonal maior: "))
# me = float(input("Insira a medida diagonal menor: "))
# a = (ma * me)/2
# print(f"\nÁrea: {a}.")

#56.
# n = input("\nInsira seu nome: ")
# print(f"Nome: {n}.")
# i = int(input("\nInsira sua idade: "))
# print(f"Idade: {i}.")

#57.
# import math
# pr1 = float(input("Insira o valor da PR1: "))
# pr2 = float(input("Insira o valor da PR2: "))
# mf = (pr1 + pr2) / 2
# mt = (mf - 0.5) + 0.001
# ma = mf + 0.001
# print(f"\nMÉDIA TRUNCADA = {mt} \nMÉDIA ARREDONDADA = {ma}")

#58.
# import math
# xnum1 = float(input("Inserir xnum1 aqui: "))
# xnum2 = float(input("Inserir xnum2 aqui: "))
# xnum3 = float(input("Inserir xnum3 aqui: "))
# x = xnum1 + xnum2 / (xnum3 + xnum1) + 2 *(xnum1 - xnum2) + math.log(64.)/math.log(2.)
# print(f"\nX = {x}")

#59. ler valores dos catetos de um triangulo ret e printar hipotenusa
# import math
# pc = float(input("Insira o valor do primeiro cateto: "))
# sc = float(input("Insira o valor do segundo cateto: "))
# h = math.sqrt(pc**2 + sc**2)
# print(f"\nA hipotenusa é {h}.")

#60 ler razão de uma PA e o valor do 1termo. imprimir 10 termos da serie
# pt = int(input("Insira o 1 termo: "))
# r = int(input("Insira a razão: "))
# dc = pt + 9*r
# print(f"\nO 10 termo é: {dc}")

#61 ler razao de pg e o 1valor. calcular o 5termo
# t1 = int(input("Insira o primeiro termo: "))
# r = int(input("Insira a razão: "))
# t5 = t1* (r**4)
# print(f"\nO quinto tempo desta P.G é:  {t5}")

#62 ler valor produto e lançar novo valor com desconto de 9%
# p = float(input("Insira o valor do produto: "))
# np = p *0.91
# print(f"\nO novo valor é: {np}.")

#63 efetuar calculo de sl liquido de um professor dados: valor hora aula, n de aulas dadas no mes e percentual de desconto inss
# print("Olá, Prezado(a) Professor(a)!")
# vha = float(input("Insira o valor da hora aula: "))
# naulaspm = int(input("Insira o número de aulas completas dadas: "))
# pdinss = float(input("Insira o percentual de desconto: "))
# sb = naulaspm * vha
# td = (pdinss / 100) * sb
# sl = sb - td
# print(f"\nSeu salário bruto é R${sb} e seu salário líquido R${sl}. n\Obrigada pela confiança!")

#64. ler temperatura em graus centigraodos e converter em fahrenheit
# c = float(input("Insira a temperatura em graus centigrados: "))
# f = ((9*c) + 160) / 5
# print(f"A temperatura em Fahrenheit é {f} F.")