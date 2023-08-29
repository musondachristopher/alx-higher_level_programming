#!/usr/bin/python3
# By - Musonda Christopher
# A Python function that prints the first x elements of a list and only integers
def safe_print_list_integers(my_list=[], x=0):
    # Print the first n elements of a list that are integers.
    # Arguments: my_list (list): The list to print elements from n (int): The number of elements of my_list to print.
    # Returns: The number of elements printed.
    ret = 0
    for i in range(0, x):
        try:
            print("{:d}".format(my_list[i]), end="")
            ret += 1
        except (ValueError, TypeError):
            continue
    print("")
    return (ret)
