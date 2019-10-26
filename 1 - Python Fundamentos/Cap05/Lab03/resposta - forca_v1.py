# Hangman Game (Jogo da Forca)
# Programação Orientada a Objetos

# Import
import random

# Board (tabuleiro)
board = ['''

>>>>>>>>>>Hangman<<<<<<<<<<

+---+
|   |
    |
    |
    |
    |
=========''', '''

+---+
|   |
O   |
    |
    |
    |
=========''', '''

+---+
|   |
O   |
|   |
    |
    |
=========''', '''

 +---+
 |   |
 O   |
/|   |
     |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
     |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
/    |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
/ \  |
     |
=========''']


# Classe
class Hangman:

    # Método Construtor
    def __init__(self, word):
        self.palavra = word
        self.letras_certas = []
        self.letras_erradas = []

    # Método para adivinhar a letra
    def guess(self, letter):
        if letter in self.palavra and letter not in self.letras_certas:
            self.letras_certas.append(letter)
        elif letter not in self.palavra and letter not in self.letras_erradas:
            self.letras_erradas.append(letter)

    # Método para verificar se o jogo terminou
    def hangman_over(self):
        if len(self.letras_erradas) >= len(board):
            return True
        return False

    # Método para verificar se o jogador venceu
    def hangman_won(self):
        set_letras_informadas = set(self.letras_certas)
        set_palavra_correta = set(self.palavra)
        return set_letras_informadas == set_palavra_correta

    # Método para não mostrar a letra no board
    def hide_word(self):
        pass

    # Método para checar o status do game e imprimir o board na tela
    def print_game_status(self):
        if 0 < len(self.letras_erradas) < len(board):
            print(board[len(self.letras_erradas)])
        elif len(self.letras_erradas) >= len(board):
            print(board[6])
        else:
            print(board[0])

        # Exibe Letras Corretas
        print("Letras Corretas: ", end='')
        for letra_certa in self.palavra:
            if letra_certa in self.letras_certas:
                print(letra_certa, end='')
            else:
                print("_", end='')
        print()

        # Exibe Letras Erradas
        print("Letras Erradas: ", end='')
        for letra_errada in self.letras_erradas:
            print(letra_errada, end=' ')
        print()


# Função para ler uma palavra de forma aleatória do banco de palavras
def rand_word():
    with open("palavras.txt", "rt") as f:
        bank = f.readlines()
    return bank[random.randint(0, len(bank) - 1)].strip().lower()


# Função Main - Execução do Programa
def main():
    # Objeto
    game = Hangman(rand_word())

    # Enquanto o jogo não tiver terminado, print do status, solicita uma letra e faz a leitura do caracter
    while not game.hangman_won():
        print()
        letra = str(input("Informe uma Letra: ")).lower()[0]
        game.guess(letra)

        # Verifica o status do jogo
        game.print_game_status()
        if game.hangman_over():
            break

    # De acordo com o status, imprime mensagem na tela para o usuário
    if game.hangman_won():
        print('\nParabéns! Você venceu!!')
    else:
        print('\nGame over! Você perdeu.')
        print('A palavra era ' + game.palavra)

    print('\nFoi bom jogar com você! Agora vá estudar!\n')


# Executa o programa
if __name__ == "__main__":
    main()
