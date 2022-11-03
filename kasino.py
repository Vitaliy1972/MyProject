# import random
# numb = random.randint(0,10)
# col = random.randint(1,2)
# print(numb, col)
# i = 0
# while i < 5:
#     a = int(input("выберите число от 1 до 10 "))
#     b = int(input("выберите цвет, 1 красный 2 черный "))
#     if a == numb and b == col:
#         print("Бинго!, Вы выиграли!", + numb, col)
#         break
#     i += 1
#     print("Неудачно")
# print("Конец игры!")



import random
numb = random.randint(0,10)
col = random.randint(1,2)
i = 0
while i < 5:
    a = int(input("выберите число от 1 до 10 "))
    b = int(input("выберите цвет, 1 красный 2 черный "))
    if a > numb:
        print("Ваше число больше!")
        if b == col:
            print("Но Вы угадали цвет")
        else:
            print("Цвет тоже не угадали")
    elif a < numb:
        print("Ваше число меньше!")
        if b == col:
            print("Но вы угадали цвет!")
        else:
            print("Цвет тоже не угадали")
    elif a == numb and b != col:
        print("Вы не угадали цвет, но угадали число!")
    elif a == numb and b == col:
        print("Бинго!, Вы выиграли!", + numb, col)
        break
    i += 1
    print("Неудачно")
print("Конец игры!")
