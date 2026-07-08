def print_pyramid(current, rows):
    # Base case
    if current > rows:
        return

    # Print one row
    spaces = " " * (rows - current)
    xs = "X " * current
    print(spaces + xs)

    # Recursive call
    print_pyramid(current + 1, rows)


# Driver code
rows = 4
print_pyramid(1, rows)