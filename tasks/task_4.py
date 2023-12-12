user_input: int= int(input("Введите число: "))
if user_input < 0:
    print("Число должно быть положительным")
elif user_input % 2 == 0 or user_input % 3 == 0:
    print("Число", user_input, "не является простым")
else:
    print("Число", user_input, "является простым")
# TODO если число делится хотябы на одно число от 2 до n, то оно не простое.
#  Пропуск
