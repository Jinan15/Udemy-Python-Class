current_board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
valid_positions = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

def game_setup():
    # Get player count
    player_count = input("\nOne player or two players (enter 1 or 2): ")
    while player_count != '1' and player_count != '2':
        print("Invalid input: please enter 1 for one player or 2 for two players")
        player_count = input("1 player or 2 players (enter 1 or 2): ")
    player_count = int(player_count)

    # Determine player markers
    player1_marker = input("input player 1 marker (ex: X,O,etc): ")
    while len(player1_marker) != 1:
        print("Invalid input: please enter a 1 character marker")
        player1_marker = input("input player 1 marker (ex: X,O,etc): ")

    if player_count == 1:
        return [player1_marker, '☺', 1]
    elif player_count == 2:
        player2_marker = input("input player 2 marker (ex: X,O,etc): ")
        while len(player2_marker) != 1:
            print("Invalid input: please enter a 1 character marker")
            player2_marker = input("input player 2 marker (ex: X,O,etc): ")

        return [player1_marker, player2_marker, 2]

def get_position():
    value = input("Input position: ")

    while value not in valid_positions:
        print(f"Invalid position: valid positions are: {valid_positions}")
        value = input("Input position: ")

    valid_positions.remove(value)
    return (int(value) - 1)

def play_game(player1_marker, player2_marker):
    count = 0
    print_current_board(current_board)
    while (count < 9):
        if (count % 2 == 0):
            print("Player 1's turn")
            current_board[get_position()] = player1_marker
            if board_check(player1_marker) == 1:
                print_current_board(current_board)
                return 1
        else:
            print("Player 2's turn")
            current_board[get_position()] = player2_marker
            if board_check(player2_marker) == 1:
                print_current_board(current_board)
                return 2
        count += 1
        print_current_board(current_board)
    return 0

def board_check(player_marker):
    check = [player_marker, player_marker, player_marker]
    # Check if any row or column has a 3 in a row
    # Returns which player won if there is a 3 in a row
    for n in range(0, 3):
        if [current_board[0 + (n * 3)], current_board[1 + (n * 3)], current_board[2 + (n * 3)]] == check:
            return 1
        if [current_board[0 + n], current_board[3 + n], current_board[6 + n]] == check:
            return 1
    # Checks main diagonal and returns which player won
    if [current_board[0], current_board[4], current_board[8]] == check:
        return 1
    # Checks contra diagonal and returns which player won
    if [current_board[2], current_board[4], current_board[6]] == check:
        return 1
    # If no player won then return 0
    return 0

def board_input_example():
    print("Board positions are indicated below")
    print_current_board(['1', '2', '3', '4', '5', '6', '7', '8', '9'])

def print_current_board(x):
    print(f"\n   {x[0]}|{x[1]}|{x[2]}")
    print("   -+-+-")
    print(f"   {x[3]}|{x[4]}|{x[5]}")
    print("   -+-+-")
    print(f"   {x[6]}|{x[7]}|{x[8]}\n")

def winner_message(winner):
    if winner == 0:
        print("-=-=-=-=-")
        print("Tie Game")
        print("-=-=-=-=-")
    else:
        print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
        print(f"Congratulations Player {winner} Won!")
        print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")

print('-----------------------------------')
print("Welcome to my Tic Tac Toe game")
print('-----------------------------------')
player1_marker, player2_marker, num_players = game_setup()

if num_players == 1:
    print("Sorry but this game mode is a work in progress")
elif num_players == 2:
    new_game = True
    board_input_example()
    while new_game:
        winner_message(play_game(player1_marker, player2_marker))
        current_board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
        valid_positions = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
        print("Would you like to play again?")
        if input("Enter Y for yes and N for no: ").lower() != 'y':
            new_game = False
    print("Thank you for playing")
