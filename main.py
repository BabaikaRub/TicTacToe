
field = [['-'] * 3 for _ in range(3)]  # Создаем игровое поле


def show_field(fld):
    """Функция отображает состояние текущего игрового поля"""
    print('  0 1 2')
    for i in range(len(fld)):
        print(i, *fld[i])


def go_player(fld):
    """Ход игрока: вводятся координаты для закрашивания клетки"""
    x = 0
    y = 0
    while True:
        turn = input('Введите координаты клетки: ').split()

        if len(turn) != 2:
            print('Введите две координаты!')
            continue

        if not(turn[0].isdigit() and turn[1].isdigit()):
            print('Введите числа!')
            continue

        x, y = map(int, turn)

        if not (0 <= x < 3 and 0 <= y < 3):
            print('Вы вышли за границы диапазона!')
            continue

        if fld[x][y] != '-':
            print('Клетка уже занята!')
            continue

        break
    return x, y


def is_finish(fld, turn):
    """Определяем текущее состояние игры:
    выиграли, проиграли или игра продолжается"""
    wins_coord = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]

    fld_list = []
    for i in fld:
        fld_list += i

    indexes = set([i for i, x in enumerate(fld_list) if x == turn])

    for j in wins_coord:
        if len(indexes.intersection(set(j))) == 3:
            return True

    return False


def start_game(fld):
    """Функция запуска игры: отображается игровое поле, игрок ставит крестик, а так же нолик
    в пустую ячейку. Проверяется наличие свободных полей или выигрышной комбинации"""
    count = 0
    while True:
        if count == 9:
            print('Ничья!')
            break

        if count % 2 == 0:
            user_turn = 'x'
        else:
            user_turn = 'o'

        show_field(fld)
        x, y = go_player(fld)
        field[x][y] = user_turn

        if is_finish(fld, user_turn):
            print(f'Выиграл {user_turn}!')
            show_field(fld)
            break
        count += 1


start_game(field)
