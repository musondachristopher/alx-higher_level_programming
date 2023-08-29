#!/usr/bin/python3
# By - Musonda Christopher
# A Python function that divides 2 integers and prints the result.
# Arguments: a (int): The numerator and b (int): The denominator.
def safe_print_division(a, b):
    # Returns the division of a by b.
    try:
        divide = a / b
    except (TypeError, ZeroDivisionError):
        divide = None
    finally:
        print("Inside result: {}".format(divide))
    # float or None: The result of the division or None if an exception occurs.
    return (divide)
