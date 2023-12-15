numbers: list = ["21", "85", "150", "190", "135", "515", "80"]

for num in numbers:
    num: int = int(num)

    if num >= 500:
        break
    if num > 150:
        continue
    elif num % 5 == 0:
        print(num)
