# Planets Database

planets = [
    "Mercury",
    "Venus",
    "Earth",
    "Mars",
    "Jupiter",
    "Saturn",
    "Uranus",
    "Neptune"
]

# Function to display all planets
def display_planets():
    print("\nPlanets in Solar System:")

    for planet in planets:
        print(planet)


# Function to search a planet
def search_planet():
    name = input("Enter Planet Name: ")

    if name.capitalize() in planets:
        print(name, "is present in the database.")
    else:
        print(name, "is not present in the database.")


# Function to add a planet
def add_planet():
    name = input("Enter Planet Name: ").capitalize()

    if name in planets:
        print("Planet already exists!")
    else:
        planets.append(name)
        print("Planet added successfully!")


# Main Program
while True:

    print("\n--- PLANETS DATABASE ---")
    print("1. Display Planets")
    print("2. Search Planet")
    print("3. Add Planet")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        display_planets()

    elif choice == '2':
        search_planet()

    elif choice == '3':
        add_planet()

    elif choice == '4':
        print("Exiting Program...")
        break

    else:
        print("Invalid Choice!")
