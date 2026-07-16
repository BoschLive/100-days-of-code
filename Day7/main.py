###############################################
##                  HANGMAN                  ##
## Guessing game in which user attempts      ##
## to guess hidden word one letter at a time.##
## Incorrect guesses add "parts" to the man  ##
## and getting all of the man is a loss.     ##
##                                           ##
## all art by phillipai on GitHub            ##
###############################################
import random
from wordlist import wordlist

print('''
█░█░█ █▀▀ █░░ █▀▀ █▀█ █▀▄▀█ █▀▀   ▀█▀ █▀█ ▀
▀▄▀▄▀ ██▄ █▄▄ █▄▄ █▄█ █░▀░█ ██▄   ░█░ █▄█ ▄

██╗░░██╗░█████╗░███╗░░██╗░██████╗░███╗░░░███╗░█████╗░███╗░░██╗
██║░░██║██╔══██╗████╗░██║██╔════╝░████╗░████║██╔══██╗████╗░██║
███████║███████║██╔██╗██║██║░░██╗░██╔████╔██║███████║██╔██╗██║
██╔══██║██╔══██║██║╚████║██║░░╚██╗██║╚██╔╝██║██╔══██║██║╚████║
██║░░██║██║░░██║██║░╚███║╚██████╔╝██║░╚═╝░██║██║░░██║██║░╚███║
╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░╚══╝░╚═════╝░╚═╝░░░░░╚═╝╚═╝░░╚═╝╚═╝░░╚══╝''')

# Art to display the hangman's state
art = ['''
  +---+
  |   |
  O   |
 /|\\  |
 / \\  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

# word list and random selection of word

word = random.choice(wordlist)

# initialize to keep track of correct letters and letters guessed
blank_word = []
answer = ""
guessed_letters = []

# initialize to keep track of lives and hangman's state
lives = 6
game_over = False

for letter in word:
    blank_word.append("_")

for item in blank_word:
    answer += item

while not game_over: # Loop until entire word is guessed or the hangman dies
    # Each round should begin by displaying the hangman's state and the current state of the mystery word.
    print(art[lives])
    print(f"Word to be guessed: {answer}\n")
    current_guess = input("Guess a letter: ").upper()
    print(f"You have guessed: {current_guess}\n")

    if current_guess in guessed_letters: # check if letter has already been guessed
        print(f"You have already guessed {current_guess}\n")

    elif current_guess in word: # check if this guess is correct
        print(f"Correct! {current_guess} is in the word!\n")
        # place the letter in the correct position in the mystery word
        i = 0
        for letter in word:
            if current_guess == letter:
                blank_word[i] = current_guess
            i += 1

    else: # incorrect guess or invalid input
        print(f"Incorrect! {current_guess} is not in the word!\n")
        lives -= 1

    answer = ""
    for item in blank_word:
        answer += item

    # add the guess to our list of guessed letters
    guessed_letters.append(current_guess)

    if lives == 0: # Player is out of guesses
        game_over = True
        print("You Lost! ")
        print(art[0])

    if answer == word: # Player has guessed every letter in the word
        game_over = True
        print("You Won! \n")

print(f"The word was {word}! \n")