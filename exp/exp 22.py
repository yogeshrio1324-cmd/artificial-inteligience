# Bird Database - Can Fly or Cannot Fly

# List of birds that can fly
can_fly = [
    "parrot",
    "pigeon",
    "crow",
    "eagle",
    "sparrow"
]

# List of birds that cannot fly
cannot_fly = [
    "penguin",
    "ostrich",
    "kiwi",
    "emu"
]


# Function to check bird
def check_bird(bird):

    bird = bird.lower()

    if bird in can_fly:
        print(bird.capitalize(), "can fly.")

    elif bird in cannot_fly:
        print(bird.capitalize(), "cannot fly.")

    else:
        print("Bird information not available.")


# Main Program
print("BIRD DATABASE")
bird = input("Enter the bird name: ")

check_bird(bird)
