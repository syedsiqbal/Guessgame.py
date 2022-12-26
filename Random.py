import random

# Generate a random number between 1 and 10
secret_num = random.randint(1, 10)

# Continue looping until the user guesses the correct number
while True:
  # Ask the user to enter a guess
  guess = int(input("Enter a guess: "))
  
  # Check the guess against the secret number
  if guess > secret_num:
    print("Too high, try a lower number.")
  elif guess < secret_num:
    print("Too low, try a higher number.")
  else:
    print("You guessed it! You win!")
    break
    
# Thank the user for playing
print("Thanks for playing!")
