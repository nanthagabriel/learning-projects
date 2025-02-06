# - EINSTEIN

# Prompt the user for mass as an integer in kilograms
def main():
    mass = int(input("Enter an integer in kilograms: "))

    # Define c as the speed of light
    c = 300000000

    # Define energy by calculating the user's input times the speed of light squared
    energy = mass * c * c

    # Result
    print(energy)
    
# Call main
main()