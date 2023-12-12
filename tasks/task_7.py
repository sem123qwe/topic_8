print("Добро пожаловать в игру \"Камень-Ножницы-Бумага\"!")

stone: str = "камень"
paper: str = "бумага"
scissors: str = "ножницы"
rulse: list = [stone, paper, scissors]


user_name_1: str = input("Игрок 1, введите свое имя: ")
user_name_2: str = input("Игрок 2, введите свое имя: ")

while True:
    user_choise_1: str = input(user_name_1 + ":")
    user_choise_2: str = input(user_name_2 + ":")

    if user_choise_1 not in rulse:
        print("ПРЕДУПРЕЖДЕНИЕ:", user_name_1,
              ", соблюдайте правила игры.")
    elif user_choise_2 not in rulse:
        print("ПРЕДУПРЕЖДЕНИЕ:", user_name_2,
              ", соблюдайте правила игры.")
    elif user_choise_1 not in rulse or user_choise_2 not in rulse:
        print("ПРЕДУПРЕЖДЕНИЕ: Пожалуйста соблюдайте правила игры.")

    if user_choise_1 == user_choise_2:
        print("Ничья!")

    if user_choise_2 == stone and user_choise_1 == scissors:
        print("Поздравляем! Победитель -", user_name_2, "!")
    elif user_choise_2 == paper and user_choise_1 == stone:
        print("Поздравляем! Победитель -", user_name_2, "!")
    elif user_choise_2 == scissors and user_choise_1 == paper:
        print("Поздравляем! Победитель -", user_name_2, "!")
    elif user_choise_1 == stone and user_choise_2 == scissors:
        print("Поздравляем! Победитель -", user_name_1, "!")
    elif user_choise_1 == paper and user_choise_2 == stone:
        print("Поздравляем! Победитель -", user_name_1, "!")
    elif user_choise_1 == scissors and user_choise_2 == paper:
        print("Поздравляем! Победитель -", user_name_1, "!")

    last_question: str = input("Хотите сыграть еще раз? (да/нет): ")

    match last_question:
        case "да":
            continue
        case "нет":
            print("Досвидания!")
            break
        
