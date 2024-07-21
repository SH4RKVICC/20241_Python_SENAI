#139. Sabendo que somente os municípios que possuem mais de 20.000 eleitores aptos
# têm segundo turno nas eleições para prefeito caso o primeiro colocado não tenha
# mais do que 50% dos votos, fazer um algoritmo que leia o nome do município, a
# quantidade de eleitores aptos, o número de votos do candidato mais votados
# e informar se ele terá ou não segundo turno em sua eleição municipal.

print('SISTEMA ELEITORAL')
n = input('Nome do Município: ')
ea = int(input(f'Qtde. de Eleitores Aptos de {n}: '))
v = int(input(f'Qtde. de Votos do Candidato mais votado de {n}: '))
c = ea / 2

if (v < c):
    print(f'Urge a necessidade de um segundo turno eleitoral em {n}.')
else:
    print('Sem necessidade de segundo turno eleitoral, o candidato mais votado será eleito.')

print('BY SH4RKVICC!')