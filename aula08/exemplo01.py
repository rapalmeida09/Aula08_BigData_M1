# lista = [['a', 'b', 'c' ], 1, 2]

# Dicionário: estrutura chave valor
produto = {
    'nome': 'Notebook',
    'preço': 3500,
    'marca': 'Lenovo'
}

print(f'Marca do Produto: {produto["marca"]}')
print(f'Dicionário inicial: {produto}')

print('\nAlterando o dicionário')
produto['marca'] = 'HP' # Alterando valor de uma chave
produto['Tela'] = '17"' # Criar uma chave nova
del produto['preço'] #apaga uma chave


print(produto)











'''
produto = {
    1 :{
        'nome': 'notebook',
        'preco': 3500,
        'marca': 'lenovo'
    } 
}
'''