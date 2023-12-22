user_input = int(input())
# number = user_input
# while True:
#     for i in range(1, user_input + 1):
#         if number % i != 0:
#             print(number)
#             break

#     number += user_input

num_copy = user_input
while True:
    for i in range(1, user_input):
        if num_copy % i != 0:
            break
        else:
            print(num_copy)
            break

    num_copy += user_input
