#!/usr/bin/python3
# By - Musonda Christopher
"""Print the numbers(numb) from 1 to 100 separated by a space.
  For multiples of three, print Fizz instead of the number
  For multiples of five, print Buzz instead of the number.
  For multiples of three and five, print FizzBuzz instead of the number.
  """
def fizzbuzz():
    for numb in range(1, 101):
        if numb % 3 == 0 and numb % 5 == 0:
            print("FizzBuzz ", end="")
        elif numb % 3 == 0:
            print("Fizz ", end="")
        elif numb % 5 == 0:
            print("Buzz ", end="")
        else:
            print("{} ".format(numb), end="")
