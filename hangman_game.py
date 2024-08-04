#!/usr/bin/env python3

import random

# Word list for the hangman game
word_list = ["ardvark", "baboon", "camel"]

# Generate a random word from the list
random_word = random.choice(word_list)

print(f"Word is {random_word}")

# Create list of "_" based on chosen word
display = []
for letter in random_word:
    display.append("_")

print(f"Word tracker {display}")



while "_" in display:
    # Ask the player to guess a letter
    guess = input("Guess a letter: ").lower()

    # Give a hint based on the letter guessed
    if guess in random_word:
        print("Correct!")
        counter = 0
        for letter in random_word:
            if letter == guess:
                display[counter] = guess
            counter = counter + 1
        print(display)
    else:
        print("Guess gain")

print(f"Game over! You got the word {random_word}")
