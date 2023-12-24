user_input: int = int(input())

num_copy: int = user_input
while True:
    for i in range(1, user_input):
        if num_copy % i != 0:
            break
    else:  # Блок должен быть у цикла
        print(num_copy)
        break

    num_copy += user_input
