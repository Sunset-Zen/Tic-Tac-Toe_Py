import random

# ( Game Global Variables / Attributes )
end_game = False
multiplayer_decision, player1_symbol, player2_symbol, cpu_symbol = '', '', '', ''
game_symbols = ['X', 'O', ' ']
tic_tac_toe_board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
string_board = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
turn_array = ['Heads', 'Tails']
coin_flip = random.randint(0, 1)

player1_first = False
player2_first = False
cpu_first = False


# ( Game Functions )
def board_display():
    # Display Tic Tac Toe Board (version 2)
    print('')
    tracker = 0
    for row in string_board:
        for element in row:
            tracker += 1
            if tracker == 3:
                print(element, end=' ')
                tracker -= 3
            else:
                print(element, end=' | ')
        print()
    print('')
def slot_check(a, b):
    # Base Condition
    if tic_tac_toe_board[a][b] == 0:
        return [a, b]
    else:
        temp_a = random.randint(0, 2)
        temp_b = random.randint(0, 2)
        slot_check(temp_a, temp_b)

print('_________________________________________________'*2)
print('\nWelcome To Tic Tac Toe')
print('Developed by : Otis Ray Jackson IV')

# ( Display Ruleset )
print('_________________________________________________'*2)
print('\n( Basic Ruleset of Tic Tac Toe )')
print('_________________________________________________'*2)
print('Depending on who goes first, [CPU, Player1, Player2]\tTurns granted are 5 while the latter is 4.')
print('100% Indexed && Turn based application.\t\t\t\t\t** ( Indexes start from 0 & Ends at 2 ) ** ')
print('Select Box Example : => \t\t\t\t\t\t\t\t0 0\t [Row, Column]\n')

# ( Ask if multiplayer -> ( ... ))
multiplayer_decision = input('Multiplayer? Type A for [Yes] and B for [No]:\t')
if multiplayer_decision == 'A':
    # ( Set user 1 symbol )
    player1_symbol = input('[Player 1] Please pick a symbol [X] or [O]: \t')
    # ( Set user 2 symbol )
    player2_symbol = input('[Player 2] Please pick a symbol [X] or [O]: \t')
    # ( Determines who goes first )
    user_guess = input('\n[Player 1] Pick / Type Heads or Tails: \t')
    user_guess2 = input('\n[Player 2] Pick / Type Heads or Tails: \t')
    if user_guess == turn_array[coin_flip]:
        player1_first = True
        player1_moves, player2_moves = 5, 4
        print('Player 1 Goes First !')
    else:
        player2_first = True
        player1_moves, player2_moves = 4, 5
        print('Player 2 Goes First !')
elif multiplayer_decision == 'B':
    # ( Receive user symbol )
    player1_symbol = input('[Player 1] Please pick a symbol [X] or [O]: \t')
    player2_symbol = None
    if player1_symbol == 'X':
        cpu_symbol = 'O'
    if player1_symbol == 'O':
        cpu_symbol = 'X'
    # ( Determines who goes first )
    user_guess = input('\nPick / Type Heads or Tails: \t')
    if user_guess == turn_array[coin_flip]:
        player1_first = True
        player1_moves, player2_moves = 5, 4
        print('Player Goes First !')
    else:
        cpu_first = True
        player1_moves, player2_moves = 4, 5
        print('CPU Goes First !')

# ( Display Board )
board_display()

# ( In Game Attributes )
keep_playing = False
board_count = 0

# ( Game Loop Logic)
if player1_first:
    while 0 < player1_moves <= 5:
        temp1, temp2 = [], []

        # ( Ask Player 1 for Input )
        resp = input('(Player 1) Enter indexed location: (row) (column)\t')
        temp1.append(int(resp[0]))
        temp1.append(int(resp[2]))

        # ( Update tic_tac_toe Board )
        tic_tac_toe_board[int(resp[0])][int(resp[2])] = 1
        string_board[int(resp[0])][int(resp[2])] = player1_symbol
        board_count += 1
        player1_moves -= 1

        # ( Debug )
        print('\nCurrent Slots (num):' + str(tic_tac_toe_board))
        print('Current Slots (str):' + str(string_board))

        # ( If Multiplayer ( Player Two Turn ) )
        if multiplayer_decision == 'A' and 0 < player2_moves <= 4:
            resp = input('\n(Player 2) Enter indexed location: (row) (column)\t')
            temp2.append(int(resp[0]))
            temp2.append(int(resp[2]))

            # ( Update tic_tac_toe board )
            tic_tac_toe_board[int(resp[0])][int(resp[2])] = 1
            string_board[int(resp[0])][int(resp[2])] = player2_symbol
            board_count += 1
            player2_moves -= 1

        # ( If CPU ( Player Two Turn ) )
        elif multiplayer_decision == 'B' and 0 < player2_moves <= 4:
            # ( CPU turn )
            cpu_row = random.randint(0, 2)
            cpu_column = random.randint(0, 2)

            if tic_tac_toe_board[cpu_row][cpu_column] == 1:
                # ( re-roll )
                while tic_tac_toe_board[cpu_row][cpu_column] == 1:
                    if tic_tac_toe_board[cpu_row][cpu_column] == 0:
                        break
                    cpu_row = random.randint(0, 2)
                    cpu_column = random.randint(0, 2)
                print('\n*** CPU rerolled ***')

            # ( Display CPU Input )
            print('\n(CPU_Player) Entered indexed location: (row) (column)\t' + str(cpu_row) + ' ' + str(cpu_column))

            resp = str(cpu_row) + ' ' + str(cpu_column)
            temp2.append(int(resp[0]))
            temp2.append(int(resp[2]))

            # ( Update Tic Tac Toe Board ( CPU ) )
            tic_tac_toe_board[int(resp[0])][int(resp[2])] = 1
            string_board[int(resp[0])][int(resp[2])] = cpu_symbol
            board_count += 1
            player2_moves -= 1

            # ( Debug )
            print('\nCurrent Slots (num):' + str(tic_tac_toe_board))
            print('Current Slots (str):' + str(string_board))

        # ( Display Board )
        board_display()
    # Print End Game Contents or Restart Loop
    print('\nGAME OVER !!! \n')
elif cpu_first:
    while 0 < player2_moves <= 5:
        temp1, temp2 = [], []

        # ( CPU turn )
        cpu_row = random.randint(0, 2)
        cpu_column = random.randint(0, 2)

        if tic_tac_toe_board[cpu_row][cpu_column] == 1:
            # ( re-roll )
            while tic_tac_toe_board[cpu_row][cpu_column] == 1:
                if tic_tac_toe_board[cpu_row][cpu_column] == 0:
                    break
                cpu_row = random.randint(0, 2)
                cpu_column = random.randint(0, 2)
            print('\n*** CPU rerolled ***')

        # ( Ask Player 1 for Input )
        print('\n(CPU_Player) Entered indexed location: (row) (column)\t' + str(cpu_row) + ' ' + str(cpu_column))

        resp = str(cpu_row) + ' ' + str(cpu_column)
        temp1.append(int(resp[0]))
        temp1.append(int(resp[2]))

        # ( Update tic_tac_toe Board )
        tic_tac_toe_board[int(resp[0])][int(resp[2])] = 1
        string_board[int(resp[0])][int(resp[2])] = cpu_symbol
        board_count += 1
        player2_moves -= 1

        # ( Debug )

        if 0 < player1_moves <= 4:
            # ( Ask Player 1 for Input )
            resp = input('\n(Player 1) Enter indexed location: (row) (column)\t')
            temp1.append(int(resp[0]))
            temp1.append(int(resp[2]))

            # ( Update tic_tac_toe Board )
            tic_tac_toe_board[int(resp[0])][int(resp[2])] = 1
            string_board[int(resp[0])][int(resp[2])] = player1_symbol
            board_count += 1
            player1_moves -= 1

        # ( Update Tic Tac Toe Board ( CPU ) )
        board_display()
    # Print End Game Contents or Restart Loop
    print('\nGAME OVER !!! \n')
elif player2_first:
    while 0 < player2_moves <=5:
        temp1, temp2 = [], []

        # ( Ask Player 2 for Input )
        resp = input('(Player 2) Enter indexed location: (row) (column)\t')
        temp1.append(int(resp[0]))
        temp1.append(int(resp[2]))

        # ( Update tic_tac_toe Board )
        tic_tac_toe_board[int(resp[0])][int(resp[2])] = 1
        string_board[int(resp[0])][int(resp[2])] = player2_symbol
        board_count += 1
        player2_moves -= 1

        # ( Debug )
        print('\nCurrent Slots (num):' + str(tic_tac_toe_board))
        print('Current Slots (str):' + str(string_board))

        # ( If Multiplayer ( Player Two Turn ) )
        if multiplayer_decision == 'A' and player1_moves > 0:
            resp = input('\n(Player 1) Enter indexed location: (row) (column)\t')
            temp2.append(int(resp[0]))
            temp2.append(int(resp[2]))

            # ( Update tic_tac_toe board )
            tic_tac_toe_board[int(resp[0])][int(resp[2])] = 1
            string_board[int(resp[0])][int(resp[2])] = player1_symbol
            board_count += 1
            player1_moves -= 1

            # ( Debug )
            print('\nCurrent Slots (num):' + str(tic_tac_toe_board))
            print('Current Slots (str):' + str(string_board))

        # ( Display Board )
        board_display()
    # Print End Game Contents or Restart Loop
    print('\nGAME OVER !!! \n')



