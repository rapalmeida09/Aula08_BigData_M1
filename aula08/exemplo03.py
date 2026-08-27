livros = []

qtd = int(input('Quantos livros: '))

for i in range(qtd):
    print(f'\nLivro {i+1}')
    
    livro = {}

    livro['titulo'] = input('Informe o titulo do livro: ')
    livro['autor'] = input('Informe o autor: ')
    livro['ano'] = int(input('Informe o ano: '))
    livro['genero'] = input('Informe o genero: ')
    livro['paginas'] = int(input('Informe as paginas: '))
    print(30* '==')

    livros.append(livro)

print('\n')   
print(30* '==')   
print('Livros a partir de 2020')
print(30* '==')
for elemento in livros:
    if elemento['ano'] >= 2020:
        print(f'\nTitulo: {elemento['titulo']}')
        print(f'Ano: {elemento['ano']}')
