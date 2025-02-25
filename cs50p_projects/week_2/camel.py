# User input in camel case format
def main():
    name = input("Provide name in camelCase: ")
    print(convert_snake_case(name))

# Convert camel case to snake case
def convert_snake_case(name):
    result = ""

    # Loop every later from input
    for letter in name:

        # Check for upper case
        if letter.isupper():

            # If input is uppercase, add an underscore before it and convert it to lowercase
            result += "_"
            result += letter.lower()
        else:

            # Add input to result if it's lowercase
            result += letter
    return result

main()
