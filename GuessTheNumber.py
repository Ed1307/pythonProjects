import random

def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
        guess = int(input(f"guess number between 1 and {x}:"))
        if guess < random_number:
            print("sorry, guess again. Too low")
        elif guess > random_number:
            print("sorry, guess again. Too high")
    print(f"yay, congrats. You have guessed the number {random_number}")

guess(10)
