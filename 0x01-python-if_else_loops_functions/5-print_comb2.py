#!/usr/bin/python3
# print numbers from 0 to 99 only.
for print_nums in range(00, 100):
    print("{:02d}".format(print_nums), end='\n' if print_nums == 99 else ", ")
