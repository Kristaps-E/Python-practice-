import random


def guessing_game():
    """
    Play a number guessing game.

    This function generates a random number between 0 and 100 and asks the
    user to guess it. After each guess, the user is informed whether their
    guess is too high, too low, or correct. If the guess is correct, the user
    is asked if they want to play another round. The game ends if
    the user declines to play again.

    Returns:
        None
    """
    while True:
        number = random.randint(0, 100)

        while True:
            try:
                user_guess = int(input("What's your guess from 0 - 100? "))
            except ValueError:
                print("Please use valid input.")
                continue

            if user_guess == number:
                print(f"Right! The answer is {user_guess}")
                break
            elif user_guess > number:
                print("It's too high! Guess again!")
            elif user_guess < number:
                print("It's too low! Guess again!")

        again = input("Do you want to guess another time? ").strip()
        if "y" not in again.lower():
            break


guessing_game()
