# Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
#
# *Пример:*
#
# 5
#     1 2 3 4 5
#     6
#     -> 5

len_of_list = int(input())
list_of_numbers = list()
for i in range(len_of_list):
    number = int(input())
    list_of_numbers.append(number)
n = int(input())
difference_min = abs(n - list_of_numbers[0])
nearest_element = list_of_numbers[0]
for i in list_of_numbers:
    current_difference = abs(n - i)
    if current_difference < difference_min:
        difference_min = current_difference
        nearest_element = i
print(nearest_element)
