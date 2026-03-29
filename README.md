
# The module for the AI mode
import random as r

def xo_game():
    # For handling positions that arent in the board
    positions = [str(num) for num in range(1, 10)]
    # Win conditions
    win_condition = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8], # Horizontal
        [0, 3, 6], [1, 4, 7], [2, 5, 8], # Vertical
        [0, 4, 8], [2, 4, 6] # Diagonal
        
    ]
    # XO Board
    xo_board = [
        "1", "2", "3",
        "4", "5", "6",
        "7", "8", "9"
    ]
    # Display
    def xo_display():
        print(xo_board[0], end=" | ")
        print(xo_board[1], end=" | ")
        print(xo_board[2], end=" ")
        print("\n--------")
        print(xo_board[3], end=" | ")
        print(xo_board[4], end=" | ")
        print(xo_board[5], end=" ")
        print("\n--------")
        print(xo_board[6], end=" | ")
        print(xo_board[7], end=" | ")
        print(xo_board[8], end="\n")
    # Choice handling
    while True:
        choice = input("Enter your choice(X/O) ->: ").upper().strip()
        if choice == "X":
            xo_user = "X"
            xo_ai = "O"
            break
        elif choice == "O":
            xo_user = "O"
            xo_ai = "X"
            break
        else:
            print("Invalid choice")
    # Position handling
    def position_func():
        xo_display()
        return input("Enter your position(1-9) ->: ")
    # Game function
    def start_game():
            while True:
                # AI variable
                xo_ai_position = r.randint(0, 8)
                # Handling Taken Spots
                position = position_func()
                while True:
                    if position not in positions:
                        print("Invalid position choice")
                        position = position_func()
                    else:
                        if xo_board[int(position)-1] not in positions:
                            print("Posiiton already taken")
                            position = position_func()
                        else:
                            break
                xo_board[int(position)-1] = xo_user
                for condition in win_condition:
                    if xo_board[condition[0]] == xo_board[condition[1]] == xo_board[condition[2]]:
                        xo_display()
                        print("You won!") if xo_board[condition[0]] == xo_user else print("You lost")
                        exit()
                    else:
                        continue
                if all(spots not in xo_board for spots in xo_board):
                    print("Its' a tie!")
                    break
                while True:
                    if xo_board[xo_ai_position] not in positions:
                        xo_ai_position = r.randint(0, 8)
                    else:
                        break
                xo_board[xo_ai_position] = xo_ai
                for condition in win_condition:
                    if xo_board[condition[0]] == xo_board[condition[1]] == xo_board[condition[2]]:
                        xo_display()
                        print("You won!") if xo_board[condition[0]] == xo_user else print("You lost")
                        exit()
                    else:
                        continue
                if all(spots not in xo_board for spots in xo_board):
                    print("Its' a tie!")
                    break
    start_game()
xo_game()

