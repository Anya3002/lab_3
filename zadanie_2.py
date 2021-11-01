#В списке, состоящем из вещественных элементов, вычислить:
#1) количество элементов списка, больших С;
#2) произведение элементов списка, расположенных после максимального по модулю элемента. Преобразовать список таким образом, чтобы сначала располагались все отрицательные элементы, а потом - все положительные (элементы, равные 0, считать положительными)
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys


if __name__ == '__main__':
    # Ввести список одной строкой.
    A = tuple(map(int, input().split()))
    C = int(input('Введите С '))

    # Проверить количество элементов кортежа.
    if len(A) != 10:
        print("Неверный размер кортежа", file=sys.stderr)
        exit(1)

    # Количество элементов больших С
    s = 0
    for item in A:
        if item > C:
            s += 1
    print(s)

    # Произведение элементов списка, расположенных после максимального по модулю элемента
    pos = 0
    mult = 1
    if abs(max(A)) > abs(min(A)): pos = A.index(max(A))
    else: pos = A.index(min(A))
    for i in range(pos + 1, len(A)):
        mult *= A[i]
    print(mult)

    # Сортированый список
    print(tuple(sorted(A)))