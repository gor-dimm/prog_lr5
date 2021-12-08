#Среднее гармоническое
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def harmid(*args):
   if args and 0 not in args:
       a = 0
       for item in args:
           a += 1 / item
       return len(args) / a
   else:
        return None


if __name__ == "__main__":
    print(harmid())
    print(harmid(1, 3, 5, 7, 9))
    print(harmid(2, 4, 6, 8, 10, 12))