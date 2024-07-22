#130. Um comerciante comprou um produto e quer vendê-lo com um lucro de 45% se o
# valor da compra for menor que R$ 20,00; caso contrário, o lucro será de 30%.
# Entrar com o valor do produto e imprimir o valor da venda.

vp = float(input('Valor do Produto: R$'))

if (vp < 20):
    l = 0.45
else:
    l = 0.30
vn = vp + (vp*l)
print(f'Valor da Venda: R$ {vn}')