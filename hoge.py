#! /usr/bin/env python3


def hogehoge(a, b):
    if a < b:
        return a + b
    else:
        return a - b


def pogepoge(a):
    return 2 * a


if __name__ == "__main__":
    print(hogehoge(5, 2))
    print(pogepoge(3))
