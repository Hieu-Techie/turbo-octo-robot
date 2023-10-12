#Trò chơi đoán số
import random

secret_number = random.randint(1, 100)
guess = 0
num_guesses = 0

print("I'm thinking of a number between 1 and 100. Can you guess what it is?")

while guess != secret_number:
    try:
        guess = int(input("Enter your guess: "))
    except ValueError:
        print("Invalid input. Please enter a number.")
        continue
    
    num_guesses += 1
    
    if guess < secret_number:
        print("Too low! Try again.")
    elif guess > secret_number:
        print("Too high! Try again.")
    else:
        print(f"Congratulations! You guessed the number in {num_guesses} tries.")