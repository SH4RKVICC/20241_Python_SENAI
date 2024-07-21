#125. Entrar com a idade de uma pessoa e informar: se é maior de idade, se é menor de idade, se é maior de 65 anos

print('Vamos brincar de idade!')
i = int(input('Me conte sua idade: '))

if (i >= 18):
    if (i > 65):
        print('Você tem mais de 65 anos!')
    else:
        print('Você é maior de idade!')
else:
    print('Você é menor de idade!')