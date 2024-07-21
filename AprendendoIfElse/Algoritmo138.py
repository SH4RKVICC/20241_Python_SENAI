#138. Ler um número inteiro entre 1 e 12 e escrever o mês correspondente. Caso o
# usuário digite um número fora desse intervalo, deverá aparecer uma mensagem
# informando que não existe mês com este número.

print('Vamos descobrir qual é o mês pelo seu número!')
n = int(input('Insira um número de 1 a 12: '))

if (n >= 1 and n <= 12):
    if (n == 1):
        m = 'Janeiro'
    elif (n == 2):
        m = 'Fevereiro'
    elif (n == 3):
        m = 'Março'
    elif (n == 4):
        m = 'Abril'
    elif (n == 5):
        m = 'Maio'
    elif (n == 6):
        m = 'Junho'
    elif (n == 7):
        m = 'Julho'
    elif (n == 8):
        m = 'Agosto'
    elif (n == 9):
        m = 'Setembro'
    elif (n == 10):
        m = 'Outubro'
    elif (n == 11):
        m = 'Novembro'
    else:
        m = 'Dezembro'
    print(f'O mês de número {n} é {m}!')
else:
    print('Não há mês com esse número :(')

print('BY SH4RKVICC!')