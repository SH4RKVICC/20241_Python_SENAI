#16.
x = int(10)
print(x)

#17.
x = int(10)
print("Valor de X = ", x)

#18.
x = int(10)
print("Valor de X =", x + 1)

#19. teste

def realint(x):
  return int(x)

import math

def formatar(num, casas_dec):
  return round(num, casas_dec)

print("raiz: ", math.sqrt(64))
print("raiz com exp e log sem realint: ", math.exp(1/2 * math.log(64)), ", ")
print(formatar(math.sin(45*math.pi/180)+0.0001,3))
print("potencial com exp e log e formatar: ", formatar(math.exp(3*math.log(8))+0.001,3))
print("potencia com exp e log sem formatar: ", math.exp(3*math.log(8)))
print("potencia com operador ** e formatar: ", formatar(8**3,3))
print("raiz cubida: ", math.exp(1/3* math.log(8)))
print("absoluto: ", abs(-8))
print("absoluto: ", abs(8))
print("convertendo para inteiro 5.5: ", realint(5.5))
print("convertendo para inteiro 6.5: ", realint(6.5))
print("convertendo para inteiro 5.45: ", realint(5.45))
print("convertendo para inteiro 5.51: ", realint(5.51))
print("convertendo para real 87: ", realint(87))
print("convertendo para int 3/4: ", realint(3/4))

#21. testando hierarquia
print("\nTESTABNDO HIERARQUIA\n")
print("\n12 + 5/2 é igual a: ", 12 + 5/2)
print("\nÉ diferente de (12 + 5)/2 que é igual a: ",(12 + 5)/2, " logo ** tem HIERARQUIA MAIOR \ndo que + ou -")
print("\n\n64** 1/4 é igual a: ", 64**1/4)
print("\nÉ DIFERENTE de 64**(1/4)que é igual a: ", 64**(1/4), " logo ** tem HIERARQUIA MAIOR \ndo que * ou /")
print("\n\n3*7 % 5 é igual a: ", 3*7 % 5)
print("\nÉ DIFERENTE de (3 * 7) % 5 que é igual a: ",(3 * 7) % 5, "logo % tem HIERARQUIA MAIOR do que: * ")
print("\n\n3 * 7 div 5 é igual a: ", 3*7 / 5)
print("\nÉ IGUAL a (3 * 7) div. 5 : ", (3 * 7) / 5," logo div tem a MESMA HIERARQUIA \nda * ou / ")

#22. teste de hierarquia 2

print("\nTESTABNDO HIERARQUIA\n")
print("\n18/6 % 2 é igual a: ", 18 + 6 % 2)
print("\nUma operação de divisâo fora de parênteses não pode ser um \ndos operados de uma expressâo com %. ")
print("\n\n20 / 4 div 2 é igual a: ", 20 / 4 //2)
print("\nÉ IGUAL a (20 / 4) div 2: ", (20 / 4) //2, " logo ** tem HIERARQUIA MAIOR \ndo que * ou /")
print("\n\n3*7 % 5 é igual a: ", 3*7 % 5)
print("\nÉ DIFERENTE de (3 * 7) % 5 que é igual a: ",(3 * 7) % 5, " logo div tem a MESMA HIERARQUIA.")
print(" da /. ")
print("\n\n30 / 4 div 2 é igual a: ", 30/4 // 2)
print("\nÉ IGUAL a (30 / 7) div. 2 : ", (30 / 4) // 2," logo div tem a MESMA HIERARQUIA")
print(" da /")
print("\n\n7. div 4: ", 7. // 4)
print("\n7 div 4: ", 7 // 4)
print("\n\n6. div 4: ", 6. // 4)
print("\n\n6 div 4: ", 6 // 4)

#23. entrar c/um número inteiro de 3 casas e imprimir o algarismo da casa das dezenas.
a = int(input("Digite o número de três casas: "))
d = a % 100 // 10
print("algarismo da casa das dezenas: ", d)

#24.
a = int(input("Digite o número de três casas: "))
d = a // 10 % 10
print("algarismo da casa das dezenas: ", d)

#25. ler data no formato ddmmaa e imprimir: dia, mês e ano separados
data = int(input("Digite a data no formato ddmmaa: "))
d = data // 10000
m = data % 10000 //100
a = data % 100
print("\nDia: ",d)
print("\nMês: ",m)
print("\nAno: ",a)

#25. ler data no formato ddmmaa e imprimir: dia, mês e ano separados

data = int(input("Digite a data no formato ddmmaa: "))
d = data // 10000
m = data % 10000 //100
a = data % 100
print("\nDia: ",d)
print("\nMês: ",m)
print("\nAno: ",a)

#26. ler data no formato ddmmaa e imprimir no formato mmddaa
data = int(input("Digite a data no formato ddmmaa: "))

d = data // 10000
m = data % 10000 // 100
a = data % 100
nd = m * 10000 + d*100 + a
print("\nDia: ",d)
print("\nMês: ",m)
print("\nAno: ",a)
print("\n\nDATA NO FORMATO MMDDAA: ", nd)

#27.
x = -2
y = -5
print("X = ", x)
print("Y = ", y)
x = x**2
y = y*2
print("Novo valor de X = ", x)
print("Novo valor de Y = ", y)

#30.o produto de 28 e 43

produto = 28 * 43
print(produto)

#31.Crie um algoritmo que imprima a média aritmetica entre os numero 8,9 e 7
s = 8 + 9 +7
m = s / 3
print(m)


