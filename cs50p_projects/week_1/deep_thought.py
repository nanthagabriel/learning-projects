# - DEEP THOUGHT
# User input of answer to question.
deep_thought = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ").strip().lower()

# Display 'Yes' if user's pick matches the choices listed or else Display a 'No'.
match deep_thought:
    case "42" | "forty-two" | "forty two":
        print("Yes")
    case _:
        print("No")