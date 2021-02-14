board = {
    '1': ' ', '2': ' ', '3': ' ',
    '4': ' ', '5': ' ', '6': ' ',
    '7': ' ', '8': ' ', '9': ' ',
}


def printBoard():
    print(board['1'] + '  | ' + board['2'] + ' | ' + board['3'])
    print('___+___+___')
    print(board['4'] + '  | ' + board['5'] + ' | ' + board['6'])
    print('___+___+___')
    print(board['7'] + '  | ' + board['8'] + ' | ' + board['9'])


def game():
    i = 1
    turn = 'X'
    while i > 0:
        if (turn == 'X'):
            print()
            printBoard()
            field = str(input("O pic the field: "))
            board[str(field)] = 'O'
            turn = 'O'
            printBoard()
        else:
            print()
            printBoard()
            field = str(input("X pic the field: "))
            board[str(field)] = 'X'
            turn = 'X'
            printBoard()

        if board['1'] == board['2'] == board['3'] == 'X':
            print(' X win ')
            break
        elif board['4'] == board['5'] == board['6'] == 'X':
            print(' X win ')
            break
        elif board['7'] == board['8'] == board['9'] == 'X':
            print(' X win ')
            break
        elif board['1'] == board['5'] == board['9'] == 'X':
            print(' X win ')
            break
        elif board['3'] == board['5'] == board['7'] == 'X':
            print(' X win ')
            break
        elif board['1'] == board['4'] == board['7'] == 'X':
            print(' X win ')
            break
        elif board['2'] == board['5'] == board['8'] == 'X':
            print(' X win ')
            break
        elif board['3'] == board['6'] == board['9'] == 'X':
            print(' X win ')
            break

        if board['1'] == board['2'] == board['3'] == 'O':
            print(' O win ')
            break
        elif board['4'] == board['5'] == board['6'] == 'O':
            print(' O win ')
            break
        elif board['7'] == board['8'] == board['9'] == 'O':
            print(' O win ')
            break
        elif board['1'] == board['5'] == board['9'] == 'O':
            print(' O win ')
            break
        elif board['3'] == board['5'] == board['7'] == 'O':
            print(' O win ')
            break
        elif board['1'] == board['4'] == board['7'] == 'O':
            print(' O win ')
            break
        elif board['2'] == board['5'] == board['8'] == 'O':
            print(' O win ')
            break
        elif board['3'] == board['6'] == board['9'] == 'O':
            print(' O win ')
            break


game()
