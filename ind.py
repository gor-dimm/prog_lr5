# 6. Произведение аргументов, расположенных между первым и вторым нулевыми аргументами.
# !/usr/bin/env python3
# -*- coding: utf-8 -*-

def between_zeros(*args):
    for item in args:
        # итерируем все аргументы
        it = iter(args)
        # ищем первый нулевой аргумент
        while True:
            i = next(it)
            if i == 0:
                break

        m = 1
        # ищем второй нулевой аргумент
        while True:
            i = next(it)
            if i == 0:
                break
            # умножаем аргументы между нулевыми аргументами
            m *= i

    print(f"Ответ: {m}")


if __name__ == '__main__':
    between_zeros(2, 0, -12, -3, 4, 5, 6, 3, 7.5, 0, 10.9, 10.8)
    between_zeros(1, 2, 3, 0, 4, 5, 6, 0, 7, 8, 9, 0)
