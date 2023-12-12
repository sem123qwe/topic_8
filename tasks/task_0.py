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
