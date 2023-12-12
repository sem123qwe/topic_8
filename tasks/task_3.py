num: int = int(input("Введите число: "))
for n in range(1, num):

    if num < 100:
        num += n
        print(num)
        pass
    if num > 100:
        print("Сумма всех чисел в диапазоне от 1 до ", num, "больше 100")
        break


# TODO см. теорию когда будет оаботать else у цикла
