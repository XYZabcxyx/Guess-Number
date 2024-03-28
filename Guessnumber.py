import random

def guess_the_number():
    number_to_guess = random.randint(1, 100)
    attempts = 0
    max_attempts = 10

    print("Guess the number between 1 and 100.")
    while attempts < max_attempts:
        attempts += 1
        guess = int(input("Enter your guess: "))
        if guess < number_to_guess:
            print("Too low. Try again.")
        elif guess > number_to_guess:
            print("Too high. Try again.")
        else:
            print(f"Congratulations! You guessed the number {number_to_guess} in {attempts} attempts.")
            break
    else:
        print(f"Out of attempts. The number was {number_to_guess}.")

guess_the_number()