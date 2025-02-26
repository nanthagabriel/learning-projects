# Cost of a bottle of coke
coca_cola = 50

# Loop until cost of coke is paid (coca_cola <= 0)
while coca_cola > 0:
    print("Amount Due:", coca_cola)

    # Get user to insert amount of coins
    coins = int(input("Insert Coin: "))

    # Check for 25, 10, and 5 cents
    if coins in [25, 10, 5]:
        # Subtract input from cost of coke
        coca_cola -= coins
    else:
        print("Invalid coin. Please insert 5, 10, or 25 cents.")

# Calculate the change to be returned if amount paid exceeds cost
change = abs(coca_cola)

# Change to be returned
print("Change Owed:", change)