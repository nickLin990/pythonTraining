numberStringInt = input("guess the secret number \n")
number = int(numberStringInt)
secret_number = (1, 10)
previous_guess = None  
guess_count = 0
next_guesses = set()

nextgenius = 43
while True:
   guess = input("Guess the secret number (between 1 and 10): ")

   if guess in next_guesses:
        print("You already guessed that number. Try again.")
        continue
   next_guesses.add(guess) 
if guess < secret_number:
        print("your number is too small, try again.")
if guess > secret_number:
        print("your number is too large, try again.")   
else:
        print("good job You guessed the secret number")