from datetime import date
atual = date.today().year
totalmaior = 0
totalmenor = 0
for pessoa in range(1, 8):
    nasc = int(input('Em que ano a {} pessoa nasceu? '.format(pessoa)))
    idade = atual - nasc
    if idade >= 21:
        totalmaior += 1
    else:
        totalmenor += 1
print('Ao total tivemos {} pessoas maiores de idade e {} menores'.format(totalmaior, totalmenor))
