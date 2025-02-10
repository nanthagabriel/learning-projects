# - HOME FEDERAL SAVINGS BANK
# User input with greeting message
greeting = input("Greeting: ").strip().lower()

# Conditions
if greeting.startswith("hello") or greeting.startswith("Hello Newman"):
    print("$0")
elif greeting.startswith("h"):
    print("$20")
else:
    print("$100")