# Fruit and Its Color Using Backtracking

# Fruit database
fruits = {
    "apple": "red",
    "banana": "yellow",
    "orange": "orange",
    "grapes": "green",
    "mango": "yellow",
    "cherry": "red"
}

# Function to find fruit colors
def fruit_color(color, fruit_list):

    if not fruit_list:
        return

    fruit = fruit_list[0]

    if fruits[fruit] == color:
        print(fruit, "is", color)

    # Backtracking to check next fruit
    fruit_color(color, fruit_list[1:])


# Main Program
print("FRUIT AND COLOR DATABASE")

color = input("Enter a color: ").lower()

print("\nFruits with", color, "color:")

fruit_list = list(fruits.keys())

fruit_color(color, fruit_list)
