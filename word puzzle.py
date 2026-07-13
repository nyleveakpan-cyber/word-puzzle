# Creativity addition: The program randomly selects a secret word from a list,
# allowing the game to have a different word each time it runs.

import random

print("Welcome to the word guessing game!")

# List of possible secret words
words = ["mosiah", "temple", "nephi", "church", "faith"]

# Choose a random secret word
secret_word = random.choice(words)

guess_count = 0

# Generate the initial hint using a loop
hint = ""
for letter in secret_word:
    hint += "_ "

print("\nYour hint is:", hint)

guess = ""

# Continue looping until the correct guess is made
while guess != secret_word:
    guess = input("What is your guess? ").lower()
    guess_count += 1

    # Check if the guess has the same number of letters
    if len(guess) != len(secret_word):
        print("Sorry, the guess must have the same number of letters as the secret word.\n")
        continue

    # Check if guess is correct
    if guess == secret_word:
        print("Congratulations! You guessed it!")
        print(f"It took you {guess_count} guesses.")
        break

    # Create hint
    hint = ""

    for i in range(len(secret_word)):
        if guess[i] == secret_word[i]:
            # Correct letter and correct position
            hint += guess[i].upper() + " "
        elif guess[i] in secret_word:
            # Correct letter but wrong position
            hint += guess[i].lower() + " "
        else:
            # Letter not in secret word
            hint += "_ "

    print("Your hint is:", hint)