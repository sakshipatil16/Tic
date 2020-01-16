import random
def display_board(board):
    #clear_output()
    print(board[1]+'|'+board[2]+'|'+board[3])
    print('------')
    print(board[4]+'|'+board[5]+'|'+board[6])
    print('------')
    print(board[7]+'|'+board[8]+'|'+board[9])
def player_input():
    markers=' '
    print("player 1 : choose  X or 0")
    markers=input("player 1= ")
    if markers=='X':
        return('X','0')
    else:
        return('0','X')
def play_first():
    flip=random.randint(0,1)
    if flip==0:
        return('player1')
    else:
        return('player2')
def player_choice(board):
    position=int(input("enter the number where you want to place your marker= "))
    return position
def place_marker(board,marker,position):
    board[position]=marker
def win_check(board,marker):
    if((board[1]==board[2]==board[3]==marker)or(board[4]==board[5]==board[6]==marker)or(board[7]==board[8]==board[9]==marker)or(board[1]==board[4]==board[7]==marker)or(board[2]==board[5]==board[8]==marker)or(board[3]==board[6]==board[9]==marker)or(board[3]==board[5]==board[7]==marker)or(board[1]==board[5]==board[9]==marker)):
        return(True)
    else:
        return(False)
def space_check(board,position):
    return board[position]==' '
def position_check(board):
    for i in range(1,10):
        if space_check(board,i):
            return(False)
        else:
            return(True)
def full_board_check():
    for i in range(1,10):
        if space_check(board,i):
            return(False)
print("Play Tic Tac Toe")
board=['#',' ',' ',' ',' ',' ',' ',' ',' ',' ']               
display_board(board)
player1,player2=player_input()
print('player 2='+player2)
turn=play_first()
print("first chance:"+turn)
play_game=input("ready to play? yes or no:")
if(play_game=='yes'):
    game_on=True
else:
    game_on=False
while game_on :       
    if(turn=='player1'):
        display_board(board)
        position=player_choice(board)
        place_marker(board,player1,position)
        if(win_check(board,player1)):
            print("player1 won")
        elif(full_board_check):
            print("tie")
        else:
            print('player 2 play')
            turn=player2
            position=player_choice(board)
            place_marker(board,player2,position)
            display_board(board)