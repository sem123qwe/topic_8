data_types: list = [
    1852, 12.43, True, 4 + 3j, "Bravo!",
    (13, -5), 3.5e10, 100.95, "abcdef",
    [21, 49], {"name": 'Micky', "age": 17}
]


num: int = 0
while num <= len(data_types):
    if isinstance is not (data_types[num], (float, str)):
        print("Элемент:", data_types[num], "Тип:", type(data_types[num]))
    num += 1











# if isinstance(data_types, str):
#     print(isinstance(data_types, str))
# for num in range(len(data_types)):
#     if type(data_types[num]) is float or type(data_types[num]) is str:
#         continue
#     print("Элемент:", data_types[num], "Тип:", type(data_types[num]))


# right = []
# for num in range(len(data_types)):
#     if isinstance(data_types, (int, bool, complex, tuple, list, dict)):
#         right.append(data_types)

#     print("Элемент:", right[num], "Тип:", type(right[num]))


# for num in data_types:
#     if type(data_types[num]) is float or type(data_types[num]) is str:
#         continue
#     print("Элемент: ", data_types[num], "Тип:", type(data_types[num]))
