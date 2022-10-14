# 4. ** Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять
# первому игроку, чтобы забрать все конфеты у своего конкурента?
# 1. Добавьте игру против бота
# 2. Подумайте как наделить бота "интеллектом"

from random import shuffle, randint


def bot_run(count):# Игрок бот
    result = count % 29
    if not result:
        result = randint(1, 28)
    return result


def players_run(play):# Игрок человек
    while play:
        result = input(f"{play}, возьмете конфеты [1 .. 28]: ")
        if not result.isnumeric():
            print("Так нельзя!!!")
            continue
        elif int(result) > 28 or int(result) < 1:
            print("Так не пойдет!!!")
            continue
        return int(result)


def out_message(play, count, value): # блок вывода сообщений
    print(
        f"\n{play} взял {count} шт.; всего конфет осталось {value} шт.")


def game_mode(msg):# Выбор игроков
    players = ['Игрок_1', 'bot' if (input(msg)) else 'Игрок_2']
    print(
        f'\nУчастники: {players[0]} и {players[1]}\nПереходим к жеребьевке:\n')
    shuffle(players)
    print(f'Первым ходит {players[0]}, вторым ходит {players[1]}')
    return players


def game_candies(mode):

    players = game_mode(mode) # Выбор с кем играем
    candies = 2021 # Количество конфет изначально!!!
    #candies = 141
    count_max = 28
    index = 0

    while candies > count_max:

        if players[index] == "bot":
            number_of_candies = bot_run(candies)
        else:
            number_of_candies = players_run(players[index])

        candies -= number_of_candies
        out_message(players[index], number_of_candies, candies)
        index = abs(index - 1) # id игрока

    print(
        f"\nOставшиеся конфеты:{candies} шт. забирает {players[index]} и выигрывает!!!\n")


message = "Начало игры:\nИгрок_1 против Игрока_2 (нажмите Enter)\n\
Если хотите играть против бота введите любой символ => "

game_candies(message)
