print("Добро пожаловать в игру \"Камень-Ножницы-Бумага\"!")

STONE: str = "камень"
PAPER: str = "бумага"
SCISSORS: str = "ножницы"

rulse: list = [STONE, PAPER, SCISSORS]

user_name_1: str = input("Игрок 1, введите свое имя: ")
user_name_2: str = input("Игрок 2, введите свое имя: ")

while True:
    user_choise_1: str = input(user_name_1 + ": ")
    user_choise_2: str = input(user_name_2 + ": ")

    # TODO: Код правильный, проверьте выводы, чтобы совпали с примерами.
    if user_choise_1 not in rulse and user_choise_2 not in rulse:
        print("ПРЕДУПРЕЖДЕНИЕ: Пожалуйста соблюдайте правила игры.")
    elif user_choise_1 not in rulse:
        print("ПРЕДУПРЕЖДЕНИЕ:", user_name_1,
              ", соблюдайте правила игры.")
    elif user_choise_2 not in rulse:
        print("ПРЕДУПРЕЖДЕНИЕ:", user_name_2,
              ", соблюдайте правила игры.")

    if user_choise_1 == user_choise_2:
        print("Ничья!")

    congretulations = "Поздравляем! Победитель -"
    if user_choise_2 == STONE and user_choise_1 == SCISSORS:
        print(congretulations, user_name_2, "!")
    elif user_choise_2 == PAPER and user_choise_1 == STONE:
        print(congretulations, user_name_2, "!")
    elif user_choise_2 == SCISSORS and user_choise_1 == PAPER:
        print(congretulations, user_name_2, "!")
    elif user_choise_1 == STONE and user_choise_2 == SCISSORS:
        print(congretulations, user_name_1, "!")
    elif user_choise_1 == PAPER and user_choise_2 == STONE:
        print(congretulations, user_name_1, "!")
    elif user_choise_1 == SCISSORS and user_choise_2 == PAPER:
        print(congretulations, user_name_1, "!")

    last_question: str = input("Хотите сыграть еще раз? (да/нет): ")

    # TODO: Эту проверку можно улучшить, первый кейс работает некорректно.
    #  Нужно проверить, если пользователь ввел "нет",
    #  то нужно break, иначе продолжим работать.
    #  Также здесь принт можно вывести за цикл.
    match last_question:
        case "да":
            continue
        case "нет":
            print("До встречи!")
            break
