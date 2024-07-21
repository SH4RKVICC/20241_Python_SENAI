#136. Depois da liberação do governo para as mensalidades dos planos de saúde, as
# pessoas começaram a fazer pesquisas para descobrir um bom plano, não muito
# caro. Um vendedor de um plano de saúde apresentou a tabela a seguir. Criar um
# algoritmo que entre com o nome e a idade de uma pessoa e imprimir o nome e o
# valor que ela deverá pagar.
# ate l0 anos -R$ 30 00
# acima de 10 até 29 anos - R$ 60,00
# acima de 29 até 45 anos - R$ 120,00
# acima de 45 até 59 anos - R$ 150,00
# acima de 59 até 65 anos - R$ 250,00
# maior que 65 anos - R$ 400,00

print('Olá, paciente!')
n = input('Me conte seu nome: ')
i = int(input(f'Ótimo, {n}! Me conte sua idade: '))
if (i <= 10):
    c = '30,00'
elif (i > 10 and i <= 29):
    c = '60,00'
elif (i > 29 and i <= 45):
    c = '120,00'
elif (i > 45 and i <= 59):
    c = '150,00'
elif (i > 59 and i <= 65):
    c = '150,00'
else:
    c = '400,00'

print(f'{n}, o valor a pagar é R${c}!')

print('BY SH4RKVICC!')