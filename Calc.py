a = float(input("введите первое число "))
c = input("Выберите операцию: +, -, *, / ")
b = float(input("введите второе число "))
if b == 0:
    print("Ошибка, делить на 0 нельзя!")

if c == ("+"):
    print(a + b)
elif c == ("-"):
    print(a - b)
elif c == ("*"):
    print(a * b)
elif c == ("/"):
    print(a / b)
else:
    print("Ошибка, введена неверная операция!")





