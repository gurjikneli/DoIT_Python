############## Guess the number ################

from random import randint

# checks answer against guess. Returns the number of turns remaining.
def check_answer(guess, answer, turns, color_list):
    high_low = 'HIGH' if guess > answer else 'LOW' if guess < answer else ''
    if high_low:
        print(f"\nTOO {color_list[1]}{high_low}{color_list[3]}. GUESS AGAIN.\n")
        return turns - 1
    else:
        return turns

    if guess > answer:
        print(f"\nTOO {color_list[1]}HIGH{color_list[3]}. GUESS AGAIN.\n")
        return turns - 1
    elif guess < answer:
        print(f"\nTOO {color_list[1]}LOW{color_list[3]}. GUESS AGAIN.\n")
        return turns - 1
    return turns  # Returns same value of turns if the guess is correct (If player guessed the number)


# Make function to set difficulty.
def set_difficulty(color_list):
    easy = 10
    hard = 5
    level = input(f"CHOOSE A DIFFICULTY. TYPE {color_list[0]}'EASY'{color_list[3]} OR {color_list[0]}'HARD'{color_list[3]}: ").lower()
    print()
    if level not in ['easy', 'hard']:
        raise ValueError(f"INVALID DIFFICULTY. PLEASE CHOOSE FROM {color_list[0]}'easy'{color_list[3]} OR {color_list[0]}'hard'{color_list[3]}: \n")
    if level == "easy":
        return easy
    return hard


def game():
    low_number = 1
    high_number = 100

    green = "\033[32m"
    red = "\033[31m"
    blue = "\033[34m"
    reset = "\033[0m"
    color_list = [green, red, blue, reset]

    print("\n***** WELCOME TO THE NUMBER GUESSING GAME! *****\n")
    print(f"GUESS AN NUMBER BETWEEN {color_list[2]}{low_number}{color_list[3]} AND {color_list[2]}{high_number}{color_list[3]}.\n")

    # Choosing a random number between 1 and 100.
    answer = randint(low_number, high_number)

    # Check difficulty level. Ask player to choose difficulty level and repeat asking until player enters ('easy' or 'hard')
    while True:
        try:
            turns = set_difficulty(color_list)
            break
        except ValueError as e:
            print(f"\nERROR: {e}")

    # Repeat the guessing functionality if they get it wrong.
    guess = 0
    while guess != answer and turns > 0:
        print(f"YOU HAVE {color_list[1]}{turns}{color_list[3]} ATTEMPTS TO GUESS THE NUMBER.")

        # Let the user guess a number and handle invalid input
        while True:
            try:
                guess = int(input("\nMAKE A GUESS: "))
                break  # Exit loop if guess is valid
            except ValueError:
                print(f"{color_list[1]}INVALID INPUT. PLEASE ENTER A NUMBER BETWEEN {low_number} AND {high_number}.{color_list[3]}")

        # Track the number of turns and reduce by 1 if they get it wrong.
        turns = check_answer(guess, answer, turns, color_list)

        if guess == answer:
            print(f"\nYOU'VE GOT IT! THE ANSWER WAS {color_list[0]}{answer}{color_list[3]}.")
        if turns == 0:
            print(f"\n{color_list[1]}YOU'VE RUN OUT OF GUESSES, YOU LOST!{color_list[3]}")



# Main loop for the game
check_for_another_game = True
while check_for_another_game:
    game()

    while True:
        another_game = input("\nDO YOU WANT TO PLAY ANOTHER GAME? ENTER 'YES' OR 'NO': ").lower()
        if another_game in ['yes', 'no']:
            break

    if another_game == 'no':
        check_for_another_game = False
        print("\nEXITING GAME. GOODBYE!")

