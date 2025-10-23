#!/usr/bin/env python3
# Created By: Christopher El-Murr
# Date: 10 23, 2025
# This program asks the user to guess the correct random generated number and
# tells them if the number is correct, incorrect or invalid
import random


def main():
    # generate a random number between 0 and 9
    number_random = random.randint(0, 9)

    try:
        # have the user guess a random number between 0 and 9
        user_guess = input("Guess a number between 0 and 9: ")
        user_guess_int = int(user_guess)

        # if the guess == the random number then display CORRECT! :)
        if user_guess_int == number_random:
            print("CORRECT! :)")
        else:
            print(f"Guess again :( The correct answer was: {number_random}")
        #if the integer is not valid, display ("this is not valid")
    except ValueError:
        print("This is not a valid integer.")
        # display thank you for playing at the end of the program
    finally:
        print("Thanks for playing!")


if __name__ == "__main__":
    main()
