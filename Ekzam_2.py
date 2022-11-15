# Задача 1
# 1. Добавьте на свой рабочий стол папку, в ней создайте 3 текстовых файла:
# test_1.txt, test_2.txt, test_3.txt.
# Затем переименуйте файлы на: rename_1.txt, rename_2.txt, rename_3.txt.
# После этого удалите созданную папку.
# Все операции выполнять с помощью встроенных функций библиотеки os.
# import os
# os.mkdir("C:\\Users\\Витоз\\Desktop\\Mypapka") # создание папки
# os.chdir("C:\\Users\\Витоз\\Desktop\\Mypapka") # Указываем рабочую папку
# open("test_1.txt", "w") #создание файла 1
# open("test_2.txt", "w") #создание файла 2
# open("test_3.txt", "w") #создание файла 3
# os.rename("test_1.txt","rename_1.txt") # переименование файла 1
# os.rename("test_2.txt","rename_2.txt") # переименование файла 2
# os.rename("test_3.txt","rename_3.txt") # переименование файла 3
# os.remove("rename_1.txt") # удаление файла 1
# os.remove("rename_2.txt") # удаление файла 2
# os.remove("rename_3.txt") # удаление файла 3
# os.chdir("C:\\Users\\Витоз\\Desktop")
# os.rmdir("Mypapka") # удаление папки
import random

#           Задача 2
#   Найти в списке те элементы, значение которых меньше среднего
#   арифметического, взятого от всех элементов списка.
# a = [5, 8, 6, 9, 12, 35, 7]
# b = sum(a) / len(a) # вычисляем среднее арифметическое
# print("среднее арифметическое равно ", b)
# c = []
# for i in a:
#     if i < b:
#         c.append(i)
# print("Элементы значение которых меньше ср. арифм. ", c)
#
#       Result:
#       среднее арифметическое равно  11.714285714285714
#       Элементы значение которых меньше ср. арифм.  [5, 8, 6, 9, 7]
#
# Process finished with exit code 0



#           Задача 3
# Создайте 2 множества:
# - Если они одинаковые: вывести что они равны
# - Если 1 множество полностью состоит из второго: вывести сообщение множество 1 состоит из множества2
# - Если 2 множество полностью состоит из 1: вывести сообщение множество 2 состоит из множества 1
# - Если они пересекаются: вывести элементы в которых они пересекаются
# - Если не пересекаются: вывести сообщение об этом
# a = {5, 4, 18, 6, 3}
# b = {2, 5, 4, 18, 6, 3}
# # b = {23, 5, 3, 18, 4, 8}
# if a == b:
#     print("множества равны!")
# elif a >= b:
#     print("множество 1 состоит из множества 2")
# elif b >= a:
#     print("множество 2 состоит из множества 1")
# elif a.isdisjoint(b):
#     print("нет пересечений!")
# else:
#     print("множества пересекаются!", a & b)

#           Задача 4
#       Создайте словарь из строки ' An apple a day keeps the doctor away'
# следующим образом: в качестве ключей возьмите символы строки, а
# значениями пусть будут числа, соответствующие количеству вхождений
# данной буквы в строку.
# a = ' An apple a day keeps the doctor away'
# b = a.split(" ")
# print(b)
# c = "".join(b)
# print(c)
# for i in c:             # вариант 1
#     d = {i: c.count(i)} # вариант 1
#     print(d)            # вариант 1

## d = {i: c.count(i) for i in c}  # вариант 2
## print(d)                        # вариант 2

### from collections import Counter  ## вариант 3
### print(dict(Counter(c)))          ## вариант 3



           ## Задача 5
#  Ввести 10 чисел, данные числа добавить их во множество.
# c = 0
# b=set([])
# while c < 10:
#     a = int(input("Введите число "))
#     b.add(a)
#     c = c + 1
# print(b)
# print(type(b))


            ### Задача 6
# Есть словарь песен группы Depeche Mode violator songsdict = { 'World in
# My Eyes': 4.76, 'Sweetest Perfection': 5.43, 'Personal Jesus': 4.56, 'Halo': 4.30,
# 'Waiting for the Night': 6.07, 'Enjoy the Silence': 4.6, 'Policy of Truth': 4.88,
# 'Blue Dress': 4.18, 'Clean': 5.68, }
# Выведите общее время звучания всех песен.
# Создайте список песен, время звучаниях которых больше 5 минут
# Создайте новый словарь тех песен, название которых состоит из одного слова

# songsdict = { 'World in My Eyes': 4.76, 'Sweetest Perfection': 5.43, 'Personal Jesus': 4.56, 'Halo': 4.30,
#               'Waiting for the Night': 6.07, 'Enjoy the Silence': 4.6, 'Policy of Truth': 4.88,
#               'Blue Dress': 4.18, 'Clean': 5.68,
#               }
# a = songsdict.values() # выводим значения словаря
# print("общее время песен равно ", sum(a))
# longsongs = [] # создаем пустой список для длинных песен
# for mn in songsdict: # проходимся по словарю
#     if songsdict[mn] >= 5.00: # находим длинные песни
#         longsongs.append(mn)  # добавляем длинные песни в список
# print("Песни которые длятся более пяти минут:", longsongs)
# for mn in songsdict:
#     if mn != " ":
#         one = {mn: songsdict[mn]}
# print("песни, название которых состоит из одного слова", one)


            # Задача 7
# 7. Дана строка. Сохранить в ней только первые вхождения символов,
# удалив все остальные. Результат вывести в виде кортежа.

# stroka = "Strings in python are surrounded by either single quotation marks, or double quotation marks."
# a=[]
# for i in stroka:
#     if stroka.count(i) > 1:
#         continue
#     else:
#         a.append(i)
# print(tuple(a))


            # Задача 8
# Сжать массив, удалив из него все элементы, величина которых находится в интервале [а, b].
# Освободившиеся в конце массива элементы заполнить нулями.

# mas = [12, 14, 54, 34, 27, 83, 45, 15]
# a = int(input("Введите начальное значение интервала "))
# b = int(input("Введите конечное значение интервала "))
# for i in range(a, b+1):
#     if i in mas:
#         mas.remove(i)
#         mas.append(0)
# print("сжатый массив", mas)


            # Задача 9
# Вычислить количество отрицательных элементов под главной диагональю матрицы.
# import random
# n = int(input("Введите кол-во строк матрицы: "))
# m = int(input("Введите кол-во столбцов матрицы: "))
# Matrix = [[random.randint(-20, 20) for j in range(n)] for i in range(m)]
# h = 0
# print("Matrix: ")
# for i in range (m):
#     print(Matrix[i])
#     for j in range(i+1, n):
#         if Matrix[i][j]<0:
#             h += 1
# print("Количество отрицательных элементов под главной диагональю", h)


#           2 вариант
# listA = []
# for i in range(n):
#     listB = []
#     [listB.append(random.randint(-100, 100)) for x in range(m)]
#     listA.append(listB)
# for i in listA:
#     print(i)
# A = 0
# for i in range(n):
#     for j in range(m):
#         if j < i and listA[i][j] < 0:
#             A += 1
# print("Число отрицательных элементов: ",A)



                # Задача 10
# Найти сумму элементов, находящихся между минимальным и максимальным элементами.
# Сами минимальный и максимальный элементы в сумму не включать.
# import random
# a = [random.randint(0, 100) for x in range(16)] # список элементов
# a.sort() # сортируем
# print(a)
# b = []
# b.append(a[1:-1]) # отсеиваем наименьшее и наибольшее числа
# print(b)
# for i in b: # проходимся по новому списку
#     print(sum(i))  # суммируем


