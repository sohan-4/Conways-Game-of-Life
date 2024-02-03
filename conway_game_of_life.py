
import time
import copy

def create_board(ix, iy):
    board=[]

    for i in range(iy):
        temp=[]
        for j in range(ix):
            temp.append('.')
        board.append(temp)

    return board

def print_board(iboard):

    for i in iboard:

        for j in i:
            print(j, end = " ")

        print()

def live_nbers(iboard, ix, iy):
    live_cells=0

    if (iy+1<len(iboard)):
        if (iboard[iy+1][ix] == 'X'):
            live_cells+=1
    
    if (iy+1<len(iboard) and ix+1<len(iboard[iy])):
        if (iboard[iy+1][ix+1] == 'X'):
            live_cells+=1

    if (ix+1<len(iboard[iy])):
        if (iboard[iy][ix+1] == 'X'):
            live_cells+=1

    if (ix+1<len(iboard[iy]) and iy-1>=0):
        if (iboard[iy-1][ix+1] == 'X'):
            live_cells+=1

    if (iy-1>=0):
        if (iboard[iy-1][ix] == 'X'):
            live_cells+=1

    if (iy-1>=0 and ix-1>=0):
        if (iboard[iy-1][ix-1] == 'X'):
            live_cells+=1

    if (ix-1>=0):
        if (iboard[iy][ix-1] == 'X'):
            live_cells+=1

    if (ix-1>=0 and iy+1<len(iboard)):
        if (iboard[iy+1][ix-1] == 'X'):
            live_cells+=1

    return live_cells


if __name__ ==  "__main__":

    print("Conway's Game of Life")
    x, y = map(int, input("Enter dimensions, separated by space, Horizontal first then Vertical:").split())
    
    board = create_board(x, y)
    print_board(board)

    point_x, point_y = -1,-1
    while (True):
        input_str = input("Enter dimensions where live cells will start, Horizontal coordinate then vertical, form:\n0 1 2\n1\n2\nsay \"quit\" to quit this step and move on\nsay \"show\" to see the current board\nsay \"delete\" to delete a live cell\n")
        if (input_str.lower() == "quit"):
            break
        elif (input_str.lower() == "show"):
            print_board(board)
            continue
        elif (input_str.lower() == "delete"):
            input_str = input("Enter cell you want to delete:\n")
            point_x, point_y = input_str.split()
            point_x = int(point_x)
            point_y = int(point_y)
            board[point_y][point_x] = '.'
            continue

        point_x, point_y = input_str.split()

        point_x = int(point_x)
        point_y = int(point_y)
        board[point_y][point_x] = 'X'

    print("This is currently your board:")
    print_board(board)

    ticks = int(input("How many ticks do you want: "))

    print("Starting game...")
    boards = []
    start = time.time()
    for i in range(ticks):
        org_board = copy.deepcopy(board)
        for j in range(len(board)):
            for k in range(len(board[j])):
                valid_surroudnings = live_nbers(org_board, k, j)
                if (board[j][k] == 'X'):
                    if (valid_surroudnings < 2 or valid_surroudnings > 3):
                        board[j][k] = '.'
                else:
                    if (valid_surroudnings == 3):
                        board[j][k] = 'X'
        boards.append(copy.deepcopy(board))

    end = time.time()
    print("Game over")
    print("It took a total of ", end-start, " seconds")
    
    for i in range(len(boards)):
        print("Tick ", i+1)
        print_board(boards[i])

    print()
