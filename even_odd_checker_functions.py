def get_integer_input():
    """Gets an integer input from the user."""

    num = int(input("Enter an integer: "))
    return num


def check_even_odd(number):
    """Checks if a number is even or odd and returns a message."""
    result = f"{number} is an "

    if number % 2 == 0:
        result += "Even number."
    else:
        result += "Odd number."


# Main program flow
print(check_even_odd(get_integer_input()))