############## Hangman ################

import random
from hangman_words import word_list
from hangman_art import logo, stages

# display encrypted word, with dashes
def encrypt_word(word, guessed):
    return ''.join([letter if letter in guessed else '_' for letter in word])


def game():
    print(logo)
    chosen_word = random.choice(word_list)
    lives = 6

    print(stages[lives])
    print(f"You have {lives} attempts.\n")
    print(f"The word is {len(chosen_word)} letters long.\n")

    guessed_letters = set()

    while lives > 0:
        print(encrypt_word(chosen_word, guessed_letters))
        letter = input("Enter a letter: ").lower()

        # Already guessed
        if letter in guessed_letters:
            print("You've already guessed that letter!\n")
            continue

        guessed_letters.add(letter)

        # Wrong guess
        if letter not in chosen_word:
            lives -= 1
            print("Wrong! Letter not in word.")
            print(stages[lives])
            print(f"Lives remaining: {lives}\n")

        # Check win
        encrypted = encrypt_word(chosen_word, guessed_letters)
        if "_" not in encrypted:
            print(encrypted)
            print(" Congratulations! You guessed the word!")
            return

    print(f"\n You lost! The word was: {chosen_word}")


# Main loop
while True:
    game()
    again = input("\nPlay again? (yes/no): ").lower()
    if again != 'yes':
        break