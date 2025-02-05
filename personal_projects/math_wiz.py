# Math Wiz -> Answer randomly generated basic arithmetic equations.

import random

# Generate two random numbers between 1 and 99.
num1 = random.randint (1, 99)
num2 = random.randint (1, 99)

# List of possible operators.
operators = ['+','-','*','/']

# A random operator is chosen.
operator = random.choice(operators)

# Set the variable 
correct_answer = None

# Generate a question based on a random operator.
if operator == '+':
    print(f"What is {num1} + {num2}?")
    correct_answer = num1 + num2
elif operator == '-':
    print(f"What is {num1} - {num2}?")
    correct_answer = num1 - num2
elif operator == '*':
    print(f"What is {num1} * {num2}?")
    correct_answer = num1 * num2
elif operator == '/':
   
    # Prevent dividing by zero error. 
    while num1 % num2 != 0:
        num1 = random.randint (10, 99)
        num2 = random.randint (1, 99)
    print(f"What is {num1} / {num2}.")
    correct_answer = num1 / num2

# User input for answer.
user_answer = int(input("Your answer: "))

# Congratulate the user if the answer is right or else reveal actual answer. 
if user_answer == correct_answer:
    print("Correct!")
else:
    print(f"That's incorrect. The answer is {correct_answer}")                         