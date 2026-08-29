'''
Uma empresa está realizando um processo seletivo para preenchimento de vagas e
precisa organizar o cadastro dos candidatos.

Desenvolva um programa que registre os dados de 5 pessoas interessadas na vaga. 

Apenas candidatos com 18 anos ou mais poderão se candidatar.

As informações coletadas serão: nome, idade, telefone, e-mail e formação acadêmica.

Ao final, o sistema deve exibir a lista de candidatos com cadastro realizado.

'''
candidatos = []

for i in range(5):
    print(f'\nCANDIDATO {i + 1}:')

    candidato = {}

    candidato['nome'] = input('NOME: ')
    candidato['idade'] = int(input('IDADE: '))
    candidato['telefone'] = input('TELEFONE: ')
    candidato['email'] = input('E-MAIL: ')
    candidato['formacao'] = input('FORMAÇÃO ACADÊMICA: ')

    if candidato['idade'] < 18:
        print('!!!Erro de cadastro!!! \n---Candidato menor de idade!---')
    else:
        print('---Candidato cadastrado!---')
        candidatos.append(candidato)

print('\n')
print(30* '==')
print('CANDIDATOS CADASTRADOS')
print(30* '==')

for i in candidatos:
    print(f'\n {i['nome']}')
    