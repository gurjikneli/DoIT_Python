############## Hangman ################
import json
import random
from hangman_art import logo, stages


# display encrypted word, with dashes
def encrypt_word(word, guessed):
    return ' '.join([letter if letter in guessed else '_' for letter in word])


def display_lives(lives, tries, color_list):
    print(f"LIVES REMAINING: {color_list[1]}{lives}{color_list[3]}/{color_list[0]}{tries}{color_list[3]}\n")


def menu():
    print(f"\n1 - GUESS THE WORD:")
    print(f"2 - GUESS THE LETTER:\n")
    choice = input("ENTER THE OPTION: ").lower()
    print()
    return choice


def display_win(encrypted, color_list):
        print(f"\n***** {color_list[0]}{encrypted.upper()}{color_list[3]} *****")
        print(f"\n{color_list[0]}CONGRATULATIONS! YOU GUESSED THE WORD!{color_list[3]}\n")


def display_loss(chosen_word, color_list):
    print(f"\n{color_list[1]}YOU'VE LOST!{color_list[3]} THE WORD WAS: {color_list[0]}{chosen_word.upper()}{color_list[3]}")




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
    tries = lives = 6

    print(stages[lives])
    print(f"YOU'VE GOT {color_list[0]}{tries}{color_list[3]} ATTEMPTS TO GUESS THE WORD.\n")
    print(f"LENGTH OF THE WORD: {color_list[2]}{len(chosen_word)}{color_list[3]}")
    print(f"DESCRIPTION: {color_list[0]}{words_dict.get(chosen_word)}{color_list[3]}\n")

    guessed_letters = set()

    # Validation that option is '1' or '2':
    while True:
        options = menu()
        if options in ['1', '2']:
            break

    if options == '1':
        word = input("\nENTER THE WORD: ").lower()
        if word == chosen_word:
            encrypted = word
            display_win(encrypted, color_list)
        else:
            display_loss(chosen_word, color_list)

    elif options == '2':
        while lives > 0: # თუ ეს ციკლი დასრულდა თავისით (return-ის) გარეშე, ეს აუცილებლად ნიშნავს, რომ მოთამაშეს ცდები ამოეწურა და დამარცხდა.
            encrypted = encrypt_word(chosen_word, guessed_letters)
            print(encrypted, '\n')

            # If letter is in alphabet validation
            letter = ''
            while not letter.isalpha():
                letter = input("\nENTER A LETTER: ").lower()

            # Already guessed
            if letter in guessed_letters:
                print("YOU'VE ALREADY GUESSED THAT LETTER!\n")
                display_lives(lives, tries, color_list)
                continue

            guessed_letters.add(letter)

            # Wrong guess
            if letter not in chosen_word:
                lives -= 1
                print(f"{color_list[1]}WRONG! THE LETTER NOT IN THE WORD.{color_list[3]}")
                print(stages[lives])

            # Check win
            encrypted = encrypt_word(chosen_word, guessed_letters)
            display_lives(lives, tries, color_list)

            if "_" not in encrypted:
                display_win(encrypted, color_list)
                return

        # ამიტომ პირდაპირ ვბეჭდავთ ციკლის გარეთ ამ წინადადებას.
        display_loss(chosen_word, color_list)


# Main loop
while True:
    game()
    while True:
        again = input("\nPlay again? (yes/no): ").lower()
        if again in ['yes', 'no']:
            break
    if again != 'yes':
        break


