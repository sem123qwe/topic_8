data_types: list = [
    1852, 12.43, True, 4 + 3j, "Bravo!",
    (13, -5), 3.5e10, 100.95, "abcdef",
    [21, 49], {"name": 'Micky', "age": 17}
]

i = 0
while i < len(data_types):
    if not isinstance(data_types[i], (float, str)):
        print("Элемент:", data_types[i], "Тип:", type(data_types[i]))
    i += 1

# Option 2
for item in data_types:
    if not isinstance(item, (float, str)):
        print("Элемент:", item, "Тип:", type(item))

# Option 3
right = []
for item in data_types:
    if isinstance(item, (int, bool, complex, tuple, list, dict)):
        right.append(item)

# Option 4
for item in right:
    print("Элемент:", item, "Тип:", type(item))

# Option 5
for num in data_types:
    item = type(data_types[num])
    if item == float or item == str:
        continue
    print("Элемент: ", data_types[num], "Тип:", type(data_types[num]))
