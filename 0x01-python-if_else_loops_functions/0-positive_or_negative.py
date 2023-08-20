#!/usr/bin/python3
import random
num = random.randint(-20,10)
if num > 0:
    print("{} is positive".format(num))
elif num == 0:
    print("{} is zero".format(num))
else:
    print("{} is negative".format(num))
