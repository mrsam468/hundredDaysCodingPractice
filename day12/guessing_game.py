import random

import art

print(art.logo)
print("welcome to the guessing game!\nI'm thinking of a number from 1 to 100")
actual_number = random.randint(1, 101)
print(actual_number)


def easy(number):
    number_of_time_remaining = 10
    print("you have 10 attempts remaining to guess the number.")
    while number_of_time_remaining > 0:
        make_guess = int(input("Make a guess: "))
        if make_guess == actual_number:
            print(f"you got it! the answer was {make_guess}")
            number_of_time_remaining = 0
        else:
            if make_guess < actual_number:
                if number_of_time_remaining > 1:
                    number_of_time_remaining -= 1
                    print("Too low\nguess again.")
                    print(f"you have {number_of_time_remaining} attempts remaining to guess the number.")
                else:
                    number_of_time_remaining -= 1
                    print("too_low")
                    print("you are out of guess you lose")
            else:
                if number_of_time_remaining > 1:
                    print("Too high\nguess again.")
                    number_of_time_remaining -= 1
                    print(f"you have {number_of_time_remaining} attempts remaining to guess the number.")
                else:
                    number_of_time_remaining -= 1
                    print("too_high")
                    print("you are out of guess you lose")

def difficult(number):
    number_of_time_remaining = 5
    print("you have 5 attempts remaining to guess the number.")
    while number_of_time_remaining > 0:
        make_guess = int(input("Make a guess: "))
        if make_guess == actual_number:
            print(f"you got it! the answer was {make_guess}")
            number_of_time_remaining = 0
        else:
            if make_guess < actual_number:
                if number_of_time_remaining > 1:
                    number_of_time_remaining -= 1
                    print("Too low\nguess again.")
                    print(f"you have {number_of_time_remaining} attempts remaining to guess the number.")
                else:
                    number_of_time_remaining -= 1
                    print("too_low")
                    print("you are out of guesses you lose")
            else:
                if number_of_time_remaining > 1:
                    print("Too high\nguess again.")
                    number_of_time_remaining -= 1
                    print(f"you have {number_of_time_remaining} attempts remaining to guess the number.")
                else:
                    number_of_time_remaining -= 1
                    print("too_high")
                    print("you are out of guesses you lose")

def guesses():
    select_option = input("Choose a difficulty. Type 'easy' or 'hard':").lower()
    if select_option == "easy":
        easy(actual_number)
    else:
        difficult(actual_number)
guesses()