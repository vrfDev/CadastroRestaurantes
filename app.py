import os


restaurantes = [{'nome': 'Yume', 'categoria' : 'Japonês', 'ativo': 'false'}, 
                {'nome': 'Los Hermanos', 'categoria' : 'Mexicano', 'ativo': 'True'},
                {'nome': 'Divino Fogão', 'categoria' : 'Brasileiro', 'ativo': 'True'}]


def menu():
    input("\nDigite uma tecla para voltar ao menu principal: ")
    main()


def exibir_nome_do_programa():
    print("𝕊𝕒𝕓𝕠𝕣 𝔼𝕩𝕡𝕣𝕖𝕤𝕤\n") # fsymbols -> Site para mudar a fonte


def exibir_opcoes():
    print('1. Cadastrar restaurante')
    print('2. Listar restaurantes')
    print('3. Alternar estado do restaurante')
    print('4. Sair\n')

def finalizar_app():
    exibir_subtitulo("Finalizando o app")

def opcao_invalida():
    print("Opção Inválida!")
    

def exibir_subtitulo(msg):
    os.system('cls')
    print(msg)
    print('-' * 30)


def cadastrar_novo_restaurante():
    exibir_subtitulo("Cadastro de novos restaurantes")
    nome_do_restaurante = input("\nDigite o nome do restaurante que deseja cadastrar\n-> ")
    categoria = input(f"\nDigite o nome da catergoria do restaurante {nome_do_restaurante}: ")
    dados_do_restaurante = {'nome': nome_do_restaurante, 'categoria': categoria, 'ativo': False}
    restaurantes.append(dados_do_restaurante)
    print(f"\nO(a) restaurante {nome_do_restaurante} foi cadastrado com sucesso!!")
    print('-' * 15)
    menu()


def listar_restaurantes():
    exibir_subtitulo("Listando os restaurantes")
    
    print(f"{'\nNome do restaurante'.ljust(23)} | {'Categoria'.ljust(20)} | Status")
    for restaurante in restaurantes:
        nome_restaurante = restaurante['nome'] 
        categoria = restaurante['categoria']
        ativo = 'ativado' if restaurante['ativo'] else 'desativado  '
        print(f"- {nome_restaurante.ljust(20)} | {categoria.ljust(20)} | {ativo}")

    menu()


def alternar_estado_restaurante():
    exibir_subtitulo("Alterando estado do restaurante")
    nome_restaurante = input("Digite o nome do restaurante que deseja alternar o estado: ")
    restaurante_encontrado = False

    for restaurante in restaurantes:
        if nome_restaurante == restaurante['nome']:
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo']
            mensagem = f"O restaurante {nome_restaurante} foi ativado com sucesso" if restaurante['ativo'] else f'O restaurante {nome_restaurante} foi desativado com sucesso'
            print(mensagem)
        
    if not restaurante_encontrado:
        print("O restaurante não foi encontrado")

    menu()



 

def escolher_opcao():
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))
        # opcao_escolhida = int(opcao_escolhida)

        if opcao_escolhida == 1: 
            cadastrar_novo_restaurante()
        elif opcao_escolhida == 2: 
            listar_restaurantes()
        elif opcao_escolhida == 3: 
            alternar_estado_restaurante()
        elif opcao_escolhida == 4: 
            finalizar_app()
        else: 
            opcao_invalida()
    except:
        opcao_invalida()

def main():
    os.system('cls')
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()

if __name__ == '__main__':
    main()