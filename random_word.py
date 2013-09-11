import random
from assets import HANGMANPICS

# absolute path within pythonanywhere
dictPath = '/home/eruji/Dropbox/PythonAnywhere/Hangman/dict.txt'

secretWord = random.choice(open(dictPath).readlines())
print secretWord

print HANGMANPICS[0]

alreadyGuessed = ''

print ' _ ' * len(secretWord)

guess = raw_input('guess a letter: ')
guess = guess.lower()

if len(guess) != 1:
    print ('Please enter a single letter')
elif guess in alreadyGuessed:
    print ('You have already guessed that letter')
elif guess not in 'abcdefghijklmnopqrstuvwxyz':
    print ('Please enter a LETTER')
else:
    print guess
