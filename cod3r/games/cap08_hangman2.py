import random
import unidecode

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
 ===''', '''
+---+
 [O  |
 /|\\ |
 / \\ |
 ===''', '''
+---+
 [O] |
 /|\\ |
 / \\ |
 ===''']

words = {'Cores': unidecode.unidecode('''vermelho laranja amarelo
 verde azul índigo violeta branco preto marrom''').split(),
         'Formas': unidecode.unidecode('''triângulo quadrado retângulo
 círculo elipse losango trapézio chevron pentágono hexágono heptágono
 octógono''').split(),
         'Frutas': unidecode.unidecode('''maçã laranja limão lima pêra
 melancia uva grapefruit cereja banana melão manga morango tomate''').split(),
         'Animais': unidecode.unidecode('''morcego urso castor gato
 puma caranguejo veado cachorro burro pato águia peixe sapo cabra
 sanguessuga leão lagarto macaco alce rato lontra coruja panda
 pitão coelho rato tubarão ovelha skunk lula tigre peru tartaruga
 doninha baleia lobo vombate zebra''').split()}


def getRandomWord(wordDict):
    # This function returns a random string from the passed
    # dictionary of lists of strings and its key.
    # First, randomly select a key from the dictionary:
    wordKey = random.choice(list(wordDict.keys()))

    # Second, randomly select a word from the key's
    # list in the dictionary:
    wordIndex = random.randint(0, len(wordDict[wordKey]) - 1)

    return [wordDict[wordKey][wordIndex], wordKey]


def displayBoard(missedLetters, correctLetters, secretWord,
                 hangman_pics_round):
    print(hangman_pics_round[len(missedLetters)])
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


def difficultyLevel():
    hangman_pics_round = HANGMAN_PICS.copy()
    difficulty = 'A'
    while difficulty not in 'FMD':
        print('''Selecione a dificuldade: F - Fácil, M - Médio, D - Difícil''')
        difficulty = input().upper()

    if difficulty == 'M':
        del hangman_pics_round[8]
        del hangman_pics_round[7]
    if difficulty == 'D':
        del hangman_pics_round[8]
        del hangman_pics_round[7]
        del hangman_pics_round[5]
        del hangman_pics_round[3]
    return hangman_pics_round


def main():
    print('F O R C A')

    missedLetters = ''
    correctLetters = ''
    secretWord, secretSet = getRandomWord(words)
    gameIsDone = False

    hangman_pics_round = difficultyLevel()

    while True:
        print(f'A palavra secreta é do conjunto: {secretSet}')
        displayBoard(missedLetters, correctLetters, secretWord,
                     hangman_pics_round)

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
            if len(missedLetters) == len(hangman_pics_round) - 1:
                displayBoard(missedLetters, correctLetters, secretWord,
                             hangman_pics_round)
                print(f'''Você não mais tentativas!\n
Depois {str(len(missedLetters))} tentativas perdidas e
 {str(len(correctLetters))} correta(s), a palavra foi "{secretWord}"''')
                gameIsDone = True

        # Ask the palyer if they want to play again
        # (but only if the game is done).
        if gameIsDone:
            if playAgain():
                missedLetters = ''
                correctLetters = ''
                gameIsDone = False
                hangman_pics_round = difficultyLevel()
                secretWord, secretSet = getRandomWord(words)
            else:
                break


if __name__ == '__main__':
    main()
