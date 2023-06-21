import random
secret_number = (1, 10)
next_guesses = set()
playing = True

while playing == True:
   guess = int(input("Guess the secret number (between 1 and 10): "))

   if guess in next_guesses:
        print("You already guessed that number. Try again.")
   elif guess < secret_number:
        next_guesses.add(guess) 
        print("your number is too small, try again.")
   elif guess > secret_number:
        next_guesses.add(guess) 
        print("your number is too large, try again.")   
   else:
        print("good job You guessed the secret number")
        playing = False