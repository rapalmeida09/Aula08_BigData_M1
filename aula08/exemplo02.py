pessoa = {}
# print(pessoa)
'''
nome = input('Informe o nome: ')
ano_nascimento = int(input('Informe o ano de nascimento: '))

pessoa['nome'] = nome # input('Informe o nome: ')
pessoa['ano_nascimento'] = ano_nascimento # int(input('Informe o ano de nascimento: '))
pessoa['idade'] = 2026 - pessoa['ano_nascimento']
'''
pessoa['nome'] = input('Informe o nome: ')
pessoa['ano_nascimento'] = int(input('Informe o ano de nascimento: '))
pessoa['idade'] = 2026 - pessoa['ano_nascimento']

print(pessoa)
# print(f'A idade é {idade}')