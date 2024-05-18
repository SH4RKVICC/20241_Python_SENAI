#48. ler valor do salário mínimo e a quantidade de quilowatts gasta p/uma residência
#valor em reais de cada quilowatt
#valor em reais a ser pago
#novo valor a ser pago por essa residência com um desconto de 10%.
sm = float(input("Insira o valor do sal. minimo atual: "))
qq = float(input("Insira a qtde. de quilowatt gasta pela residencia: "))
p = sm / 700
vp = p * qq
vd = vp * 0.9
print("\nPreço do quilowatt: ", p, "\n valor a ser pago: ", vp, "\n valor com desconto: ", vd)
print("FROM SH4RKVICC")