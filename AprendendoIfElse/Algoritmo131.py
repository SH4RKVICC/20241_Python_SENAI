#131. A turma de Programação 1, por ter muitos alunos, será dividida em dias de provas.
# Após um estudo feito pelo coordenador, decidiu-se dividi-la em três grupos.
# Fazer um algoritmo que leia o nome do aluno e indicar a sala em que ele deverá
# fazer as provas, tendo em vista a tabela a seguir e sabendo-se que todas as salas
# se encontram no bloco F:
# A - K:sala 101
# L-N:sala 102
# O - Z:sala 103

n = input('Insira seu nome para descobrir o local de prova: ')
inicial = n[0].upper()

if (inicial == 'A' or inicial == 'B' or inicial == 'C' or inicial == 'D' or inicial == 'E' or inicial == 'F' or inicial == 'G' or inicial == 'H' or inicial == 'I' or inicial == 'J' or inicial == 'K'):
    s = '101'
elif (inicial == 'L' or inicial == 'M' or inicial == 'N'):
    s = '102'
else:
    s = '103' 
print(f'{n}, sua sala é a {s}')