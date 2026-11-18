# Towers of Hanoi

def tower_of_hanoi(n, source, auxiliary, destination):

    if n == 1:
        print("Move disk 1 from", source, "to", destination)
        return

    # Move n-1 disks to auxiliary rod
    tower_of_hanoi(n - 1, source, destination, auxiliary)

    # Move largest disk to destination
    print("Move disk", n, "from", source, "to", destination)

    # Move n-1 disks to destination rod
    tower_of_hanoi(n - 1, auxiliary, source, destination)


# Main Program
n = int(input("Enter the number of disks: "))

if n <= 0:
    print("Enter a positive number!")
else:
    print("Steps to solve Towers of Hanoi:")
    tower_of_hanoi(n, 'A', 'B', 'C')

    print("Total moves:", 2**n - 1)
