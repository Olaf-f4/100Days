import random
import re

hangman_Ascii = ['''
  +---+
  |   |
      |
      |
      |
      |
===========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
===========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
===========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
===========''', r'''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
===========''', r'''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
===========''', r'''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
===========''']

# Word bank of animals
words = ('ant baboon badger bat bear beaver camel cat clam cobra cougar '
         'coyote crow deer dog donkey duck eagle ferret fox frog goat '
         'goose hawk lion lizard llama mole monkey moose mouse mule newt '
         'otter owl panda parrot pigeon python rabbit ram rat raven '
         'rhino salmon seal shark sheep skunk sloth snake spider '
         'stork swan tiger toad trout turkey turtle weasel whale wolf '
         'wombat zebra ').split()

word = random.choice(words).lower()
underscore_Generate = ""
for x in word:
    underscore_Generate += "_"

underscore_Generate = [i for i in underscore_Generate]
word_split = [i for i in word]
letter_storage = ""
positions = ""

errors = 0
while errors <= 5 and underscore_Generate != word_split:
    print(f"{hangman_Ascii[0 + errors]}\t\t\tWord -> {underscore_Generate}")
    print(f"\nWelcome to hangman!\nYou have {6 - errors} guesses before you lose. Good luck!")
    user_guess = input("Guess: ").lower()

    if user_guess in word:
        print("Correct! Good guess.")
    else:
        errors += 1

    # Get letter in List
    for position in range(len(word)):
        letter = word[position]
        if letter == user_guess:
            underscore_Generate[position] = letter

    # for c in user_guess:
    #     if c in word:
    #         for idx, x in enumerate(word):
    #             if x == user_guess:
    #                 underscore_Generate[idx] = user_guess
    #         print(underscore_Generate)
    #         print("Nice you got one!")
    #         word.find(c)
    #     else:
    #         errors += 1

if underscore_Generate == word_split:
    print(f"You win! The word was {word}.")
else:
    print(f"{hangman_Ascii[0 + errors]}\nGame Over! You Loser!")

#    for user_guess in word:


# for position in range(len(word)):
#     letter = word[position]
#     if letter == user_guess:
#         ...[position] = letter
#
# Much better for loop to get position in list, then compare if letter == user_guess
# Much much better






