def main():
    name = input("Provide name in camelCase: ")
    print(convert_snake_case(name))

def convert_snake_case(name):
    result = ""
    for letter in name:
        if letter.isupper():
            result += "_"
            result += letter.lower()
        else:
            result += letter
    return result

main()
