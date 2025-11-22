def umayrah_calculator():
    try:
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        
        print("Addition:", a + b)
        print("Subtraction:", a - b)
        print("Multiplication:", a * b)
        print("Division:", a / b if b != 0 else "Cannot divide by zero.")

    except:
        print("Invalid input. Please enter numbers again.")

import random

def maryam_guessing_game():
    print("Let's play a guessing game!")
    number = random.randint(1, 50)
    attempts = 0

    while True:
        try:
            guess = int(input("Enter your guess (1-50): "))
            attempts += 1

            if guess < number:
                print("Too low, try again.")
            elif guess > number:
                print("Too high, try again.")
            else:
                print("Well done! You guessed it in " + str(attempts) + " attempts.")
                break
        except:
            print("Invalid input! Enter a number only.")