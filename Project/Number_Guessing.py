############## Guess the number ################


from random import randint

# Function to check user's guess against actual answer.
def check_answer(guess, answer, turns):
    if guess > answer:
        print("Too high. Guess again.\n")
        return turns - 1
    elif guess < answer:
        print("Too low. Guess again.\n")
        return turns - 1
    return -1


# function to set difficulty.
def set_difficulty():
    easy = 10
    hard = 5
    level = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    print()
    if level not in ['easy', 'hard']:
        raise ValueError("Invalid difficulty. Please choose from 'easy' or 'hard': \n")
    if level == "easy":
        return easy
    return hard


def game():
    low_number = 1
    high_number = 100

    print("\nWelcome to the Number Guessing Game!\n")
    print(f"I'm thinking of a number between {low_number} and {high_number}.\n")

    # Choosing a random number between 1 and 100.
    answer = randint(low_number, high_number)

    # Check difficulty level
    difficulty_check = True
    while difficulty_check:
        try:
            turns = set_difficulty()
            difficulty_check = False
        except ValueError as e:
            print(f"\nError: {e}")

    # Repeat the guessing functionality if they get it wrong.
    guess = 0
    while guess != answer:
        print(f"You have {turns} attempts remaining to guess the number.")

        # Let the user guess a number.
        guess = int(input("\nMake a guess: "))

        # Track the number of turns and reduce by 1 if they get it wrong.
        turns = check_answer(guess, answer, turns)
        if turns == -1:
            print(f"You've got it! The answer was {answer}.")
        if turns == 0:
            print("You've run out of guesses, you lose.")
            return


check_for_another_game = True
while check_for_another_game:
    game()

    input_validation = True
    while input_validation:
        another_game = input("\nDo you want to play another game? Enter 'yes' or 'no': ").lower()
        if another_game in ['yes', 'no']:
            input_validation = False

            if another_game == 'no':
                check_for_another_game = False
