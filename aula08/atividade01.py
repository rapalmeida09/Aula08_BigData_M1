META = 5000
vendedores = []

for i in range(3):
    print(f'\nVENDEDOR {i+1}')
    
    vendedor = {}

    vendedor['nome'] = input('Informe o nome: ')
    vendedor['região_atuação'] = input('Informe a região de atuação:')
    vendedor['valor_vendas'] = float(input('Informe o valor total de vendas no mês: '))
    vendedor['qtd_vendas'] = int(input('Informe a quantidade de vendas ralizadas: '))
    print(30* '==')

    vendedores.append(vendedor)

print('\n')   
print(30* '==')
print('VENDEDORES QUE BATERAM A META!')
print(30* '==')
for elemento in vendedores:
    if elemento['valor_vendas'] >= META:
        print(f'\nVendedor: {elemento['nome']}')

