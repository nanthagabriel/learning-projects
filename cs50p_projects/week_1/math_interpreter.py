# - MATH INTERPRETER
# User input
expression = input("Write an arithmetic expression: ")

# Split spaces in between
x, operator, z = expression.split()

# Set x and z as integers
x = int(x)
z = int(z)

# Operator function corresponding user's input
if operator == "+":
    print(float(x + z))

elif operator == "-":
    print(float(x - z))

elif operator == "*":
    print(float(x * z))

elif operator == "/":
    print(float(x / z))