# 127. Entrar com nome, nota da PR e nota da PR2 de um aluno. Imprimir nome, nota
# da PR1, nota da PR2, média e uma das mensagens: Aprovado, Reprovado ou em
# Prova Final (a média é 7 para aprovação, menor que 3 para reprovação e as de-
# mais em prova final).

print('Vamos descobrir se você foi aprovado!')
print('Me conte seu nome!')
n = input('Nome: ')

print(f'Okay, {n}! Me conte suas notas!')
p1 = float(input('PR1: '))
p2 = float(input('PR2: '))
m = (p1 + p2) / 2

if (m >= 3):
    if (m < 7):
        s = 'em Prova Final'
    else:
        s = 'Aprovado! Parábens'
else:
    s = 'Reprovado'

print(f'{n}, sua média é {m} e você está {s}!')