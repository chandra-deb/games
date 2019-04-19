import random
HANGMANPICS = ['''

        +---+
         |        |
                  |
                  |
                  |
                  |
==========''', '''

        +---+
         |        |
         0       |
                  |
                  |
                  |
==========''', '''

        +---+
         |        |
         0       |
         |        |
                  |
                  |
==========''', '''

        +---+
         |        |
         0       |
      / |       |
                  |
                  |
==========''', '''

        +---+
         |        |
         0       |
      / |\     |
                  |
                  |
==========''', '''

        +---+
         |        |
         0       |
      / |\     |
       /        |
                  |
==========''', '''

        +---+
         |        |
         0       |
      / |\     |
       /  \    |
                  |
==========''','''

        +---+
         |        |
         0]     |
      / |\     |
       /  \    |
                  |
==========''','''

        +---+
         |        |
       [0]       |
      / |\     |
       /  \    |
                  |
==========''']



    
words = {'Colors' : 'black blue red orange yellow indigo purple white violet white brown'.split(),
         'Shapes' : 'round circle square  triangle rectangle ellipse pentagon hexaon'.split(),
         'Fruits' : 'apple banana orange lime lemon pear watermelon grape grapefruit cherry mango tomato strawberry'.split(),
         'Animals' : 'bear lion tiger fish frog cat dog deer donkey goose lizard mouse moose otter owl panda python rabbit rat'.split()
         }

def getRandomWord(wordDict):
    wordKey = random.choice(list(wordDict.keys()))
    wordIndex = random.randint(0, len(wordDict[wordKey]) - 1)
    return [wordDict[wordKey][wordIndex], wordKey]

def getGuess(alreadyGuessed):
    while True:
        guess = input('Enter a your guess : ').lower()

        if len(guess) != 1:
            print('Enter a letter.')
        elif guess in alreadyGuessed:
            print('You already guessed the letter. Try another.')
        elif guess not in 'abcdefghijklmnopqrstuvwxyz':
            print('You have to enter a letter. No other character allowed!')
        else:
            return guess

def displayBoard(missedLetters, correctLetters, secretWord):
    print(HANGMANPICS[len(missedLetters)])
    print()
    
    print('Missed Letters : ', end = ' ')
    for letter in missedLetters:
        print(letter, end=' ')
    print()

    blanks = '-' * len(secretWord)

    for i in range(len(secretWord)):
        if secretWord[i] in correctLetters:
            blanks = blanks[:i] + secretWord[i] + blanks[i+1:]
            
    for blank in blanks:
        print(blank, end='')
    print()

def playAgain():
    return input('Do You Want To Play Again?(yes or no)').lower().startswith('y')
######################################
difficulty = 'X'

while difficulty not in ['E', 'M', 'H']:
    print('Enter difficulty: E - Easy, M - Medium, H - Hard')
    difficulty = input().upper()

if difficulty == 'M':
    for d in range(8, 6, -1):
        del HANGMANPICS[d]
        
if difficulty == 'H':
    del  HANGMANPICS[8]
    for d in range(7, 2, -2):
        del HANGMANPICS[d]

missedLetters = ''
correctLetters = ''
secretWord, secretSet = getRandomWord(words)
gameIsDone = False

while True:
    print()
    print('The secret word is in the', secretSet)
    displayBoard(missedLetters, correctLetters, secretWord)

    guess = getGuess(missedLetters + correctLetters)

    if guess in secretWord:
        correctLetters = guess + correctLetters

        foundAllLetters = True
        for i in range(len(secretWord)):
            if secretWord[i] not in correctLetters:
                foundAllLetters = False
                break
        if foundAllLetters:
            displayBoard(missedLetters, correctLetters, secretWord)
            print('You have Won The Game! The Word is', secretWord)
            gameIsDone = True
            
    else:
        missedLetters = guess + missedLetters

        if len(missedLetters) == len(HANGMANPICS) -1:
            displayBoard(missedLetters, correctLetters, secretWord)
            print('You loose!', 'The word was', secretWord)
            gameIsDone = True

    if gameIsDone:
        if playAgain():
            missedLetters = ''
            correctLetters = ''
            secretWord, secretSet = getRandomWord(words)
            gameIsDone = False
        else:
            break
            
        
