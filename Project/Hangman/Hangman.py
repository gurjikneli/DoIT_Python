############## Hangman ################
import json
import random
from hangman_art import logo, stages

# display encrypted word, with dashes
def encrypt_word(word, guessed):
    return ''.join([letter if letter in guessed else '_' for letter in word])


def game():
    green = "\033[32m"
    red = "\033[31m"
    blue = "\033[34m"
    reset = "\033[0m"
    color_list = [green, red, blue, reset]

    with open("hangman_words.json", "r") as f:
        words_dict = json.load(f)

    print(logo)
    chosen_word = random.choice(list(words_dict.keys()))
    lives = 6

    print(stages[lives])
    print(f"You have {lives} attempts.\n")
    print(f"The word is {len(chosen_word)} letters long.\n")
    print(f"The word is: {words_dict.get(chosen_word)}")

    guessed_letters = set()

    while lives > 0: # თუ ეს ციკლი დასრულდა თავისით (return-ის) გარეშე, ეს აუცილებლად ნიშნავს, რომ მოთამაშეს ცდები ამოეწურა და წააგო.
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
            print(f"{color_list[1]}Wrong! Letter not in word.{color_list[3]}")
            print(stages[lives])
            print(f"Lives remaining: {color_list[1]}{lives}{color_list[3]}\n")

        # Check win
        encrypted = encrypt_word(chosen_word, guessed_letters)
        if "_" not in encrypted:
            print(f"\n****** {color_list[0]}{encrypted.upper()}{color_list[3]} *****")
            print(f"\n{color_list[0]}CONGRATULATIONS! YOU GUESSED THE WORD!{color_list[3]}\n")
            return

    print(f"\n{color_list[1]}YOU LOST! The word was: {color_list[0]}{chosen_word.upper()}{color_list[3]}")  # ამიტომ ვბეჭდავთ ციკლს გარეთ ამ წინადადებას.


# Main loop
while True:
    game()
    while True:
        again = input("\nPlay again? (yes/no): ").lower()
        if again in ['yes', 'no']:
            break
    if again != 'yes':
        break


