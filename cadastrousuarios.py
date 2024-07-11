lista = []

print('CADASTRO DE USUÁRIOS')
print('-' * 20)

    

def cadastro():
    nome = input('Nome do usuário: ')
    idade = input('Idade do usuário: ')
    cpf = input('Cpf do usuário: ') 

    for usuário in lista:
        if usuário['Nome'] == nome:
            print('O usuário já está cadastrado.')
            return

    usuário = {
        'Nome': nome,
        'Idade': idade,
        'Cpf': cpf
    }

    lista.append(usuário)
    print(f'O usuário {nome} foi cadastrado. ')

def editar():
    nome = input('Digite o usuário que deseja editar: ')
    for usuário in lista:
        if usuário['Nome'] == nome:
            novonome = input('Novo nome: ')
            novaidade = input('Nova idade: ')
            novocpf = input('Novo cpf: ')
            usuário['Nome'] = novonome
            usuário['Idade'] = novaidade
            usuário['Cpf'] = novocpf
            print(f'O usuário {nome} foi editado.')

def excluir():
    nome = input('Digite o usuário para excluir: ')
    for usuário in lista:
        if usuário['Nome'] == nome:
            lista.remove(usuário) 
            print(f'O usuário {nome} foi removido.')

def listar():
    if lista:
        print('Usuários cadastrados: ')
        for i, usuário in enumerate(lista, start=1):
            print(f'{i}, Nome: {usuário['Nome']}, Idade: {usuário['Idade']}, Cpf: {usuário['Cpf']}')


while True:
    print('1. Cadastrar usuário')
    print('2. Editar usuário')
    print('3. Remover usuário')
    print('4. Listar usuários')
    print('5. Sair')

    opcao = input('Digite um número: ')
        
    if opcao == '1':
        cadastro()

    elif opcao == '2':
        editar()

    elif opcao == '3':
        excluir()

    elif opcao == '4':
        listar()

    elif opcao == '5':
        print('Saindo')
        break 