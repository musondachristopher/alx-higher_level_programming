#!/usr/bin/python3
# By - Musonda Christopher
# A Python function that divides element by element 2 lists.
# Arguments: my_list_1 (list): The first lis, my_list_2 (list): The second list and list_length (int): The number of elements to divide.
def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    for i in range(0, list_length):
        try:
            divide = my_list_1[i] / my_list_2[i]
        except TypeError:
            print("wrong type")
            divide = 0
        except ZeroDivisionError:
            print("division by 0")
            divide = 0
        except IndexError:
            print("out of range")
            divide = 0
        finally:
            new_list.append(divide)
    # Returns: A new list of length list_length containing all the divisions.
    return (new_list)
