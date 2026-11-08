"""Greets the user and tells them the year they were born.

Input:
    The user's name, read as a string from keyboard input.
    The user's age, read as an integer from keyboard input.

Process:
    Subtract the user's age from the current year to find the birth year.

Output:
    A greeting printed to the screen with the user's name and birth year.

Typical usage example:
    What is your name? Alex
    How old are you? 24
    Hello Alex! You were born in 2002.
"""

from datetime import date

CURRENT_YEAR = date.today().year


def main():
    """Run the name-age program."""
    name = input("What is your name? ")
    age = int(input("How old are you? "))
    birth_year = CURRENT_YEAR - age
    print("\nHello " + name + "! You were born in " + str(birth_year) + ".")


if __name__ == "__main__":
    main()
