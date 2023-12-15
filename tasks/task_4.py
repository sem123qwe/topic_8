user_input: int = int(input("Введите число: "))

if user_input < 2:
    print("Число должно быть больше 1")
else:
    for i in range(2, int(user_input ** 0.5) + 1):
        if user_input % i == 0:
            print("Число", user_input, "не является простым")
            break
    else:
        print("Число", user_input, "является простым")
