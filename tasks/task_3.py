num: int = int(input("Введите число: "))

total: int = 0
for n in range(1, num + 1):
    total += n

    if total > 100:
        print("Сумма всех чисел в диапазоне от 1 до", num, "больше 100")
        break
else:
    print(total)
