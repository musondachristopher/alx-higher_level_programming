#!/usr/bin/python3
# By - Musonda Christopher
# A function that retrieves an element from a list like in C
def element_at(my_list, idx):
    if idx < 0:
        return (None)
    lenth = len(my_list)
    if idx > lenth - 1:
        return (None)
    return(my_list[idx])
