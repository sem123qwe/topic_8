numbers: list = ["21", "85", "150", "190", "135", "515", "80"]


num: int = 0
check = int(numbers[num])
for num in range(len(numbers)):
    if check >= 500:
        break
    if check > 150:
        continue
    elif check % 5 == 0:
        print(check)

# TODO реализовать через перебор и убрать дубликаты
