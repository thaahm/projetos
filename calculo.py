print('\033[1;35;40mCALCULADORA\033[m')
print('-' * 13)


def calculo():
    
    n1 = int(input('Primeiro número: '))
    n2 = int(input('Segundo número: '))
    operacao = input('Selecione uma operação -> + para adição, - para subtração, * para multiplicação e / para divisão: ')
    

    if operacao == '+':
        print(f'{n1} + {n2} = ')
        print(n1 + n2)

    elif operacao == '-':
        print(f'{n1} - {n2} = ')
        print(n1 - n2)

    elif operacao == '*':
        print(f'{n1} * {n2} = ')
        print(n1 * n2)

    elif operacao == '/':
        print(f'{n1} / {n2} = ')
        print(n1 / n2)

    else: 
        print('\033[0;31;40mErro! Digite um número válido.\033[m')


    cont_calculo = (input('Quer calcular de novo? S/N: ')).upper()

    if cont_calculo == 'S':
        calculo()

    elif cont_calculo == 'N':
        print('Até mais!')

    else:
        cont_calculo

calculo()