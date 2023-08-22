#!/usr/bin/python3
# by Musonda Christopher
# A Python program that prints all the names defined by the compiled module hidden_4.pyc (please download it locally).
if __name__ == "__main__":
    """Print all names defined by hidden_4 module """
    import hidden_4
    import sys
    names = dir(hidden_4)
    for nme in names:
        if nme[:2] != "__":
            print(nme)
