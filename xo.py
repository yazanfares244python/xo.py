# The module for the AI
import random as r
# XO function
def xo_game():
    # Positions handling
    positions = [str(num) for num in range(1, 10)]
    # XO board
    xo_board = [
        "1", "2", "3",
        "4", "5", "6",
        "7", "8", "9"
    ]
    # Win conditions
    win_conditions = [
        ["1", "2", "3"], ["4", "5", "6"], ["7", "8", "9"],
        ["1", "4", "7"], ["2", "5", "8"], ["3", "6", "9"],
        ["1", "5", "9"], ["3", "5", "7"]
    ]
    # XO display
    def xo_display():
        for spots in range(9):
            if spots == 2 or spots == 5:
                print(xo_board[spots])
                print("----------")
            elif spots == 8:
                print(xo_board[spots])
            else:
                print(xo_board[spots], end=" | ")
    # Win/Lose/Tie checker
    def condition_checker():
        for condition in win_conditions:
            if xo_board[int(condition[0])-1] == xo_board[int(condition[1])-1] == xo_board[int(condition[2])-1]:
                if xo_board[int(condition[0])-1] == xo_user:
                    xo_display()
                    print(f"Congratulations({xo_user}), You have won against the AI!")
                    exit()
                elif xo_board[int(condition[0])-1] == xo_ai:
                    xo_display()
                    print(f"Sorry the AI({xo_ai}) won, better luck next time!")
                    exit()
            elif all(spots not in positions for spots in xo_board):
                xo_display()
                print("It's a tie!")
                exit()
    # Position function
    def position_func():
        xo_display()
        return input("Enter your position(1-9) ->: ")
    # Main game function
    def start_game():
        choice = input("Enter your choice(X/O) ->: ").upper().strip()
        while True:
            if choice == "X":
                global xo_user
                global xo_ai
                xo_user = "X"
                xo_ai = "O"
                condition_checker()
                position = position_func()
                while True:
                    # Invalid position handling
                    if position not in positions:
                        print("Invalid position")
                        position = position_func()
                    # Taken position handling
                    elif xo_board[int(position)-1] not in positions:
                        print("Position already taken")
                        position = position_func()
                    else:
                        break
                xo_board[int(position)-1] = xo_user
                # AI position handling
                condition_checker()
                while True:
                        xo_ai_position = r.randint(0, 8)
                        if xo_board[xo_ai_position] not in positions:
                            continue
                        else:
                            xo_board[xo_ai_position] = xo_ai
                            break
            elif choice == "O":
                xo_user = "O"
                xo_ai = "X"
                # AI position handling
                condition_checker()
                while True:
                    xo_ai_position = r.randint(0, 8)
                    if xo_board[xo_ai_position] not in positions:
                        continue
                    else:
                        xo_board[xo_ai_position] = xo_ai
                        break
                condition_checker()
                position = position_func()
                while True:
                    # Invalid position handling
                    if position not in positions:
                        print("Invalid position")
                        position = position_func()
                    # Taken position handling
                    elif xo_board[int(position)-1] not in positions:
                        print("Position already taken")
                        position = position_func()
                    else:
                        break
                xo_board[int(position)-1] = xo_user
            else:
                print("Invalid choice")
                choice = input("Enter your choice(X/O) ->: ").upper().strip()
    start_game()
xo_game()