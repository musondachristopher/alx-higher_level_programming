# By - Musonda Christopher
# A Python function that prints x elements of a list.
def safe_print_list(my_list=[], x=0):
    # Print x elements of a list.
    # Arguments:
    # my_list (list): This is the list to print elements.
    # x(int): The number of elements of my_list to print.
    # Returns:
    # The number of elements printed.
    output_count = 0
    for i in range(x):
        try:
            print("{}".format(my_list[i]), end="")
            output_count += 1
        except IndexError:
            break
    print("")
    return output_count
