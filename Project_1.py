import sys


def board_show():
    board = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
    print("That's your gamemap!")

    print(
        " {} | {} | {} \n-----------\n {} | {} | {} \n-----------\n {} | {} | {} ".format(board[0], board[1], board[2],
                                                                                          board[3], board[4], board[5],
                                                                                          board[6], board[7], board[8]))


def board_writing(board):
    return (
        " {} | {} | {} \n-----------\n {} | {} | {} \n-----------\n {} | {} | {} ".format(board[0], board[1], board[2],
                                                                                          board[3], board[4], board[5],
                                                                                          board[6], board[7], board[8]))


def start_game():
    choice = "wrong"

    while choice == "wrong":
        new_choice = input("Do u want start the game? (Yes or No): ")

        if new_choice.lower() == "yes":
            choice = new_choice
        elif new_choice.lower() == "no":
            sys.exit()
        else:
            print("Wrong pick, type Yes or No!")

    return choice


def player_choice():
    choice = "wrong"

    while choice == "wrong":

        new_choice = str(input("Player 1 choose (X or O): "))

        if new_choice.upper() == "X" or new_choice.upper() == "O":
            print("Player 1 picked {}.".format(new_choice.upper()))
            choice = new_choice
        else:
            print("Wrong pick!")

    return choice


def player_win(picks, player):
    if (1 in picks and 2 in picks and 3 in picks) or (4 in picks and 5 in picks and 6 in picks) or \
            (7 in picks and 8 in picks and 9 in picks) or (1 in picks and 4 in picks and 7 in picks) or \
            (2 in picks and 5 in picks and 8 in picks) or (3 in picks and 6 in picks and 9 in picks) or \
            (1 in picks and 5 in picks and 9 in picks) or (3 in picks and 5 in picks and 7 in picks):
        print("{} win!!".format(player.upper()))
        return True


def game(player_one):
    board = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
    # Showing players gamemap
    board_writing(board)

    if player_one.upper() == "X":
        player_2 = "O"
    else:
        player_2 = "X"

    picked_numbers = []
    player_1_numbers = []
    player_2_numbers = []
    full_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    while game:
        while True:

            # There, player is picking place on the board to put
            pick_player_1 = int(input("Player 1, pick place where you want place your symbol (from 1 to 9): "))

            # Checking if number is picked
            if pick_player_1 in picked_numbers:
                print("That number was picked!")
            # Checking that number picked by player_1 is not picked and is in range from 1 to 9
            elif pick_player_1 != picked_numbers and pick_player_1 in range(1, 10):
                board[pick_player_1 - 1] = "{}".format(player_one.upper())
                picked_numbers.append(pick_player_1)
                player_1_numbers.append(pick_player_1)
                print(board_writing(board))
                picked_numbers.sort()
                break
            # Wrong pick
            else:
                print("Pick number from 1 to 9!")

        # Check if player 1 is winning
        if player_win(player_1_numbers, player_one):
            break
        elif picked_numbers == full_list:
            print("Draw!")
            break

        while True:
            # There, player is picking place on the board to put
            pick_player_2 = int(input("Player 2, pick place where you want place your symbol (from 1 to 9): "))

            # Checking if number is picked
            if pick_player_2 in picked_numbers:
                print("That number was picked!")
            # Checking that number picked by player_1 is not picked and is in range from 1 to 9
            elif pick_player_2 != picked_numbers and pick_player_2 in range(1, 10):
                board[pick_player_2 - 1] = "{}".format(player_2.upper())
                picked_numbers.append(pick_player_2)
                player_2_numbers.append(pick_player_2)
                print(board_writing(board))
                break
            # Wrong pick
            else:
                print("Pick number from 1 to 9!")

        # check if player 2 is winning
        if player_win(player_2_numbers, player_2):
            break


while True:
    board_show()
    start_game()
    player_1 = player_choice()
    game(player_1)
