#87. permitir que o aluno responda qual a capital do brasil de todas as possibilidades de escrita
cb = input('Qual a capital do Brasil? ')
if (cb == 'BRASÍLIA' or cb == 'Brasília'):
  print('Parabéns! Você acertou.')
else:
  if (cb == 'brasília' or cb == 'Brazília'or cb == 'brazília'):
    print('CERTO! Mas atenção para a ortógrafia: Brasília ou BRASÍLIA.')
  else:
    print('ERRADO! Estude mais, querido!')
print('FROM')