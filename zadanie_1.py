#Ввести список А из 10 элементов, найти разность положительных элементов кратных 11, их количество и вывести результаты на экран
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys


if __name__ == '__main__':
    # Ввести список одной строкой.
    A = tuple(map(int, input().split()))
    # Проверить количество элементов кортежа.
    if len(A) != 10:
        print("Неверный размер кортежа", file=sys.stderr)
        exit(1)

    k = s = 0
    for item in A:
        if item % 11 == 0 and item > 0:
              k -= item
              s += 1

    print(k, '\n', s)



