board = ['_', '_', '_',
        '_', '_', '_',
        '_', '_', '_']
currentPlayer = "X"
winner = None
gameRunning = True

#printing board
def printBoard(board):
    print(board[0] , "  " , board[1] , "  " , board[2])
    print(board[3] , "  " , board[4] , "  " , board[5])
    print(board[6] , "  " , board[7] , "  " , board[8])

#take player input
def playerInput(board):
    while True:
        if currentPlayer == "X":
            inp = int(input(f"Enter a number 1-9 {currentPlayer}'s turn: "))
        else:
            inp = int(input(f"Enter a number 1-9 {currentPlayer}: "))
        if inp >= 1 and inp <= 9 and board[inp-1] == "_":
            board[inp-1] = currentPlayer
            break
        else:
            if currentPlayer == "X":
                print(f"Oops! Try again! Already filled.")
            else:
                print(f"Oops! Try again! Already filled.")
            printBoard(board)

#check for win or tie
def checkHorizontal(board):
    global winner
    if (board[0] == board[1] == board[2] and board[0] != "_") or (board[3] == board[4] == board[5] and board[3] != "_") or (board[6] == board[7] == board[8] and board[6] != "_"):
        winner = currentPlayer
        return True
def checkRow(board):
    global winner
    if (board[0] == board[3] == board[6] and board[0] != "_") or (board[1] == board[4] == board[7] and board[1] != "_") or (board[2] == board[5] == board[8] and board[2] != "_"):
        winner = currentPlayer
        return True
def checkDiagonal(board):
    global winner
    if (board[0] == board[4] == board[5] and board[0] != "_") or (board[2] == board[4] == board[6] and board[2] != "_"):
        winner = currentPlayer
        return True
def checkTie(board):
    global gameRunning
    if "_" not in board:
        printBoard(board)
        print("Its a tie")
        gameRunning = False

def checkWin():
    if checkDiagonal(board) or checkHorizontal(board) or checkRow(board):
        print(f"The winner is {winner}")

#switch the player
def switchPlayer():
    global currentPlayer
    if currentPlayer == "X":
        currentPlayer = "O"
    else:
        currentPlayer = "X"

#check for win or tie again
while gameRunning:
    printBoard(board)
    if winner != None:
        break
    playerInput(board)
    checkWin()
    checkTie(board)
    switchPlayer()