start: int = int(input())
finish: int = int(input())

if start > finish:
    start, finish == finish, start
elif start == finish or start < 0:
    print("Некорректный диапазон")

simple_num: list = []
for num in range(start, finish):

    if num % 2 != 0 and num % 3 != 0:
        simple_num.append(num)
    else:
        num += 1

print("Простые числа в заданном диапазоне:", str(simple_num))
