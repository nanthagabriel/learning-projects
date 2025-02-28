def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

# WRITE FROM HERE
def is_valid(s):

    # Input requirement to be between 2 and 6 characters
    if not (2 <= len(s) <= 6):
        return False

    # Check if input only contain letters and numbers
    if not s.isalnum():
        return False

    # Check if first two characters are letters
    if not (s[0].isalpha() and s[1].isalpha()):
        return False

    # Look for the first number and check the number rules
    for i in range(len(s)):
        if s[i].isdigit():

            # Check if the first number is 0 which is invalid
            if s[i] == '0' and i == 2:
                return False

            # Check if there are numbers are after letters
            if i > 1 and s[i:].isdigit():
                return True
            return False

    # Valid if no numbers found
    return True

main()