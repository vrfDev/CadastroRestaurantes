import os


restaurantes = [{'nome: Yume', 'categoria : Japonês', 'ativo: false'}, 
                {'nome: Los Hermanos', 'categoria : Mexicano', 'ativo: True'},
                {'nome: Divino Fogão', 'categoria : Brasileiro', 'ativo: True'}]


def menu():
    input("Digite uma tecla para voltar ao menu principal: ")
    main()


def exibir_nome_do_programa():
    print("𝕊𝕒𝕓𝕠𝕣 𝔼𝕩𝕡𝕣𝕖𝕤𝕤\n") # fsymbols -> Site para mudar a fonte


def exibir_opcoes():
    print('1. Cadastrar restaurante')
    print('2. Listar restaurantes')
    print('3. Ativar restaurante')
    print('4. Sair\n')

def finalizar_app():
    exibir_subtitulo("Finalizando o app")

def opcao_invalida():
    print("Opção Inválida!")
    

def exibir_subtitulo(msg):
    os.system('cls')
    print(msg)
    print


def cadastrar_novo_restaurante():
    exibir_subtitulo("Cadastro de novos restaurantes")
    print('-' * 30)
    nome_do_restaurante = input("\nDigite o nome do restaurante que deseja cadastrar\n-> ")
    restaurantes.append(nome_do_restaurante)
    print(f"\nO(a) restaurante {nome_do_restaurante} foi cadastrado com sucesso!!")
    print('-' * 15)
    menu()


def listar_restaurantes():
    exibir_subtitulo("Listando os restaurantes")
    print('-' * 30)
    for i in range(len(restaurantes)):
        print(f"{i + 1}° - {restaurantes[i]}")
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
            print('Ativar restaurante')
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