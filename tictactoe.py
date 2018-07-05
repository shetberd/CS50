board = [" "]*10
x = 0
o = 0
def display_board(board):
        print("      |      |     ")
        print(f"  {board[7]}   |  {board[8]}   |   {board[9]}    ")
        print("      |      |       ")
        print("___________________")
        print("      |      |       ")
        print(f"   {board[4]}  |  {board[5]}   |   {board[6]}    ")
        print("      |      |       ")
        print("___________________")
        print("      |      |       ")
        print(f"   {board[1]}  |  {board[2]}   |   {board[3]}    ")
        print("      |      |       ")

def choose_marker():
    while True:
        marker = input("Choose X or O: ").upper()
        if marker == "X" or marker == "O":
            return marker
            break

def player_input():
        position = int(input("Choose a position: "))
        if position >= 1 and position <= 9:
            return position
        elif position == None:
            player_input()

def place_marker(pos, marker):
        global cmarker
        if board[pos] == " ":
            board[pos] = marker
            win_check(board,cmarker)
            if cmarker == "X":
                cmarker = "O"
            elif cmarker == "O":
                cmarker = "X"
        else:
            place_marker(player_input(),marker)

def win_check(board, mark):
    global start
    global x
    global o
    who_won = ((board[7] == mark and board[8] == mark and board[9] == mark) or
    (board[4] == mark and board[5] == mark and board[6] == mark) or
    (board[1] == mark and board[2] == mark and board[3] == mark) or
    (board[7] == mark and board[4] == mark and board[1] == mark) or
    (board[8] == mark and board[5] == mark and board[2] == mark) or
    (board[9] == mark and board[6] == mark and board[3] == mark) or
    (board[7] == mark and board[5] == mark and board[3] == mark) or
    (board[9] == mark and board[5] == mark and board[1] == mark))
    if who_won == True:
        print(f"{mark} has won!")
        if mark == "X":
            x += 1
        else:
            o += 1
        score(x,o)
        clear()
        if x == 3 or o == 3:
            play_again()

def clear():
    global board
    board = [" "]*10

def score(x,o):
    print(f"Current score:\nX: {x}\nO: {o} ")

def full(board):
    global start
    counter = 0
    for pos in board:
        if " " not in pos:
            counter += 1
    if counter == 9:
        print("Draw!")
        clear()

def play_again():
    global start
    global o
    global x
    play_input = input("Play again? Y / N").upper()
    if play_input == "Y":
        start = True
        o = 0
        x = 0
    elif play_input == "N":
        start = False
    else:
        play_again()


start = True
cmarker = choose_marker()
display_board(board)
while start == True:
    place_marker(player_input(),cmarker)
    full(board)
    display_board(board)
