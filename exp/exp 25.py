# Monkey Banana Problem

# Initial State
monkey = "door"
box = "window"
monkey_status = "onfloor"
banana = "not_grabbed"


def monkey_banana():

    global monkey, box, monkey_status, banana

    print("Initial State:")
    print("Monkey is at", monkey)
    print("Box is at", box)
    print("Monkey is on floor")
    print("Banana is not grabbed")

    # Step 1: Monkey moves to box
    print("\nStep 1: Monkey moves towards the box")
    monkey = box

    # Step 2: Monkey pushes box
    print("Step 2: Monkey pushes the box under bananas")
    box = "center"
    monkey = "center"

    # Step 3: Monkey climbs the box
    print("Step 3: Monkey climbs onto the box")
    monkey_status = "onbox"

    # Step 4: Monkey grabs bananas
    print("Step 4: Monkey grabs the bananas")
    banana = "grabbed"

    # Final State
    print("\nFinal State:")
    print("Monkey is at:", monkey)
    print("Box is at:", box)
    print("Monkey is:", monkey_status)
    print("Banana is:", banana)

    if banana == "grabbed":
        print("\nSuccess! Monkey got the bananas.")


# Main Program
monkey_banana()
