import random

HANGMAN_PICS = ['''
+---+
  |
  |
  |
 ===''', '''
+---+
  O  |
     |
     |
 ===''', '''
+---+
  O  |
  |  |
     |
 ===''', '''
+---+
  O  |
 /|  |
     |
 ===''', '''
+---+
  O  |
 /|\\ |
     |
 ===''', '''
+---+
  O  |
 /|\\ |
 /   |
 ===''', '''
+---+
  O  |
 /|\\ |
 / \\ |
 ===''']

words = '''Amarelo Amiga Amor Ave Aviao Avo Balao Bebe
 Bolo Branco Cama Caneca Celular Clube Copo Doce Elefante
 Escola Estojo Faca Foto Garfo Geleia Girafa Janela Limonada
 Mae Meia Noite oculos onibus Ovo Pai Pao Parque Passarinho
 Peixe Pijama Rato Umbigo'''.split()


def getRandomWord(wordList):
    # This function returns a random string from the passed
    # list of strings
    wordIndex = random.randint(0, len(wordList) - 1)
    return wordList[wordIndex].lower()


def displayBoard(missedLetters, correctLetters, secretWord):
    print(HANGMAN_PICS[len(missedLetters)])
    print()

    print('Letras erradas:', end=' ')
    for letter in missedLetters:
        print(letter, end=' ')
    print()

    blanks = '_' * len(secretWord)

    for i in range(len(secretWord)):        # Replace blanks with correctly
        if secretWord[i] in correctLetters:  # guessed letters.
            blanks = blanks[:i] + secretWord[i] + blanks[i+1:]

    for letter in blanks:      # Show the secret word with spaces in between
        print(letter, end=' ')  # each letter
    print()


def getGuess(alreadyGuessed):
    # Return the letter the player entered. This funciton makes sure the
    # player entered a single letter and not somehing else.
    while True:
        print('Adivinhe uma letra.')
        guess = input().lower()
        if len(guess) != 1:
            print('Por favor entre com uma única letra.')
        elif guess in alreadyGuessed:
            print('Você já escolheu este letra. Escolha novamente.')
        elif guess not in 'abcdefghijklmnopqrstuvwxyz':
            print('Por favor entre com uma LETRA.')
        else:
            return guess


def playAgain():
    # This function returns True if the player wants to play again;
    # otherwise, it returns False.
    print('Você gostaria de jogar novamente? (sim ou não)')
    return input().lower().startswith('s')


def main():
    print('F O R C A')
    missedLetters = ''
    correctLetters = ''
    secretWord = getRandomWord(words)
    gameIsDone = False

    while True:
        displayBoard(missedLetters, correctLetters, secretWord)

        # Let the player enter a letter.
        guess = getGuess(missedLetters + correctLetters)

        if guess in secretWord:
            correctLetters += guess

            # Check if the player has won.
            foundAllLetters = True
            for i in range(len(secretWord)):
                if secretWord[i] not in correctLetters:
                    foundAllLetters = False
                    break
            if foundAllLetters:
                print(
                    f'Sim! A palavra secreta é {secretWord}! Você ganhou')
                gameIsDone = True
        else:
            missedLetters += guess

            # Check if player has guessed too many times and lost.
            if len(missedLetters) == len(HANGMAN_PICS) - 1:
                displayBoard(missedLetters, correctLetters, secretWord)
                print(f'''Você não mais tentativas!\n
Depois {str(len(missedLetters))} tentativas perdidas e
 {str(len(correctLetters))} a palavra foi "{secretWord}"''')
                gameIsDone = True

        # Ask the palyer if they want to play again
        # (but only if the game is done).
        if gameIsDone:
            if playAgain():
                missedLetters = ''
                correctLetters = ''
                gameIsDone = False
                secretWord = getRandomWord(words)
            else:
                break


if __name__ == '__main__':
    main()
