peso = float(input('Qual seu peso? (Kg) '))
alt = float(input('Qual sua altura? (m) '))
total = peso / (alt ** 2)
print('O imc dessa pessoa é de {:.2f}'.format(total))
if total < 18.5:
    print('Abaixo do peso')
elif total < 25:
    print('Peso ideal')
elif total < 30:
    print('Sobrepeso')
elif total < 40:
    print('Obesidade')
elif total >= 40:
    print('Obesidade mórbida')