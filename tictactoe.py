
#tictactoe game
#setup global variables and import

import random as rnd


X = 'X'
O = 'O'
EMPTY = ' '
TIE = 'TIE'
NUM_SQUARES = 9


def display_instruct():
    """display the instructions to the user"""
    print(
        """Welcome to the TicTacToe game human, you are playing against the silicon brain. GOOD LUCK!

You will make a move by entering 0-8. Your number will correspond to the number on the following TicTacToe board:

                                    0 | 1 | 2
                                    ---------
                                    3 | 4 | 5
                                    ---------
                                    6 | 7 | 8
---------------------------------------------------------------------------------------""")


def pieces():
    n = rnd.randrange(0, 2)
    # print(n)
    human = X
    computer = O
    if n == 0:
        return human, computer

    else:
        human = O
        computer = X
        return human, computer


def new_board():
    """ create a new board """
    """ create lists for values inside the board
    list -> [[0, 1, 2],       0 | 1 | 2 
             [3, 4, 5],  -->  3 | 4 | 5
             [6, 7, 8]]       6 | 7 | 8

             """

    board = []

    for square in range(NUM_SQUARES):
        board.append(EMPTY)
    return board


def display_board(board):
    print("\n\t", board[0], "|", board[1], "|", board[2])
    print("\t", "----------")
    print("\t", board[3], "|", board[4], "|", board[5])
    print("\t", "----------")
    print("\t", board[6], "|", board[7], "|", board[8], "\n")


def legal_moves(board):
    """create a list of all legal moves possible in the current board"""
    moves = []
    for square in range(NUM_SQUARES):
        if board[square] == EMPTY:
            "takes the index of the empty spaces and puts them in a list"
            moves.append(square)
    return moves


def winner(board):
    """checks board for a winner"""
    ways_to_win = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8),
                   (0, 4, 8), (2, 4, 6))

    for row in ways_to_win:
        """this cycles through ways to win and sees if there are three matching symbols(x or o)"""
        if board[row[0]] == board[row[1]] == board[row[2]] != EMPTY:
            winner = board[row[0]]
            return winner

        if EMPTY not in board:
            return TIE

    return None


def human_move(board, human):
    """ask for legal move by human, check move, if not legal ask again"""
    legal = legal_moves(board)
    # print(legal)
    move = None
    while move not in legal:
        # keep looping until player enters a legal move
        move = int(input("Please enter a legal move as an Integer: "))
        if move not in legal:
            print("\n That square is already taken. Please enter a new move. \n")
    print("Nice move!")
    return move


def computer_move(board, human, computer):
    # making new board because 1st board is immutable
    board = board[:]
    # ------AI Logic--------
    # if comp has a winning move, it should
    # if comp can stop human from winning it should make that move
    # comp should go for center square, then corner squares
    # if center and square != empty, choose a random square
    best_moves = (4, 0, 2, 6, 8, 1, 3, 5, 7)
    print("Computer: I will take square number", end=" ")

    legal = legal_moves(board)
    #going through legal moves to check for winning conditions
    for move in legal:
        #temp put computer's symbol in square and check if it results ina winning condition
        board[move] = computer
        if winner(board) == computer:
            print(move)
            return move
        #if no winning moves, don't make the move yet
        board[move] = EMPTY

        # check to see if there is a space that could give the human a winning condition
    for move in legal:
        board[move] = human
        if winner(board) == human:
            print(move)
            return move
        board[move] = EMPTY

    for move in best_moves:
        if move in legal:
            print(move)
            return move


def next_turn(turn):
    if turn == 'X':
        return 'O'
    else:
        return 'X'


def main():
    display_instruct()
    computer, human = pieces()
    turn = 'X'
    board = new_board()
    # display_board(board)

    while not winner(board):
        # loop that goes on until game is over
        if turn == human:
            # human turn and make move on board
            move = human_move(board, human)
            board[move] = human
        else:
            # computers turn and put move in to board
            move = computer_move(board, human, computer)
            board[move] = computer
        display_board(board)
        turn = next_turn(turn)

    #winning condition has been met
    the_winner = winner(board)
    if the_winner == human:
        print("Congratulations, you have won TicTacToe!")
    elif the_winner == computer:
        print("You let a brainless computer beat you!")
    elif the_winner == TIE:
        print("It's a tie! work on being smarter than a computer and play again!")


if __name__ == "__main__":
    main()