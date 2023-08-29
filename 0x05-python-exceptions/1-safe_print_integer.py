#!/usr/bin/python3
# By - Musonda Christopher
# A Python function that prints an integer with "{:d}".format()
def safe_print_integer(value):
    # Print an integer with "{:d}".format().

    # Arguments:
    # value (int): The integer to print.
    # Returns:
    # If a TypeError or ValueError occurs - False.
    # Otherwise - True.
    try:
        print("{:d}".format(value))
        return (True)
    except (TypeError, ValueError):
        return (False)
