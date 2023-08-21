#!/usr/bin/python3
# this program prints the alphabet except 'q' and 'e'.
for print_alphabt in range(97, 123):
    if (print_alphabt != 101 and print_alphabt != 113):
        print("{:c}".format(print_alphabt), end='')
