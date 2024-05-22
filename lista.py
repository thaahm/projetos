lista = []

print('LISTA DE MERCADO')
print('-' * 17)

while True:
    print('Inserir')
    print('Apagar')
    print('Listar')
    opcao = input('Escolha uma opção: ')

    if opcao == 'Inserir':
        item = input('Insira um item na lista: ')
        lista.append(item)
        print(f'O {item} foi adicionado na lista.')

    if opcao == 'Apagar':
        item = input('Digite o item para remover da lista: ')
        if item in lista:
            lista.remove(item)
            print(f'O {item} foi removido da lista.')

    if opcao == 'Listar':
        if lista:
            print('Lista de Compras: ')
            for i, item in enumerate(lista, start=1):
                print(f'{i}, {item}')