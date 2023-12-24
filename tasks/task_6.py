start: int = int(input())
finish: int = int(input())

if start == finish or start < 0 or finish < 0:  # Добавлена проверка finish
    print("Некорректный диапазон")
else:
    if start > finish:
        start, finish = finish, start  # Исправлена опечатка

    simple_num: list = []
    # TODO: Тут ошибка, этот код не определяет простых чисел.
    #  Переделайте код, в задании №4 мы разбирали пример.
    for num in range(start, finish):
        if num % 2 != 0 and num % 3 != 0:
            simple_num.append(num)
        else:
            num += 1

    print("Простые числа в заданном диапазоне:", *simple_num)
