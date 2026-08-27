dias = ['segunda-feira', 'terça-feira', 'quarta-feira', 'quinta-feira', 'sexta-feira']

print(dias[0])

# for tradicional
for i in range(len(dias)):
   print(dias[i])

# Segundo for
for elemento in dias:
    if elemento == 'quarta-feira' or elemento == 'segunda-feira':
        print('Hoje tem aula!')
    else:
        print('Obá!!! Estou de folga!')

# Terceiro for com enumerate: usado para pegar posição e o valor
# Normalmente usado, quando precisa do índice
for i, v in enumerate(dias):
    print(f'Posição {i}, dia {v}')