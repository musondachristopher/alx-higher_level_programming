#!/usr/bin/python3
# By - Musonda Christopher
# Function checks for lowercase characters.
def islower(c):
    if ord(c) >= 97 and ord(c) <= 122:
        return True
    else:
        return False
islower('w')
