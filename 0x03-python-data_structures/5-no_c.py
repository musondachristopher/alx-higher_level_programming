#!/usr/bin/python3
# by - Muzzo
# A Python function that removes all characters c and C from a string.
def no_c(my_string):
    new_string = my_string.translate({ord(i): None for i in 'cC'})
    return new_string
