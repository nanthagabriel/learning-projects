# Mind Reader -> You have 10 attempts to guess a number between 1 and 99. Are you a mind reader? 

import random

# Generate a random number to guess.
secret_number = random.randint (1, 99)

# Greeting
print("I'm thinking of a number between 1 and 99.")

# The maximum number of attempts given to the user.
max_num_of_attempts = 10
num_of_attempts = 0


# User input of guesses. 
guess = int(input(f"Can you guess what number it is? .. I'll give you {max_num_of_attempts} attempts. Go : ")) 

# Loop till '10' attempts are over. 
while guess != secret_number and num_of_attempts < max_num_of_attempts:
    
    # Clues are given to narrow down the user's guesses. 
    if guess < secret_number:
        print("no no no .. that's too low")
    else :
        print(" aye yai yai  .. thats too high")

    # Plus '1' every time the user fails an attempt.
    num_of_attempts += 1

    # Calculate the remaining attempts left.
    remaining_attempts = max_num_of_attempts - num_of_attempts

    # Show of the number of attempts taken and the user input for another guess.
    if num_of_attempts < max_num_of_attempts:
         guess = int(input(f"\nDon't give up! .. You have {remaining_attempts} attempts left .. C'mon now make another guess! : "))
    
    # After '10' failed attempts, the secret number is revealed.
    else:
         print(f"Oh well, i guess you're not a mind reader, the number i was thinking of was {secret_number}. ")
         break

# Congratulate the user and reveal how attempts was taken to narrow down to the answer. 
if guess == secret_number:
    print(f"Boomz!, You're right! it's {secret_number}. Not bad!, you guessed it in {num_of_attempts} attempts!")
