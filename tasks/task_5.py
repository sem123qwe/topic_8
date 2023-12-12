user_input = int(input(""))
number = 1

while True:
    for num in range(1, user_input):
        if (num % 2 != 0 and num % 3 != 0) % number == 0: 
            print(num)
        else:
            num += 1


'''
20 внешний цикл 
проверка в внутренем цикле 
'''
