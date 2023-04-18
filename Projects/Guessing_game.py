import random

"""def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
        guess = int(input(f"Guess a number between 1 and {x}: "))
        if guess > x:
            print("Sorry, you crossed the range, try the number between range")

        elif guess < random_number:
            print("Sorry, guess again. Too low")
        elif guess > random_number:
            print("Sorry, try again, too high")
        else:
            print(f"You guessed the number {random_number} correctly")
"""

def computer_guess(x):
    low = 1
    high = x
    feedback = ''
    while feedback != 'c':
        if low != high:
                guess = random.randint(low, high)
        else:
            guess = low
        feedback = input(f"Is {guess} too high, too low, or correct: ").lower()
        if feedback == "h":
            high = guess - 1

        elif feedback == "l":
            low = guess + 1


    print(f"The computer guessed your number, {guess} correctly!")

computer_guess(50)

