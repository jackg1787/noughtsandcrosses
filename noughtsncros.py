#Noughts and Crosses

turn = 1


#n = int(input("Enter a number for how large u want 2 play: "))
def sumColumn(m):
    return [sum(col) for col in zip(*m)]

def Grid(n):
    for i in range(0,n+1):
        print(" ---"*n)
        if i< n :
             print( "| 0 "*n ,"|", sep="")

#### Check for winner ####

def CheckWin():
    searcht = '.'
    for i in range(3):
         #rows
         if matrix[i][0] == matrix[i][1] and matrix[i][0] == matrix[i][2] and matrix[i][0] != '.' :
            print("We have a winner!")
            return 1
         #columns     
         elif matrix[0][i] == matrix[1][i] and matrix[0][i] == matrix[2][i] and matrix[0][i] != '.':
            print("We have a winner!")
            return 1
         #diagonals   
         elif matrix[0][0] == matrix[1][1] and matrix[0][0] == matrix[2][2] and matrix[0][0] != '.':
             print("We have a winner!")
             return 1
         elif matrix[0][2] == matrix[1][1] and matrix[0][2] == matrix[2][0] and matrix[0][2] != '.':
             print("We have a winner!")
             return 1
    # check board is full
    for sublist in matrix:
        if searcht in sublist:
            return 0

    print ("Game over - the board is filled")
    return 1

	
### check for valid inputs ###
             
def input_valid(move):
	# input has only two values
    if len(move) != 2:
        print ("Input must be two numbers in format row,col e.g.  1,2 ")
        return 0
    # check input is a number between 1 and 3 (inclusive)
    try:
        if (1 <= int(move[0]) <= 3) and (1 <= int(move[1]) <= 3):
            #position taken
            if matrix[int(move[0])-1][int(move[1])-1] != '.':
                print("Position taken you dopey twat")
                return 0
            return 1
        else:
            print("the board goes from 1 to 3 you fuck head")
            return 0
    except ValueError:
        print("the board goes from 1 to 3 you fuck head")
        return 0
    
### draw the board with the new choice ###
def draw_board(move,player):
    matrix[int(move[0])-1][int(move[1])-1]=player
    print(matrix[0],"\n",matrix[1],"\n",matrix[2], sep = "")
    
            
##############################################################################

# Game board
matrix = [['.','.','.'],['.','.','.',],['.','.','.']]
print(matrix[0],"\n",matrix[1],"\n",matrix[2], sep = "")

# while game not over: play game

while not CheckWin():
    move = [0]
    while not input_valid(move):
        player = turn % 2
        if player == 0:
            player = 2
            piece = 'O'
        else:
            piece = 'X'
        move = input("Player "+ str(player)+ ":")
        move = move.split(",")

    draw_board(move,piece)

    move = [0]
    turn +=1



