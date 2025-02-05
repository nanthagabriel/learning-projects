# Basic Arithmetic Calculator -> calculate the (+, -, * or /) between two numbers.

# User input of first and second numbers 
num1 = float(input("Enter first number: "))
print(f"Your first number is: {num1}")
num2 = float(input("Enter second number: "))
print(f"Your second number is: {num2}")


# Loop until valid corresponding number is picked.
while True: 
   
    # Display the choice of operations with corresponding numbers.
    print("\nChoose an operation:")
    print("1. Add (+)")
    print("2. Subtract (-)")
    print("3. Multiply (*)")
    print("4. Divide (/)")

    # User input of a number corresponding to the choice of the 4 listed operations.
    operation = input("\nEnter one of the corresponding operator numbers: ")

    # Corresponding operations
    if operation == '1':
        result = num1 + num2
        print(f"\nThe result of {num1} + {num2} is: {result}")
        break  
    elif operation == '2':
        result = num1 - num2
        print(f"\nThe result of {num1} - {num2} is: {result}")
        break  
    elif operation == '3':
        result = num1 * num2
        print(f"\nThe result of {num1} * {num2} is: {result}")
        break  
    elif operation == '4':
       
        # Error if user picks '0' as 'num2' for a division.
        if num2 == 0:
            print("\nERROR, You can't divide by zero.")
        else:
            result = num1 / num2
            print(f"\nThe result of {num1} / {num2} is: {result}")
        break  
    else:
       
        # If user input is any other choice besides the given numbers corresponding with the operators.
        print("\nInvalid choice. Please choose a valid operation.")