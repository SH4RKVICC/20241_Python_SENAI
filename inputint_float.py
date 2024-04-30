#36.leia 2 numeros inteiros e imprima a soma. antes deve aparecer a mensagem soma
n1 = int(input("Insira o primeiro numero inteiro: "))
n2 = int(input("Insira o segundo numero inteiro: "))
s = n1 + n2
print("Soma")
print(s)

#37.ler dois numeros inteiro e imprimir o produto
n1 = int(input("Insira o primeiro numero inteiro: "))
n2 = int(input("Insira o segundo numero inteiro: "))
p = n1 * n2
print("Aqui esta seu produto: ", p)

#38.ler num real e imprimir a terca parte
nr = float(input("Insira o número real desejado: "))
tp = nr / 3
print(tp)

#39.entrarcom dois numeros reais e imprimir a media com a mensagem media antes do resultado
n1 = float(input("Insira o primeiro numero real: "))
n2 = float(input("Insira o segundo numero real: "))
m = (n1 + n2) / 2
print("Média.")
print(m)

#40. dividendo, divisor, quociente, resto

i1 = int(input("Entre com o dividendo: "))
i2 = int(input("Entre com o divisor: "))
q = i1/i2
r = i1 % i2
print("dividendo: ", i1, "\nDivisor: ", i2, "\nQuociente: ", q, "\nResto: ", r)

#41. ler 4 num e fazer a média

n1 = int(input("Inserir o primeiro num.: "))
n2 = int(input("Inserir o segundo num.: "))
n3 = int(input("Inserir o terceiro num.: "))
n4 = int(input("Inserir o quarto num.: "))
m = (n1 + n2 + n3 + n4) /4
print("A média dos quatro termos acima é ", m)

#43. ler numero e realizar log base 10
from math import log
n = float(input("Inserir o número desejado: "))
r = log(n) / log(10)
print("O resultado é ", r)

#44. ler num e a base q se deseja calcular o logaritmo dele
n = float(input("Inserir o número desejado: "))
l = float(input("Insira a base que deseja calcular: "))
r = log(n) / log(l)
print("O resultado é ", r)

#45.
#n = float(input("Inserir o número desejado: "))
#q =
#rq =

#46. ler núm. e imprimir a seguinte saída:
n = float(input("Digite o número desejado: "))
q = n ** 2
rq = (n ** (1/2))
print("\nNúmero: ", n)
print("\nQuadrado: ", q)
print("\nRaiz Quadrada: ", rq)

#47. ler núm no formato CDU e imprimir invertido: UDC (Ex:123, sairá 321.)
#núm dv ser armazenado em outra variável antes de ser impresso
cdu = int(input("Insira o número de 3 dígitos: "))
c = cdu // 100
d = cdu % 100 // 10
u = cdu % 10
n1 = u * 100 + d*10 + c
print("\nNúmero: ", cdu)
print("\nInvertido: ", n1)

#48. ler valor do salário mínimo e a quantidade de quilowatts gasta p/uma residência
#valor em reais de cada quilowatt
#valor em reais a ser pago
#novo valor a ser pago por essa residência com um desconto de 10%.
sm = float(input("Insira o valor do sal. minimo atual: "))
qq = float(input("Insira a qtde. de quilowatt gasta pela residencia: "))
p = sm / 700
vp = p * qq
vd = vp * 0.9
print("\nPreço do quilowatt: ", p, "\n valor a ser pago: ", vp, "\n valor com desconto: ", vd)

#49. nome
n = input("Insira seu nome completo: ")
print("\nTodo o nome: ", n)
print("\nPrimeiro Caractere: ", n[0])
print("\nÚltimo Caractere: ", n[-1])
print("\nPrimeiro ao terceiro caractere: ", n[:3])
print("\nQuarto Caractere: ", n[3])
print("\nTodos menos o primeiro: ", n[1:])
print("\nOs dois ultimos: ", n[-2:])