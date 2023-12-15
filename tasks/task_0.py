mainas: list = []
plis: list = []
count: int = 0
while True:
    if count < 3:
        num = int(input())
    else:
        break

    if num > 0:
        plis.append(num)
    elif num < 0:
        mainas.append(num)
        count += 1

print("Сумма положительных чисел:", sum(plis))
print("Сумма отрицательных чисел:", sum(mainas))

# -------------------------------------------

# Option 2
positive_sum = negative_sum = negative_count = 0
while True:
    num = int(input())

    if num < 0:
        negative_count += 1
        negative_sum += num
    else:
        positive_sum += num

    if negative_count > 2:
        break

print("Сумма положительных чисел:", positive_sum)
print("Сумма отрицательных чисел:", negative_sum)
