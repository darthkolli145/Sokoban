from game_settings import *
from copy import deepcopy
x = deepcopy(board)
status = 1
def create_box(pBoard):
    for i in pBoard:
        for j in range(len(i)):
            print(i[j], end='')
            if j < len(i) - 1:
                print(" ", end='')
        print()
targets = []                                                    #list of targets
for i in range(len(board)):                                     #adds the target squares to the target list for later use
    for j in range(len(board[1])):
            if board[i][j] == TARGET or board[i][j] == BOX_S:
                targets.append([i, j])
def movement(mvmt):
    init_pos = checkposition(board)
    if move_input == "w":
        if board[init_pos[0]-1][init_pos[1]] == EMPTY or board[init_pos[0]-1][init_pos[1]] == TARGET:
            board[init_pos[0]-1][init_pos[1]] = SPRITE
            board[init_pos[0]][init_pos[1]] = EMPTY
        elif board[init_pos[0]-1][init_pos[1]] == BOX_S or board[init_pos[0]-1][init_pos[1]] == BOX_NS:
            if board[init_pos[0]-2][init_pos[1]] == EMPTY or board[init_pos[0]-2][init_pos[1]] == TARGET:
                if board[init_pos[0]-1][init_pos[1]] == BOX_NS:
                    board[init_pos[0]-2][init_pos[1]] = BOX_NS
                elif board[init_pos[0]-1][init_pos[1]] == BOX_S:
                    board[init_pos[0]-2][init_pos[1]] = BOX_NS
                board[init_pos[0]-1][init_pos[1]] = SPRITE
                board[init_pos[0]][init_pos[1]] = EMPTY
    elif move_input == "a":
        if board[init_pos[0]][init_pos[1]-1] == EMPTY or board[init_pos[0]][init_pos[1]-1] == TARGET:
            board[init_pos[0]][init_pos[1]-1] = SPRITE
            board[init_pos[0]][init_pos[1]] = EMPTY
        elif board[init_pos[0]][init_pos[1]-1] == BOX_NS or board[init_pos[0]][init_pos[1]-1] == BOX_S:
            if board[init_pos[0]][init_pos[1]-2] == EMPTY or board[init_pos[0]][init_pos[1]-2] == TARGET:
                if board[init_pos[0]][init_pos[1]-1] == BOX_NS:
                    board[init_pos[0]][init_pos[1]-2] = BOX_NS
                elif board[init_pos[0]][init_pos[1]-1] == BOX_S:
                    board[init_pos[0]][init_pos[1]-2] = BOX_NS
                board[init_pos[0]][init_pos[1]-1] = SPRITE
                board[init_pos[0]][init_pos[1]] = EMPTY
    elif move_input == "s":
        if board[init_pos[0]+1][init_pos[1]] == EMPTY or board[init_pos[0]+1][init_pos[1]] == TARGET:
            board[init_pos[0]+1][init_pos[1]] = SPRITE
            board[init_pos[0]][init_pos[1]] = EMPTY
        elif board[init_pos[0]+1][init_pos[1]] == BOX_S or board[init_pos[0]+1][init_pos[1]] == BOX_NS:
            if board[init_pos[0]+2][init_pos[1]] == EMPTY or board[init_pos[0]+2][init_pos[1]] == TARGET:
                if board[init_pos[0]+1][init_pos[1]] == BOX_NS:
                    board[init_pos[0]+2][init_pos[1]] = BOX_NS
                elif board[init_pos[0]+1][init_pos[1]] == BOX_S:
                    board[init_pos[0]+2][init_pos[1]] = BOX_NS
                board[init_pos[0]+1][init_pos[1]] = SPRITE
                board[init_pos[0]][init_pos[1]] = EMPTY
    elif move_input == "d":
        if board[init_pos[0]][init_pos[1]+1] == EMPTY or board[init_pos[0]][init_pos[1]+1] == TARGET:
            board[init_pos[0]][init_pos[1]+1] = SPRITE
            board[init_pos[0]][init_pos[1]] = EMPTY
        elif board[init_pos[0]][init_pos[1]+1] == BOX_S or board[init_pos[0]][init_pos[1]+1] == BOX_NS:
            if board[init_pos[0]][init_pos[1]+2] == EMPTY or board[init_pos[0]][init_pos[1]+2] == TARGET:
                if board[init_pos[0]][init_pos[1]+1] == BOX_NS:
                    board[init_pos[0]][init_pos[1]+2] = BOX_NS
                elif board[init_pos[0]][init_pos[1]+1] == BOX_S:
                    board[init_pos[0]][init_pos[1]+2] = BOX_NS
                board[init_pos[0]][init_pos[1]+1] = SPRITE
                board[init_pos[0]][init_pos[1]] = EMPTY
    if checkposition(board) in targets:
        board[checkposition(board)[0]][checkposition(board)[1]] = SPRITE_T
    for i in range(len(targets)):
        if board[targets[i][0]][targets[i][1]] == EMPTY:
            board[targets[i][0]][targets[i][1]] = TARGET
    for i in range(len(targets)):
        if board[targets[i][0]][targets[i][1]] == BOX_NS:
            board[targets[i][0]][targets[i][1]] = BOX_S
def checkposition(board):
    for i in range(len(board)):
        for j in range(len(board[1])):
            if board[i][j] == SPRITE or board[i][j] == SPRITE_T:
                return [i, j]
def checkforwin(board):
     for x in board:
        if BOX_NS in x:
            return False
     return True           
win = False
move_input = 'w'
while move_input != "q" and win == False:
    create_box(board)
    print('')
    move_input = input()
    while move_input != "w" and move_input != "a" and move_input != "s" and move_input != "d" and move_input != " " and move_input != "q":
        move_input = input("enter a valid move:\n")
    if move_input == 'q':
        break
    else:   
        if move_input == "w":
            movement(move_input)
        if move_input == "a":
            movement(move_input)
        if move_input == "s":
            movement(move_input)
        if move_input == "d":
            movement(move_input)
        if move_input == " ":
            board = deepcopy(x)
    win = checkforwin(board)
if win == True:
    create_box(board)
    print('You Win!')
else:
    print('Goodbye')
