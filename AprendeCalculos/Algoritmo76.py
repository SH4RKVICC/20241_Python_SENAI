#76. ler num entre 0 e 60 e mostrar seu sucessor, o sucesso de 60 é 0.
#Não pode ser utilizado nenhum comando de seleção, nem de repetição.
print("-------------------------- DESCOBRINDO O SUCESSOR! -------------------------")
n = float(input('Insira o número (0-60) desejado: '))
s = (n + 1) % 61
print(f'O sucessor é {s:.0f}.') 
print('----------------------------------------------------------------------------')
print("FROM SH4RKVICC")