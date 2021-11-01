# Проверка вхождения элемента в кортеж
# Оператор in
# Заданный кортеж, который содержит строки
A = ("abc", "abcd", "bcd", "cde")

# Ввести элемент
item = str(input("s = "))

if (item in A):
    print(item, " in ", A, " = True")
else:
    print(item, " in ", A, " = False")
