#Среднее геометрическое
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def geomid(*args):
    if args:
        a = 1
        for item in args:
            a *= item
        return pow(a, 1/len(args))
    else:
        return None

if __name__ == "__main__":
    print(geomid())
    print(geomid(2, 4, 6, 8,))
    print(geomid(1, 3, 5, 7, 9, 11))