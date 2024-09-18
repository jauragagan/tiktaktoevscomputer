import random

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board, player):
    win_conditions = [
        [board[0][0], board[0][1], board[0][2]],
        [board[1][0], board[1][1], board[1][2]],
        [board[2][0], board[2][1], board[2][2]],
        [board[0][0], board[1][0], board[2][0]],
        [board[0][1], board[1][1], board[2][1]],
        [board[0][2], board[1][2], board[2][2]],
        [board[0][0], board[1][1], board[2][2]],
        [board[2][0], board[1][1], board[0][2]],
    ]
    return [player, player, player] in win_conditions

def get_empty_positions(board):
    empty_positions = []
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                empty_positions.append((i, j))
    return empty_positions

def player_move(board):
    while True:
        try:
            row = int(input("Enter the row (0, 1, 2): "))
            col = int(input("Enter the column (0, 1, 2): "))
            if board[row][col] == " ":
                board[row][col] = "X"
                break
            else:
                print("This position is already taken.")
        except (ValueError, IndexError):
            print("Invalid input. Please enter numbers between 0 and 2.")

def computer_move(board):
    empty_positions = get_empty_positions(board)
    move = random.choice(empty_positions)
    board[move[0]][move[1]] = "O"

def main():
    board = [[" " for _ in range(3)] for _ in range(3)]
    print("Welcome to Tic Tac Toe!")
    print_board(board)

    for turn in range(9):
        if turn % 2 == 0:
            print("Player's turn.")
            player_move(board)
        else:
            print("Computer's turn.")
            computer_move(board)
        
        print_board(board)
        
        if check_winner(board, "X"):
            print("Player wins!")
            return
        elif check_winner(board, "O"):
            print("Computer wins!")
            return
    
    print("It's a tie!")

if __name__ == "__main__":
    main()
