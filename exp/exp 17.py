# Sum of integers from 1 to N

def sum_n(n):
    if n == 0:
        return 0
    else:
        return n + sum_n(n - 1)


# Main Program
n = int(input("Enter the value of N: "))

if n >= 0:
    result = sum_n(n)
    print("Sum =", result)
else:
    print("Please enter a positive integer")
