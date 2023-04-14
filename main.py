# Hangman
from data import *
import random

# Print Hangman Banner
print(logo)

# Select a random word
word_to_guess = random.choice(word_list)

# Create a list to store output
answer = ["_" for _ in word_to_guess]

# Variable to check if game is on
game_on = True
lives = 6
guessed = []

while game_on:
    print("\n\n")
    # Check if attempts are left
    if lives == 0:
        print("You have run out of lives! The correct word was:", word_to_guess)
        break

    print("Current State: ", " ".join(answer))
    letter = input("Guess a letter: ").lower()

    # Check if the letter is already guessed
    if letter in guessed:
        print("You've already guessed this letter.")
        continue
    else:
        guessed.append(letter)

    # Check if letter is not in the word
    if letter not in word_to_guess:
        print("Incorrect Guess.")
        lives -= 1
        print(stages[6-lives])
        print(f"Remaining Attempts: {lives}")
        continue

    # Rest of the code works only when a correct letter is guessed
    print("Nice Guess!")
    for i in range(0, len(word_to_guess)):
        if letter == word_to_guess[i]:
            answer[i] = letter

    if "_" not in "".join(answer):
        print(f"Congratulations! You have guessed the word {word_to_guess}.")
        game_on = False
