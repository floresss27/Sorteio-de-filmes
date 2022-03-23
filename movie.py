import random

def list_movie():
    arquivo = open('Filmes.txt', 'r')
    lista = arquivo.read()
    print(lista)
    menu = input("---- Pressione qualquer tecla para voltar ao menu ----")

def sorteio():
    arquivo = open('Filmes.txt', 'r')
    ler = arquivo.readlines()
    escolhido = random.choice(ler)
    print(escolhido)

def new_movie():
    print('---- Digite o nome do filme que deseja adicionar ----')
    filme = input()
    arquivo = open('Filmes.txt', 'a')
    arquivo.write('%s\n' % filme)
    print('Filme adicionado com sucesso!!!')
    menu = input("---- Pressione qualquer tecla para voltar ao menu ----")

def main():   
    while True:
        print('Sorteador de filmes™')
        print('------------ Menu ------------')                                                                                                        # Mostra as opções do banco.

        print('1 - Adicionar novo filme')
        print('2 - Sortear algum filme')
        print("3 - Ver os filmes que contem")


        escolha = input('Escolha uma das opções acima: ')
        if escolha == '1':
           new_movie()
        if escolha == '2':
            sorteio()
        if escolha == '3':
            list_movie()    
main()