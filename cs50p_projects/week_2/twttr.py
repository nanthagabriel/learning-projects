# User input
answer = input("Input: ")

# Output
print("Output: ", end="")

# Loop each letter from user input
for letter in answer:

    # Check if input has vowels regardless upper or lowercase
    if letter.lower() not in ['a', 'e', 'i', 'o', 'u']:
        print(letter, end="")

# New line
print()
