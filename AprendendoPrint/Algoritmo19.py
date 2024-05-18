#19. testando biblioteca math e suas funções.

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
print("FROM SH4RKVICC")