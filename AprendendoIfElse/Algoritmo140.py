#140. Um restaurante faz uma promoção semanal de descontos para clientes de acordo
# com as iniciais do nome da pessoa. Criar um algoritmo que leia o primeiro nome
# do cliente, o valor de sua conta e se o nome iniciar com as letras A, D, M ou S, dar
# um desconto de 30%. Para o cliente cujo nome não se inicia por nenhuma dessas
# letras, exibir a mensagem "Que pena. Nesta semana o desconto não é para seu
# nome; mas continue nos prestigiando que sua vez chegara".

n = input('Me conte seu nome: ')
v = float(input('Valor da conta: R$'))
i = n[0].upper()

ld = {'A', 'D', 'M', 'S'}

if i in ld:
    vd = v - (v*0.3)
    print(f'{n}, seu valor ao pagar com 30% de desconto é R${vd}')
else:
    print('Que pena. Nesta semana o desconto não é para seu nome; mas continue nos prestigiando que sua vez chegara!')