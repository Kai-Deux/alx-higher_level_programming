#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    count = len(sys.argv)
    if count == 1:
        print("{} arguments.".format(count - 1))
    elif count == 2:
        print("{} arguments:".format(count - 1))
    else:
        print("{} arguments:".format(count - 1))

    for i in range(1, count):
        print("{}: {}".format(i, sys.argv[i]))
