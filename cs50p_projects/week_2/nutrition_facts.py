# User input of type of fruit
fruit = input("Item: ").strip().title()

# Dictionary of Fruits snd their calorie count based on FDA poster
fruits_calories = {
    "Apple" : "130",
    "Avocado" : "50",
    "Banana" : "110",
    "Cantaloupe" : "50",
    "Grapefruit" : "60",
    "Grapes" : "90",
    "Honeydew Melon" : "50",
    "Kiwifruit" : "90",
    "Lemon" : "15",
    "Lime" : "20",
    "Nectarine" : "50",
    "Orange" : "80",
    "Peach" : "60",
    "Pear" : "100",
    "Pineapple" : "50",
    "Plums" : "70",
    "Strawberries" : "50",
    "Sweet Cherries" : "100",
    "Tangerine" : "50",
    "Watermelon" : "80"
}

# Return calories from the dictionary of fruits
if fruit in fruits_calories.keys():
    print("Calories: ", fruits_calories[fruit])
