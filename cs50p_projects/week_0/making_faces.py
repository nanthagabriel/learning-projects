# - MAKING FACES

# Replace :) and :( with 🙂 and 🙁 respectively
def convert(text):
    text = text.replace(':)', '🙂')
    text = text.replace(':(', '🙁')
    return text

# Prompt user for input
def main():
    user = input()

    # Convert :) and :( from user input
    output = convert(user)
    # Result

    print(output)

# Call main
main()