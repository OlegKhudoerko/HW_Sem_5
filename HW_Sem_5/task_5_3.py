# 3. * Создайте программу для игры в "Крестики-нолики".
# Поле 3x3. Игрок - игрок, без бота.

def game_playing_field(array):
    for i in range(3):
        print(
            f"\n\t{array[0 + i * 3]:1}\t|\t{array[1 + i * 3]}\t|\t{array[2 + i * 3]}\n", '-' * 22)


def players(number, name, char_name, playing_field):
    while name:
        index = input(
            f'{number} игрок введите число, куда поставим {name}?  [1 .. 9]: ')
        if not index.isnumeric():
            print("Так нельзя!!!")
            continue
        index = int(index)
        if index > 9 or index < 1:
            print("Так не пойдет!!!")
            continue
        elif str(playing_field[index-1]) == chr(10060) or str(playing_field[index-1]) == chr(11093):
            print("Эта клетка уже занята!!!'")
            continue
        else:
            playing_field[index - 1] = char_name
            return


def win_check(cell):
    coordinates = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6),
                   (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
    for j in coordinates:
        if cell[j[0]] == cell[j[1]] == cell[j[2]]:
            return cell[j[0]]
    return False


def main(playing_field):
    counter = 0
    win = False
    while not win:
        game_playing_field(playing_field)
        if counter % 2 == 0:
            players("Первый", "крестик", chr(10060), playing_field)
        else:
            players("Второй", "нолик", chr(11093), playing_field)
        counter += 1
        if counter > 4:
            tmp = win_check(playing_field)
            if tmp:
                win = True
                if tmp == chr(10060):
                    print("Первый", end=' ')
                else:
                    print("Второй", end='')
                print(" игрок выиграл!!!")
                break
        if counter == 9:
            print('Ничья!')
            break
    game_playing_field(playing_field)


def game_tic_tac_toe():
    print(f"\nИгра в крестики-нолики для двух игроков\n \
           \rПервый игрок ставит крестики: {chr(10060)}, второй нолики:  {chr(11093)}\n")
    playing_field = list(range(1, 10))
    main(playing_field)


game_tic_tac_toe()
