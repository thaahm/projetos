somaidade = 0
mediaidade = 0
maioridadeh = 0
nomevelho = ''
mulher = 0
for p in range(1, 6):
    print('---- {} PESSOA ----'.format(p))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [F/M]: ')).strip()
    somaidade += idade
    if p == 1 and sexo in 'Mm':
        maioridadeh = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maioridadeh:
        maioridadeh = idade
        nomevelho = nome
    mediaidade = somaidade / 4
    if sexo in 'Ff' and idade < 20:
        mulher += 1
print('A média de idade do grupo é {}'.format(mediaidade))
print('O homem mais velho tem {} anos e se chama {}'.format(maioridadeh, nomevelho))
print('São {} mulheres com menos de 20 anos'.format(mulher))



