#135. Criar um algoritmo que leia a idade de uma pessoa e informara sua classe eleitoral:
# não-eleitor (abaixo de 16 anos)
# eleitor obrigatório (entre 18 e 65 anos)
# eleitor facultativo (entre 16 e 18 anos e maior de 65 anos)

print('Vamos descobrir sua classe eleitoral!')
i = int(input('Me conte sua idade: '))

if (i >= 16):
    if (i > 65 or i < 18 and i >= 16):
        s = 'eleitor facultativo'
    else:
        s = 'eleitor obrigatório'
else:
    s = 'não-eleitor'
print(f'Você é {s}!')