#129. Entrar com o salário de uma pessoa e imprimir o desconto do INSS segundo a ta-
# bela a seguir:

# menor ou igual a R$ 600,00 isento
# maior que R$ 600,00 e menor ou igual a R$ 1200,00 20%
# maior que R$ 1200,00 e menor ou igual a R$2000,00 25%
# maior que R$ 2000,00 30%

s = float(input('Insira seu salário atual: '))

if (s > 600):
    if (s > 600 and s <= 1200):
        t = 0.20
    elif (s > 600 and s <= 1200):
        t = 0.25
    else:
        t = 0.30
    sd = s - (s*t)
    print(f'Valor final do Sal.: {sd}')
else:
    print('Você está insento de taxa.')
print('BY SH4RKVICC!')
