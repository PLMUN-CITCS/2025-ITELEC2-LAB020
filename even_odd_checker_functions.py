def get_integer_input():
    """Gets an integer input from the user."""

    num = int(input("Enter an integer: "))
    return num


def check_even_odd(number):
    """Checks if a number is even or odd and returns a message."""

    if number % 2 == 0:
        return f"{number} is an Even number."
    else:
        return f"{number} is an Odd number."


# Main program flow
print(check_even_odd(get_integer_input()))