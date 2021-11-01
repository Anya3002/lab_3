# Метод count - подсчет количества вхождений элемента в кортеж
# Заданный кортеж
A = ("ab", "ac", "ab", "ab", "ca", "ad", "jklmn")

d1 = A.count("ab") # d1 = 3
d2 = A.count("jprst") # d2 = 0
d3 = A.count("ca") # d3 = 1

print("d1 = ", d1)
print("d2 = ", d2)
print("d3 = ", d3)