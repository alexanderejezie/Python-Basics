import random

print("Welcome to the Guess the Number game!")
print("I'm thinking of a number between 1 and 100. Can you guess what it is?")

# Generate a random number between 1 and 100
secret_number = random.randint(1, 100)

# Initialize the user's guess
guess = None

# Loop until the correct number is guessed
while guess != secret_number:
    # Prompt the player to enter a guess
    guess = int(input("Enter your guess: "))

    # Compare the guess with the secret number
    if guess < secret_number:
        print("Your guess is too low. Guess again.")
    elif guess > secret_number:
        print("Your guess is too high. Guess again.")
    else:
        print("🎉 Congratulations! You guessed the number correctly!")
