def valor_a_pagar(x, n):
    resultado = x * n
    print(f'Total a pagar: {resultado:.2f}')


for i in range(3):
    print(f'\nCLIENTE {i+1}')

    quantidade = int(input('Informe a quantidade: '))
    valor = float(input('Informe o valor: '))

    valor_a_pagar(quantidade,valor)
