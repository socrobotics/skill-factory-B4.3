dashboard = list(range(1, 10))


def draw_board(dashboard):
    print("-" * 13)
    for i in range(3):
        print("|", dashboard[0 + i * 3], "|", dashboard[1 + i * 3], "|", dashboard[2 + i * 3], "|")
        print("-" * 13)


def take_input(player):
    valid = False
    while not valid:
        player_answer = input("Куда поставим " + player + "? ")
        try:
            player_answer = int(player_answer)
        except:
            print("Некорректный ввод. Вы уверены, что ввели число?")
            continue
        if player_answer >= 1 and player_answer <= 9:
            if (str(dashboard[player_answer - 1]) not in "XO"):
                dashboard[player_answer - 1] = player
                valid = True
            else:
                print(f"В данной клетке уже стоит {str(dashboard[player_answer - 1])}")
        else:
            print("Некорректный ввод. Введите число от 1 до 9 чтобы продолжить.")


def check_win(dashboard):
    win_coord = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
    for item in win_coord:
        if dashboard[item[0]] == dashboard[item[1]] == dashboard[item[2]]:
            return dashboard[item[0]]
    return False


def main(dashboard):
    counter = 0
    win = False
    while not win:
        draw_board(dashboard)
        if counter % 2 == 0:
            take_input("X")
        else:
            take_input("O")
        counter += 1
        if counter > 4:
            tmp = check_win(dashboard)
            if tmp:
                print(tmp, "выиграл!")
                win = True
                break
        if counter == 9:
            print("Ничья!")
            break
    draw_board(dashboard)


main(dashboard)
