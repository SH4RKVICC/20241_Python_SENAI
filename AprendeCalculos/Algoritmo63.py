#63 efetuar calculo de sl liquido de um professor dados: valor hora aula, n de aulas dadas no mes e percentual de desconto inss
print("Olá, Prezado(a) Professor(a)!")
vha = float(input("Insira o valor da hora aula: "))
naulaspm = int(input("Insira o número de aulas completas dadas: "))
pdinss = float(input("Insira o percentual de desconto: "))
sb = naulaspm * vha
td = (pdinss / 100) * sb
sl = sb - td
print(f"\nSeu salário bruto é R${sb} e seu salário líquido R${sl}. n\Obrigada pela confiança!")
print("FROM SH4RKVICC")