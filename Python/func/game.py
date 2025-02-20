from random import seed, randint


def rock_paper_scissors() -> None:
    """Игра Камень, ножницы, бумага.

    :return: None
    """

    print('Добро пожаловать в игру: "Камень, ножницы, бумага"')

    while True:
        print('\n"1" - Камень. "2" - Ножницы. "3" - Бумага. "0" - Переход в меню.')
        text = int(input('Ваш выбор? '))
        reply: int = randint(1, 3)

        if text == 1 or text == 2 or text == 3:
            if text == reply:
                print('\nНичья! Ещё партию?')
            elif reply == 3 and text == 1:
                print('\nВы проиграли! Ещё партию?')
            elif text < reply:
                print('\nВы победили! Ещё партию?')
            elif reply == 1 and text == 3:
                print('\nВы победили! Ещё партию?')
            else:
                print('\nВы проиграли! Ещё партию?')

        elif text == 0:
            break
        else:
            print('\nОшибка ввода!')


def guess_the_number() -> None:
    """Игра "Угадай число".

    :return: None
    """

    print('Добро пожаловать в игру: "Угадай число"')
    print('Загадано целое от 0 до 1000 число, отгадайте его!')
    seed(2024)
    answer: int = randint(0, 1000)

    while True:
        num = int(input('\nВаш вариант? '))
        if 0 <= num <= 1000:

            if num == answer:
                print('\nУгадали!')
                break
            elif num > answer:
                print('\nМеньше!')
            else:
                print('\nБольше!')

        else:
            print('\nОшибка ввода!')


def main_menu() -> None:
    """Главное меню игры.

    :return: None
    """

    while True:
        print('\nДобрый день! Желаете сыграть?')
        print('"1" - «Камень, ножницы, бумага». "2" - «Угадай число». "0" - Выход из меню.')
        temp = int(input('\nВаш выбор? '))
        if temp == 1:
            rock_paper_scissors()
        elif temp == 2:
            guess_the_number()
        elif temp == 0:
            print('\nВы уверены?')

            if int(input('Повторите "0" если хотите выйти. "1" - если отмена. ')):
                pass
            else:
                break

        else:
            print('\nОшибка ввода!')


if __name__ == '__main__':
    main_menu()
