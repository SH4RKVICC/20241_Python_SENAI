#134. A confederação brasileira de natação irá promover eliminatórias para o próximo
# mundial Fazer um algoritmo que receba a idade de um nadador e imprimir a sua
# categoria segundo a tabela a seguir:

# Categoria Idade
# InfantilA 5-7anos
# Infantil B 8— 10 anos
# JuvenilA 11 - 13 anos
# Juvenil 14— 17 anos
# Sênior maiores de 18 anos

print('Olá, nadador!')
i = int(input('Me conte sua idade: '))
if (i >= 5):
    if (i <= 7):
        c = 'Infantil A'
    elif (i > 7 and i == 10):
        c = 'Infantil B'
    elif (i > 10 and i == 13):
        c = 'Juvenil A'
    elif (i > 13 and i == 17):
        c = 'Juvenil B'
    else:
        c = 'Sênior'
else:
    'O nadador ainda não está apto para a competição.'

print(f'Sua classificação é {c}!')