# Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N]. Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
#
# *Пример:*
#
# 5
#     1 2 3 4 5
#     3
#     -> 1


len_of_list = int(input())
list_of_numbers = list()
for i in range(len_of_list):
    number = int(input())
    list_of_numbers.append(number)
count_of_numbers = int(input())
print(list_of_numbers.count(count_of_numbers))
    