print("\nКрестики нолики.\nЧто бы играть введите кординаты через пробел кординаты места где вы хотите поставить 'x' или 'O', например (a 3). \nКресткики ходят первые.\n")

first_string = [' ', 'a', 'b', 'c']
second_string = ['1', '-', '-', '-']
third_string = ['2', '-', '-', '-']
forth_string = ['3', '-', '-', '-']




def board():
    print(*first_string)
    print(*second_string)
    print(*third_string)
    print(*forth_string)

def ttt_x(m,n):
    global second_string
    global third_string
    global forth_string

    if n == 1:
        second_string.pop(m)
        second_string.insert(m, 'x')
    elif n == 2:
        third_string.pop(m)
        third_string.insert(m, 'x')
    elif n == 3:
        forth_string.pop(m)
        forth_string.insert(m, 'x')

def ttt_O(m,n):
    global second_string
    global third_string
    global forth_string

    if n == 1:
        second_string.pop(m)
        second_string.insert(m, 'O')
    elif n == 2:
        third_string.pop(m)
        third_string.insert(m, 'O')
    elif n == 3:
        forth_string.pop(m)
        forth_string.insert(m, 'O')

user_input_m = None
user_input_n = None

def inputs():
    while True:
        global user_input_n
        global user_input_m

        a = input()
        user_input = a.split()
        if len(a) != 3 or user_input[0] != 'a' and user_input[0] != 'b' and user_input[0] != 'c':
            print('вы ошиблись, попробуйте еще раз')
        else:
            user_input[1] = int(user_input[1])
            if user_input[0] == 'a':
                user_input.pop(0)
                user_input.insert(0, 1)
            elif user_input[0] == 'b':
                user_input.pop(0)
                user_input.insert(0, 2)
            elif user_input[0] == 'c':
                user_input.pop(0)
                user_input.insert(0, 3)
            user_input_m = user_input[0]
            user_input_n = user_input[1]
            break


def move_x():
    if user_input_n in dict_ and user_input_n in dict_[user_input_m]:
        dict_[user_input_m].remove(user_input_n)
        ttt_x(user_input_m, user_input_n)
    else:
        print('вы ошиблись, попробуйте еще раз')
        inputs()
        move_x()


def move_O():
    if user_input_n in dict_ and user_input_n in dict_[user_input_m]:
        dict_[user_input_m].remove(user_input_n)
        ttt_O(user_input_m, user_input_n)
    else:
        print('вы ошиблись, попробуйте еще раз')
        inputs()
        move_O()



dict_ = {1: [1, 2, 3], 2: [1, 2, 3], 3: [1, 2, 3]}



n = 0
while n < 9:
    board()
    inputs()
    move_x()
    n = n + 1
    if n >= 9:
        print('ничья')
        board()
        break
    elif ((second_string[1] == 'x' and second_string[2] == 'x' and second_string[3] == 'x') or
        (third_string[1] == 'x' and third_string[2] == 'x' and third_string[3] == 'x') or
        (forth_string[1] == 'x' and forth_string[2] == 'x' and forth_string[3] == 'x') or
        (second_string[1] == 'x' and third_string[2] == 'x' and forth_string[3] == 'x') or
        (second_string[3] == 'x' and third_string[2] == 'x' and forth_string[1] == 'x') or
        (second_string[1] == 'x' and third_string[1] == 'x' and forth_string[1] == 'x') or
        (second_string[2] == 'x' and third_string[2] == 'x' and forth_string[2] == 'x') or
        (second_string[3] == 'x' and third_string[3] == 'x' and forth_string[3] == 'x')):
        print('Крестики выйграли')
        board()
        break
    else:
        board()
        inputs()
        move_O()
        n = n + 1
        if n >= 9:
            print('ничья')
            board()
            break
        elif ((second_string[1] == 'O' and second_string[2] == 'O' and second_string[3] == 'O') or
              (third_string[1] == 'O' and third_string[2] == 'O' and third_string[3] == 'O') or
              (forth_string[1] == 'O' and forth_string[2] == 'O' and forth_string[3] == 'O') or
              (second_string[1] == 'O' and third_string[2] == 'O' and forth_string[3] == 'O') or
              (second_string[3] == 'O' and third_string[2] == 'O' and forth_string[1] == 'O') or
              (second_string[1] == 'O' and third_string[1] == 'O' and forth_string[1] == 'O') or
              (second_string[2] == 'O' and third_string[2] == 'O' and forth_string[2] == 'O') or
              (second_string[3] == 'O' and third_string[3] == 'O' and forth_string[3] == 'O')):
            print('Нолики выйграли')
            board()
            break
else:
    board()
    print('ничья')




