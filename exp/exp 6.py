# Vacuum Cleaner Problem

def vacuum_cleaner():

    # Initial room status
    rooms = {
        'A': 'Dirty',
        'B': 'Dirty'
    }

    # Starting position
    location = 'A'

    print("Initial State:")
    print(rooms)

    while 'Dirty' in rooms.values():

        print("\nVacuum Cleaner is in Room", location)

        if rooms[location] == 'Dirty':
            print("Room", location, "is Dirty")
            print("Cleaning Room", location)

            rooms[location] = 'Clean'

        else:
            print("Room", location, "is already Clean")

        # Move to the other room
        if location == 'A':
            location = 'B'
        else:
            location = 'A'

    print("\nAll rooms are Clean!")
    print("Final State:")
    print(rooms)


# Main Program
vacuum_cleaner()
