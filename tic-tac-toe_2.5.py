import os
import msvcrt

field = {a: " " for a in range(1, 10, 1)}   # Генератор словаря


def yes_x():                    # Финальное украшательство
    print("X)"*10, "\n"+"X)"*10, "\nX)X)"*2+"\n"+"X)"*10 +
          "\n"+"X)"*10+"\nX)X)"*2+"\n"+"X)"*10+"\n"+"X)"*10)
    print("\n"*1)
    print("X)"*10, "\n"+"X)"*10, "\nX)X)"*3+"\n"+"X)X)" +
          "\nX)X)"*2+"\n"+"X)"*10+"\n"+"X)"*10)


def yes_o():                    # Финальное украшательство
    print("O)"*10, "\n"+"O)"*10, "\nO)O)"*2+"\n"+"O)"*10 +
          "\n"+"O)"*10+"\nO)O)"*2+"\n"+"O)"*10+"\n"+"O)"*10)
    print("\n"*1)
    print("O)"*10, "\n"+"O)"*10, "\nO)O)"*3+"\n"+"O)O)" +
          "\nO)O)"*2+"\n"+"O)"*10+"\n"+"O)"*10)

# _________Объявление переменных_________
listS = ["", "", "", "", "", "", "", "", ""]
cursor = "\b█"
turn = 5
on = 1
off = 0
nothing = ""
n = nothing
s1, s2, s3, s4, s5, s6, s7, s8, s9, s35 = \
    n, n, n, n, n, n, n, n, n, n
up, down, left, right = "up", "down", "left", "right"
f = field
draw = 0
win = 0
s5 = cursor
# _______


def func_win_check(symbl):               # Проверка на победу или ничью
    global win, draw

    if f[1] == symbl and f[4] == symbl and f[7] == symbl:
        win = symbl
    elif f[2] == symbl and f[5] == symbl and f[8] == symbl:
        win = symbl
    elif f[3] == symbl and f[6] == symbl and f[9] == symbl:
        win = symbl
    elif f[1] == symbl and f[2] == symbl and f[3] == symbl:
        win = symbl
    elif f[4] == symbl and f[5] == symbl and f[6] == symbl:
        win = symbl
    elif f[7] == symbl and f[8] == symbl and f[9] == symbl:
        win = symbl
    elif f[1] == symbl and f[5] == symbl and f[9] == symbl:
        win = symbl
    elif f[3] == symbl and f[5] == symbl and f[7] == symbl:
        win = symbl
    elif f[1] != " " and f[2] != " " and f[3] != " " and f[4] != " " \
            and f[5] != " " and f[6] != " " and f[7] != " " \
            and f[8] != " " and f[9] != " ":
        draw = 1


def func_screen(x, o, status):
    global s1, s2, s3, s4, s5, s6, s7, s8, s9, s35, cursor, player
    field[o] = "O"
    field[x] = "X"
    cursor = "\b█"

    screen = "-------------\n"\
      + "| {0} | {1} | {2} |\n".format(s1+field[1], s2+field[2], s3+field[3])\
      + "-------------\n"\
      + "| {0} | {1} | {2} |\n".format(s4+field[4], s5+field[5], s6+field[6])\
      + "-------------\n"\
      + "| {0} | {1} | {2} |\n".format(s7+field[7], s8+field[8], s9+field[9])\
      + "-------------\n"

    if status == on:
        os.system("cls")
        print(screen)
    elif status == "X":
        os.system("cls")
        print(' Ставьте "X"')
        print(screen)
    elif status == "O":
        os.system("cls")
        print(' Ставьте "O"')
        print(screen)
    elif status == off:
        pass


def func_cursor(sign):    # |____Внедрение в игру курсора____________________|

    def move(coordinates, direction):    # ____Движения курсора____
        #                                Это второстепенная функция,
        #                                смотри func_keyboard_listening() ниже
        global s1, s2, s3, s4, s5, s6, s7, s8, s9, s35, \
            up, down, left, right, cursor, turn, listS
        p = coordinates
        d = direction
        c = cursor
        nothing = ""
        n = nothing
        s1, s2, s3, s4, s5, s6, s7, s8, s9, s35 = \
            n, n, n, n, n, n, n, n, n, n

        # По умолчанию: s1 = "".
        # В func_screen() указано, что cursor = "\b█"
        # Если мы попадаем на s1,
        # то происходит неочевидное присвоение: s1 = "\b█"

        """ Снизу много быдлокода. Проектик был написан очень давно.
        Я знаю, что так нельзя. Сейчас не позволил бы себе такое..."""

        if p == 1 and d == up:
            s1 = c; p = 1
        elif p == 1 and d == down:
            s4 = c; p = 4
        elif p == 1 and d == left:
            s1 = c; p = 1
        elif p == 1 and d == right:
            s2 = c; p = 2

        elif p == 2 and d == up:
            s2 = c; p = 2
        elif p == 2 and d == down:
            s5 = c; p = 5
        elif p == 2 and d == left:
            s1 = c; p = 1
        elif p == 2 and d == right:
            s3 = c; p = 3

        elif p == 3 and d == up:
            s3 = c; p = 3
        elif p == 3 and d == down:
            s6 = c; p = 6
        elif p == 3 and d == left:
            s2 = c; p = 2
        elif p == 3 and d == right:
            s3 = c; p = 3

        elif p == 4 and d == up:
            s1 = c; p = 1
        elif p == 4 and d == down:
            s7 = c; p = 7
        elif p == 4 and d == left:
            s4 = c; p = 4
        elif p == 4 and d == right:
            s5 = c; p = 5

        elif p == 5 and d == up:
            s2 = c; p = 2
        elif p == 5 and d == down:
            s8 = c; p = 8
        elif p == 5 and d == left:
            s4 = c; p = 4
        elif p == 5 and d == right:
            s6 = c; p = 6

        elif p == 6 and d == up:
            s3 = c; p = 3
        elif p == 6 and d == down:
            s9 = c; p = 9
        elif p == 6 and d == left:
            s5 = c; p = 5
        elif p == 6 and d == right:
            s6 = c; p = 6

        elif p == 7 and d == up:
            s4 = c; p = 4
        elif p == 7 and d == down:
            s7 = c; p = 7
        elif p == 7 and d == left:
            s7 = c; p = 7
        elif p == 7 and d == right:
            s8 = c; p = 8

        elif p == 8 and d == up:
            s5 = c; p = 5
        elif p == 8 and d == down:
            s8 = c; p = 8
        elif p == 8 and d == left:
            s7 = c; p = 7
        elif p == 8 and d == right:
            s9 = c; p = 9

        elif p == 9 and d == up:
            s6 = c; p = 6
        elif p == 9 and d == down:
            s9 = c; p = 9
        elif p == 9 and d == left:
            s8 = c; p = 8
        elif p == 9 and d == right:
            s9 = c; p = 9

        coordinates, turn = p, p
        return coordinates
    # ______________________________________

    def func_keyboard_listening():    # ____Обработка нажатий____
        global player, turn, s5, cursor
        coordinates = 5

        func_screen(None, None, sign)
        while 1:  # проверка на свободную клетку

            while 1:    # перемещение курсора и Enter

                key = msvcrt.getch()
                if key == b'\x00':
                    continue
                    # pass


                elif key == b'\r' or key == b' ':      # Enter
                    # print("Нажат ENTER")
                    player = coordinates  # передача координат курсора
                    break
                elif key == b'\x1b':    # Escape (отладка)
                    exit()

                elif key == b'H' or key == b'w':
                    # print("Нажата кнопочка ВВЕРХ))\n")
                    coordinates = move(turn, up)


                elif key == b'P' or key == b's':
                    # print("Нажата кнопочка ВНИЗ))\n")
                    coordinates = move(turn, down)

                elif key == b'K' or key == b'a':
                    # print("Нажата кнопочка ВЛЕВО))\n")
                    coordinates = move(turn, left)

                elif key == b'M' or key == b'd':
                    # print("Нажата кнопочка ВПРАВО))\n")
                    coordinates = move(turn, right)

                func_screen(None, None, sign)

            # _________________________граница между циклами_______
            if field[player] == " ":
                break
            else:
                print("Эта клетка уже занята. Выберите другую")
                key = msvcrt.getch()

    func_keyboard_listening()   # _______Важный_Вызов_______


# ____________________Заголовок_________________________________________________
os.system("cls")
# print("_*X*_*O*"*7+"\n")
print("Игра Крестики-Нолики\n")
print(" Управление курсором - стрелочками на клаве.")
print(" Поставить крестик или нолик - Enter")
print('Нажмите anykey для начала игры...')
key = msvcrt.getch()


def final():
    global field, win, draw, f, turn, player, s5, cursor, \
        s1, s2, s3, s4, s5, s6, s7, s8, s9, s35

    while 1:
        print("  Играть снова - Enter")
        print("        Выйти  - Escape")
        key = msvcrt.getch()
        if key == b'\r' or key == b' ':      # Enter
            field = {a: " " for a in range(1, 10, 1)}
            f = field
            s1, s2, s3, s4, s5, s6, s7, s8, s9, s35 = \
                n, n, n, n, n, n, n, n, n, n
            s5 = cursor
            # turn = player
            # player = 5
            # turn = 5
            win = 0
            draw = 0
            game()  # Enter / Играть снова
        elif key == b'\x1b':    # Escape / Выход
            exit()


def congratulations():
    global win, draw, f
    if win == "X":
        print("   Поздравляем крестики с победой =)")
        yes_x()
    elif win == "O":
        print("   Поздравляем нолики с победой =)")
        yes_o()
    elif draw == 1:
        print("  __Ничья__  =)")
    else:
        print(" ERROR! "*5)
        print(" win = ", win)
        print(" draw = ", draw)
        print(" f = ", f)
    final()


# ________________________________________________Главная функция___________________


def game():
    global win, draw, player
    while 1:
        player = 5
        func_cursor("X")
        func_screen(player, None, off)
        func_win_check("X")

        if win != 0 or draw != 0:
            func_screen(None, None, on)
            break
        # ________________________
        player = 5
        func_cursor("O")
        func_screen(None, player, off)
        func_win_check("O")

        if win != 0 or draw != 0:
            func_screen(None, None, on)
            break

    congratulations()
# _____________________________________
game()
